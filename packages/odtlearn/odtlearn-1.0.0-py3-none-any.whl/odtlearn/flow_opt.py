from sklearn.utils.validation import check_array, check_is_fitted, check_X_y

from odtlearn import ODTL
from odtlearn.flow_opt_ms import FlowOPTMultipleSink
from odtlearn.flow_opt_ss import FlowOPTSingleSink
from odtlearn.utils.validation import (
    check_binary,
    check_columns_match,
    check_ipw,
    check_y,
    check_y_hat,
)


class FlowOPT_IPW(FlowOPTSingleSink):
    """
    An optimal decision tree that prescribes treatments (as opposed to predicting class labels),
    fitted on a binary-valued observational data set.

    Parameters
    ----------
    solver: str
        A string specifying the name of the solver to use
        to solve the MIP. Options are "Gurobi" and "CBC".
        If the CBC binaries are not found, Gurobi will be used by default.
    depth : int, default=1
        A parameter specifying the depth of the tree to learn.
    time_limit : int
        The given time limit for solving the MIP in seconds.
    method : str, default='IPW'
        The method of Prescriptive Trees to run. Choices in ('IPW', 'DM', 'DR), which represents the
        inverse propensity weighting, direct method, and doubly robust methods, respectively.
    num_threads: int, default=None
        The number of threads the solver should use. If not specified,
        solver uses all available threads.
    verbose : bool, default = False
        Flag for logging solver outputs.

    """

    def __init__(
        self,
        solver,
        depth=1,
        time_limit=60,
        num_threads=None,
        verbose=False,
    ) -> None:
        super().__init__(
            solver,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

    def fit(self, X, t, y, ipw):
        """Method to fit the PrescriptiveTree class on the data

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The training input samples.
        t : array-like, shape (n_samples,)
            The treatment values. An array of int.
        y : array-like, shape (n_samples,)
            The observed outcomes upon given treatment t. An array of int.
        ipw : array-like, shape (n_samples,)
            The inverse propensity weight estimates. An array of floats in [0, 1].

        Returns
        -------
        self : object
            Returns self.
        """
        # store column information and dtypes if any
        self._extract_metadata(X, y, t)

        # this function returns converted X and t but we retain metadata
        X, t = check_X_y(X, t)

        # need to check that t is discrete, and/or convert -- starts from 0 in accordance with indexing rule
        try:
            t = t.astype(int)
        except TypeError:
            print("The set of treatments must be discrete.")

        assert (
            min(t) == 0 and max(t) == len(set(t)) - 1
        ), "The set of treatments must be discrete starting from {0, 1, ...}"

        # we also need to check on y and ipw/y_hat depending on the method chosen
        y = check_y(X, y)
        self._ipw = check_ipw(X, ipw)

        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)

        self._create_main_problem()
        self._solver.optimize(self._X, self, self._solver)

        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

        # Return the classifier
        return self

    def predict(self, X):
        """Method for making prescriptions using a PrescriptiveTree classifier

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        t : ndarray, shape (n_samples,)
            The prescribed treatments for the input samples.
        """

        # Check if fit had been called
        check_is_fitted(self, ["b_value", "w_value", "p_value"])

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        X = check_array(X)

        check_columns_match(self._X_col_labels, X)

        return self._make_prediction(X)


class FlowOPT_DM(FlowOPTMultipleSink):
    def __init__(
        self,
        solver,
        depth=1,
        time_limit=60,
        num_threads=None,
        verbose=False,
    ) -> None:
        """
        An optimal decision tree that prescribes treatments (as opposed to predicting class labels),
        fitted on a binary-valued observational data set.

        Parameters
        ----------
        solver: str
            A string specifying the name of the solver to use
            to solve the MIP. Options are "Gurobi" and "CBC".
            If the CBC binaries are not found, Gurobi will be used by default.
        depth : int, default=1
            A parameter specifying the depth of the tree to learn.
        time_limit : int, default=60
            The given time limit for solving the MIP in seconds.
        num_threads: int, default=None
            The number of threads the solver should use. If not specified,
            solver uses all available threads
        verbose: bool, default=False
            Flag for logging solver outputs.

        """
        super().__init__(
            solver,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

    def _define_objective(self):
        # define objective function
        obj = self._solver.lin_expr(0)
        for i in self._datapoints:
            for n in self._tree.Nodes + self._tree.Leaves:
                for k in self._treatments:
                    obj += self._zeta[i, n, k] * (
                        self._y_hat[i][int(k)]
                    )  # we assume that each column corresponds to an ordered list t, which might be problematic

        self._solver.set_objective(obj, ODTL.MAXIMIZE)

    def fit(self, X, t, y, y_hat):
        """Method to fit the PrescriptiveTree class on the data

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The training input samples.
        t : array-like, shape (n_samples,)
            The treatment values. An array of int.
        y : array-like, shape (n_samples,)
            The observed outcomes upon given treatment t. An array of int.
        y_hat: array-like, shape (n_samples, n_treatments)
            The counterfactual predictions.


        Returns
        -------
        self : object
            Returns self.
        """
        # store column information and dtypes if any
        self._extract_metadata(X, y, t)

        # this function returns converted X and t but we retain metadata
        X, t = check_X_y(X, t)

        # need to check that t is discrete, and/or convert -- starts from 0 in accordance with indexing rule
        try:
            t = t.astype(int)
        except TypeError:
            print("The set of treatments must be discrete.")

        assert (
            min(t) == 0 and max(t) == len(set(t)) - 1
        ), "The set of treatments must be discrete starting from {0, 1, ...}"

        # we also need to check on y and ipw/y_hat depending on the method chosen
        y = check_y(X, y)
        self._y_hat = check_y_hat(X, self._treatments, y_hat)

        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)

        self._create_main_problem()
        self._solver.optimize(self._X, self, self._solver)

        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

        # Return the classifier
        return self

    def predict(self, X):
        """Classify test points using the StrongTree classifier

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y : ndarray, shape (n_samples,)
            The label for each sample is the label of the closest sample
            seen during fit.
        """
        # Check is fit had been called
        # for now we are assuming the model has been fit successfully if the fitted values for b, w, and p exist
        check_is_fitted(self, ["b_value", "w_value", "p_value"])

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        X = check_array(X)

        check_columns_match(self._X_col_labels, X)

        return self._make_prediction(X)


