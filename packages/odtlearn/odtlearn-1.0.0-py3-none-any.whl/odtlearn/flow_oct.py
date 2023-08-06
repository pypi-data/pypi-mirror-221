from sklearn.utils.multiclass import unique_labels
from sklearn.utils.validation import check_array, check_is_fitted, check_X_y

from odtlearn import ODTL
from odtlearn.flow_oct_ss import FlowOCTSingleSink
from odtlearn.utils.callbacks import BendersCallback
from odtlearn.utils.validation import check_binary, check_columns_match


class FlowOCT(FlowOCTSingleSink):
    """An optimal decision tree classifier, fitted on a given
    integer-valued data set to produce a provably optimal
    decision tree.

    Parameters
    ----------
    solver: str
        A string specifying the name of the solver to use
        to solve the MIP. Options are "Gurobi" and "CBC".
        If the CBC binaries are not found, Gurobi will be used by default.
    _lambda: float, default = 0
            The regularization parameter in the objective, taking values
            between 0 and 1, that controls
            the complexity of a the learned tree.
    obj_mode: str, default="acc"
        The objective should be used to learn an optimal decision tree.
        The two options are "acc" and "balance".
        The accuracy objective attempts to maximize prediction accuracy while the
        balance objective aims to learn a balanced optimal decision
        tree to better generalize to our of sample data.
    depth : int, default=1
        A parameter specifying the depth of the tree to learn.
    time_limit : int, default=60
        The given time limit for solving the MIP in seconds.
    num_threads: int, default=None
        The number of threads the solver should use. If not specified,
        solver uses all available threads
    verbose : bool, default = False
        Flag for logging solver outputs.
    """

    def __init__(
        self,
        solver,
        _lambda=0,
        obj_mode="acc",
        depth=1,
        time_limit=60,
        num_threads=None,
        verbose=False,
    ) -> None:
        self._obj_mode = obj_mode
        super().__init__(
            solver,
            _lambda,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

    def _define_objective(self):
        obj = self._solver.lin_expr(0)
        # obj = LinExpr(0)
        for n in self._tree.Nodes:
            for f in self._X_col_labels:
                # obj.add(-1 * self._lambda * self._b[n, f])
                obj += -1 * self._lambda * self._b[n, f]
        assert self._obj_mode in [
            "acc",
            "balance",
        ], "Wrong objective mode. obj_mode should be one of acc or balance."
        if self._obj_mode == "acc":
            for i in self._datapoints:
                obj += (1 - self._lambda) * self._z[i, 1]

        else:
            for i in self._datapoints:
                obj += (
                    (1 - self._lambda)
                    * (
                        1
                        / self._y[self._y == self._y[i]].shape[0]
                        / self._labels.shape[0]
                    )
                    * self._z[i, 1]
                )
        self._solver.set_objective(obj, ODTL.MAXIMIZE)

    def fit(self, X, y):
        # extract column labels, unique classes and store X as a DataFrame
        self._extract_metadata(X, y)

        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)
        # this function returns converted X and y but we retain metadata
        X, y = check_X_y(X, y)

        # Store the classes seen during fit
        self._classes = unique_labels(y)

        self._create_main_problem()
        self._solver.optimize(
            self._X, self, self._solver, callback=False, callback_action=None
        )
        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

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


class BendersOCT(FlowOCTSingleSink):
    def __init__(
        self,
        solver,
        _lambda=0,
        obj_mode="acc",
        depth=1,
        time_limit=60,
        num_threads=None,
        verbose=False,
    ) -> None:
        """
        Parameters
        ----------
        solver: str
            A string specifying the name of the solver to use
            to solve the MIP. Options are "Gurobi" and "CBC".
            If the CBC binaries are not found, Gurobi will be used by default.
        _lambda: float, default = 0
            The regularization parameter in the objective,
            taking values between 0 and 1, that controls
            the complexity of a the learned tree.
        obj_mode: str, default="acc"
            The objective should be used to learn an optimal decision tree.
            The two options are "acc" and "balance".
            The accuracy objective attempts to maximize prediction accuracy while the
            balance objective aims to learn a balanced optimal decision
            tree to better generalize to our of sample data.
        depth : int, default=1
            A parameter specifying the depth of the tree to learn.
        time_limit : int, default=60
            The given time limit for solving the MIP in seconds.
        num_threads: int, default=None
            The number of threads the solver should use. If not specified,
            solver uses all available threads
        verbose : bool, default = False
            Flag for logging solver outputs.
        """

        super().__init__(
            solver,
            _lambda,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

        self._lambda = _lambda
        self._obj_mode = obj_mode

    def _define_variables(self):
        self._tree_struc_variables()

        # g[i] is the objective value for the sub-problem[i]
        self._g = self._solver.add_vars(
            self._datapoints, vtype=ODTL.CONTINUOUS, ub=1, name="g"
        )

    def _define_constraints(self):
        self._tree_structure_constraints()

    def _define_objective(self):
        obj = self._solver.lin_expr(0)
        for n in self._tree.Nodes:
            for f in self._X_col_labels:
                obj += -1 * self._lambda * self._b[n, f]
        assert self._obj_mode in [
            "acc",
            "balance",
        ], "Wrong objective mode. obj_mode should be one of acc or balance."
        if self._obj_mode == "acc":
            for i in self._datapoints:
                obj += (1 - self._lambda) * self._g[i]
        else:
            for i in self._datapoints:
                obj += (
                    (1 - self._lambda)
                    * (
                        1
                        / self._y[self._y == self._y[i]].shape[0]
                        / self._labels.shape[0]
                    )
                    * self._g[i]
                )

        self._solver.set_objective(obj, ODTL.MAXIMIZE)

    def fit(self, X, y):

        # extract column labels, unique classes and store X as a DataFrame
        self._extract_metadata(X, y)

        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)
        # this function returns converted X and y but we retain metadata
        X, y = check_X_y(X, y)

        # Store the classes seen during fit
        self._classes = unique_labels(y)

        self._create_main_problem()

        # we need these in the callback to have access to the value of the decision variables in the callback
        self._solver.store_data("g", self._g)
        self._solver.store_data("b", self._b)
        self._solver.store_data("p", self._p)
        self._solver.store_data("w", self._w)
        # We also pass the following information to the model as we need them in the callback
        # self._solver.model._self_obj = self
        self._solver.store_data("self", self)

        callback_action = BendersCallback

        self._solver.optimize(
            self._X,
            self,
            self._solver,
            callback=True,
            callback_action=callback_action,
            g=self._g,
            b=self._b,
            p=self._p,
            w=self._w,
        )

        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

        return self

    def predict(self, X):
        """Classify test points using the Benders' Formulation Classifier

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