class FlowOPT_DR(FlowOPTMultipleSink):
    def __init__(
        self, solver, depth=1, time_limit=60, num_threads=None, verbose=False
    ) -> None:
        """
        An optimal decision tree that prescribes treatments (as opposed to predicting class labels),
        fitted on a binary-valued observational data set.

        Parameters
        ----------
        solver: str
            A string specifying the name of the solver to use
            to solve the MIP. Options are "Gurobi" and "CBC".
            If the CBC binaries are not found, Gurobi will be used by default.
        depth : int
            A parameter specifying the depth of the tree
        time_limit : int
            The given time limit for solving the MIP in seconds
        num_threads: int, default=None
            The number of threads the solver should use
        verbose: bool, default=False
            Display solver output.

        """
        super().__init__(solver, depth, time_limit, num_threads, verbose)

    def fit(self, X, t, y, ipw, y_hat):
        """Method to fit the PrescriptiveTree class on the data

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The training input samples.
        t : array-like, shape (n_samples,)
            The treatment values. An array of int.
        y : array-like, shape (n_samples,)
            The observed outcomes upon given treatment t. An array of int.
        ipw : array-like, shape (n_samples,)
            The inverse propensity weight estimates. An array of floats in [0, 1].
        y_hat: array-like, shape (n_samples, n_treatments)
            The counterfactual predictions.


        Returns
        -------
        self : object
            Returns self.
        """
        # store column information and dtypes if any
        self._extract_metadata(X, y, t)

        # this function returns converted X and t but we retain metadata
        X, t = check_X_y(X, t)

        # need to check that t is discrete, and/or convert -- starts from 0 in accordance with indexing rule
        try:
            t = t.astype(int)
        except TypeError:
            print("The set of treatments must be discrete.")

        assert (
            min(t) == 0 and max(t) == len(set(t)) - 1
        ), "The set of treatments must be discrete starting from {0, 1, ...}"

        # we also need to check on y and ipw/y_hat depending on the method chosen
        y = check_y(X, y)
        self._ipw = check_ipw(X, ipw)
        self._y_hat = check_y_hat(X, self._treatments, y_hat)

        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)

        self._create_main_problem()
        self._solver.optimize(self._X, self, self._solver)

        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

        # Return the classifier
        return self

    def predict(self, X):
        """Classify test points using the StrongTree classifier

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y : ndarray, shape (n_samples,)
            The label for each sample is the label of the closest sample
            seen during fit.
        """
        # Check is fit had been called
        # for now we are assuming the model has been fit successfully if the fitted values for b, w, and p exist
        check_is_fitted(self, ["b_value", "w_value", "p_value"])

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        X = check_array(X)

        check_columns_match(self._X_col_labels, X)

        return self._make_prediction(X)

    def _define_objective(self):
        # define objective function
        obj = self._solver.lin_expr(0)
        for i in self._datapoints:
            for n in self._tree.Nodes + self._tree.Leaves:
                for k in self._treatments:
                    obj += self._zeta[i, n, k] * (
                        self._y_hat[i][int(k)]
                    )  # we assume that each column corresponds to an ordered list t, which might be problematic
                    if self._t[i] == int(k):
                        obj += (
                            self._zeta[i, n, k]
                            * (self._y[i] - self._y_hat[i][int(k)])
                            / self._ipw[i]
                        )
        self._solver.set_objective(obj, ODTL.MAXIMIZE)
