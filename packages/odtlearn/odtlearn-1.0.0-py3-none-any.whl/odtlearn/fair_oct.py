from itertools import combinations

import numpy as np
import pandas as pd
from sklearn.utils.multiclass import unique_labels
from sklearn.utils.validation import check_array, check_is_fitted, check_X_y

from odtlearn import ODTL
from odtlearn.flow_oct_ms import FlowOCTMultipleSink
from odtlearn.utils.validation import check_binary, check_columns_match


class FairOCT(FlowOCTMultipleSink):
    def __init__(
        self,
        solver,
        positive_class,
        _lambda=0,
        depth=1,
        obj_mode="acc",
        fairness_type=None,
        fairness_bound=1,
        time_limit=60,
        num_threads=None,
        verbose=False,
    ) -> None:
        """
        An optimal and fair classification tree fitted on a given binary-valued
        data set. The fairness criteria enforced in the training step is one of statistical parity (SP),
        conditional statistical parity (CSP), predictive equality (PE),
        equal opportunity (EOpp) or equalized odds (EOdds).

        Parameters
        ----------
        solver: str
            A string specifying the name of the solver to use
            to solve the MIP. Options are "Gurobi" and "CBC".
            If the CBC binaries are not found, Gurobi will be used by default.
        positive_class : int
            The value of the class label which is corresponding to the desired outcome
        depth : int, default= 1
            A parameter specifying the depth of the tree
        time_limit : int, default= 60
            The given time limit (in seconds) for solving the MIO problem
        _lambda : float, default= 0
            The regularization parameter in the objective. _lambda is in the interval [0,1)
        num_threads: int, default=None
            The number of threads the solver should use. If None, it will use all avaiable threads
        fairness_type: [None, 'SP', 'CSP', 'PE', 'EOpp', 'EOdds'], default=None
            The type of fairness criteria that we want to enforce
        fairness_bound: float (0,1], default=1
            The bound of the fairness constraint. The smaller the value the stricter
            the fairness constraint and 1 corresponds to no fairness at all
        :param X: numpy matrix or pandas data-frame of covariates.
                  It's up to the user to include the protected features in X or not.
                  We assume that we are allowed to branch on any of the columns within X.
        """
        super().__init__(
            solver,
            _lambda,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

        self._obj_mode = obj_mode
        self._fairness_type = fairness_type
        self._fairness_bound = fairness_bound
        self._positive_class = positive_class

    def _extract_metadata(self, X, y, protect_feat):
        super(FlowOCTMultipleSink, self)._extract_metadata(X, y)
        if isinstance(protect_feat, pd.DataFrame):
            self._protect_feat_col_labels = protect_feat.columns
            self._protect_feat_col_dtypes = protect_feat.dtypes
        else:
            self._protect_feat_col_labels = np.array(
                [f"P_{i}" for i in np.arange(0, protect_feat.shape[1])]
            )

    def _add_fairness_constraint(self, p_df, p_prime_df):
        count_p = p_df.shape[0]
        count_p_prime = p_prime_df.shape[0]
        constraint_added = False
        if count_p != 0 and count_p_prime != 0:
            constraint_added = True
            self._solver.add_constr(
                (
                    (1 / count_p)
                    * self._solver.quicksum(
                        self._solver.quicksum(
                            self._zeta[i, n, self._positive_class]
                            for n in self._tree.Leaves + self._tree.Nodes
                        )
                        for i in p_df.index
                    )
                    - (
                        (1 / count_p_prime)
                        * self._solver.quicksum(
                            self._solver.quicksum(
                                self._zeta[i, n, self._positive_class]
                                for n in self._tree.Leaves + self._tree.Nodes
                            )
                            for i in p_prime_df.index
                        )
                    )
                )
                <= self._fairness_bound
            )

            self._solver.add_constr(
                (
                    (1 / count_p)
                    * self._solver.quicksum(
                        self._solver.quicksum(
                            self._zeta[i, n, self._positive_class]
                            for n in (self._tree.Leaves + self._tree.Nodes)
                        )
                        for i in p_df.index
                    )
                )
                - (
                    (1 / count_p_prime)
                    * self._solver.quicksum(
                        self._solver.quicksum(
                            self._zeta[i, n, self._positive_class]
                            for n in self._tree.Leaves + self._tree.Nodes
                        )
                        for i in p_prime_df.index
                    )
                )
                >= -1 * self._fairness_bound
            )

        return constraint_added

    def _define_constraints(self):
        super()._define_constraints()
        # Loop through all possible combinations of the protected feature
        for protected_feature in self._P_col_labels:
            for combo in combinations(self._X_p[protected_feature].unique(), 2):
                p = combo[0]
                p_prime = combo[1]

                if self._fairness_type == "SP":
                    p_df = self._X_p[self._X_p[protected_feature] == p]
                    p_prime_df = self._X_p[self._X_p[protected_feature] == p_prime]
                    self._add_fairness_constraint(p_df, p_prime_df)
                elif self._fairness_type == "PE":
                    p_df = self._X_p[
                        (self._X_p[protected_feature] == p)
                        & (self._X_p[self._class_name] != self._positive_class)
                    ]
                    p_prime_df = self._X_p[
                        (self._X_p[protected_feature] == p_prime)
                        & (self._X_p[self._class_name] != self._positive_class)
                    ]
                    self._add_fairness_constraint(p_df, p_prime_df)
                elif self._fairness_type == "EOpp":
                    p_df = self._X_p[
                        (self._X_p[protected_feature] == p)
                        & (self._X_p[self._class_name] == self._positive_class)
                    ]
                    p_prime_df = self._X_p[
                        (self._X_p[protected_feature] == p_prime)
                        & (self._X_p[self._class_name] == self._positive_class)
                    ]
                    self._add_fairness_constraint(p_df, p_prime_df)
                elif (
                    self._fairness_type == "EOdds"
                ):  # Need to check with group if this is how we want to enforce this constraint
                    PE_p_df = self._X_p[
                        (self._X_p[protected_feature] == p)
                        & (self._X_p[self._class_name] != self._positive_class)
                    ]
                    PE_p_prime_df = self._X_p[
                        (self._X_p[protected_feature] == p_prime)
                        & (self._X_p[self._class_name] != self._positive_class)
                    ]

                    EOpp_p_df = self._X_p[
                        (self._X_p[protected_feature] == p)
                        & (self._X_p[self._class_name] == self._positive_class)
                    ]
                    EOpp_p_prime_df = self._X_p[
                        (self._X_p[protected_feature] == p_prime)
                        & (self._X_p[self._class_name] == self._positive_class)
                    ]

                    if (
                        PE_p_df.shape[0] != 0
                        and PE_p_prime_df.shape[0] != 0
                        and EOpp_p_df.shape[0] != 0
                        and EOpp_p_prime_df.shape[0] != 0
                    ):
                        self._add_fairness_constraint(PE_p_df, PE_p_prime_df)
                        self._add_fairness_constraint(EOpp_p_df, EOpp_p_prime_df)
                elif self._fairness_type == "CSP":
                    for l_value in self._X_p[self._legitimate_name].unique():
                        p_df = self._X_p[
                            (self._X_p[protected_feature] == p)
                            & (self._X_p[self._legitimate_name] == l_value)
                        ]
                        p_prime_df = self._X_p[
                            (self._X_p[protected_feature] == p_prime)
                            & (self._X_p[self._legitimate_name] == l_value)
                        ]
                        self._add_fairness_constraint(p_df, p_prime_df)

    def _define_objective(self):
        # Max sum(sum(zeta[i,n,y(i)]))
        obj = self._solver.lin_expr(0)
        for n in self._tree.Nodes:
            for f in self._X_col_labels:
                obj += -1 * self._lambda * self._b[n, f]
        if self._obj_mode == "acc":
            for i in self._datapoints:
                for n in self._tree.Nodes + self._tree.Leaves:
                    obj += (1 - self._lambda) * (self._zeta[i, n, self._y[i]])
        elif self._obj_mode == "balance":
            for i in self._datapoints:
                for n in self._tree.Nodes + self._tree.Leaves:
                    obj += (
                        (1 - self._lambda)
                        * (
                            1
                            / self._y[self._y == self._y[i]].shape[0]
                            / self._labels.shape[0]
                        )
                        * (self._zeta[i, n, self._y[i]])
                    )
        else:
            raise ValueError(
                "Invalid objective mode. obj_mode should be one of acc or balance."
            )

        self._solver.set_objective(obj, ODTL.MAXIMIZE)

    def fit(self, X, y, protect_feat, legit_factor):
        """
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples, n_features)
            The training input samples.
        y : array-like, shape (n_samples,)
            The target values (class labels in classification).
        protect_feat : array-like, shape (n_samples,1) or (n_samples, n_p)
            The protected feature columns (Race, gender, etc); Can have one or more columns
        legit_factor : array-like, shape (n_samples,)
            The legitimate factor column(e.g., prior number of criminal acts)

        Returns
        -------
        self : object
            Returns self.
        """
        self._extract_metadata(X, y, protect_feat)

        self._protect_feat = protect_feat
        self._legit_factor = legit_factor

        self._class_name = "class_label"
        self._legitimate_name = "legitimate_feature_name"

        # this function returns converted X and y but we retain metadata
        if isinstance(y, (pd.Series, pd.DataFrame)):
            X, y = check_X_y(X, y.values.ravel())
        else:
            X, y = check_X_y(X, y)
        # Raises ValueError if there is a column that has values other than 0 or 1
        check_binary(X)

        self._X_p = np.concatenate(
            (protect_feat, legit_factor.reshape(-1, 1), y.reshape(-1, 1)), axis=1
        )
        self._X_p = pd.DataFrame(
            self._X_p,
            columns=(
                self._protect_feat_col_labels.tolist()
                + [self._legitimate_name, self._class_name]
            ),
        )

        self._P_col_labels = self._protect_feat_col_labels

        # Store the classes seen during fit
        self._classes = unique_labels(y)

        self._create_main_problem()
        self._solver.optimize(self._X, self, self._solver)

        self.b_value = self._solver.get_var_value(self._b, "b")
        self.w_value = self._solver.get_var_value(self._w, "w")
        self.p_value = self._solver.get_var_value(self._p, "p")

        # Return the classifier
        return self

    def predict(self, X):
        """Classify test points using the FairTree classifier

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
        check_is_fitted(self, ["b_value", "w_value", "p_value"])

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        X = check_array(X)

        check_columns_match(self._X_col_labels, X)

        return self._make_prediction(X)

    def get_SP(self, protect_feat, y):
        """
        This function returns the statistical parity value for any given protected level and outcome value

        :param protect_feat: array-like, shape (n_samples,1) or (n_samples, n_p)
                The protected feature columns (Race, gender, etc); We could have one or more columns
        :param y: array-like, shape (n_samples,)
                The target values (class labels in classification).

        :return sp_dict: a dictionary with key =(p,t) and value = P(Y=t|P=p)
        where p is a protected level and t is an outcome value

        """
        if isinstance(protect_feat, pd.DataFrame):
            protect_feat_test_col_names = protect_feat.columns
        else:
            protect_feat_test_col_names = np.array(
                [f"P_{i}" for i in np.arange(0, protect_feat.shape[1])]
            )

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        protect_feat, y = check_X_y(protect_feat, y)

        check_columns_match(self._protect_feat_col_labels, protect_feat)

        class_name = "class_label"
        X_p = np.concatenate((protect_feat, y.reshape(-1, 1)), axis=1)
        X_p = pd.DataFrame(
            X_p,
            columns=(protect_feat_test_col_names.tolist() + [class_name]),
        )

        sp_dict = {}

        for t in X_p[class_name].unique():
            for protected_feature in protect_feat_test_col_names:
                for p in X_p[protected_feature].unique():
                    p_df = X_p[X_p[protected_feature] == p]
                    sp_p_t = None
                    if p_df.shape[0] != 0:
                        sp_p_t = p_df[p_df[class_name] == t].shape[0] / p_df.shape[0]
                    sp_dict[(p, t)] = sp_p_t

        return sp_dict

    def get_CSP(self, protect_feat, legit_factor, y):
        """
        This function returns the conditional statistical parity value for any given
        protected level, legitimate feature value and outcome value

        :param protect_feat: array-like, shape (n_samples,1) or (n_samples, n_p)
                The protected feature columns (Race, gender, etc); We could have one or more columns
        :param legit_fact: array-like, shape (n_samples,)
            The legitimate factor column(e.g., prior number of criminal acts)
        :param y: array-like, shape (n_samples,)
                The target values (class labels in classification).


        :return csp_dict: a dictionary with key =(p, f, t) and value = P(Y=t|P=p, L=f) where p is a protected level
                          and t is an outcome value and l is the value of the legitimate feature

        """

        if isinstance(protect_feat, pd.DataFrame):
            protect_feat_test_col_names = protect_feat.columns
        else:
            protect_feat_test_col_names = np.array(
                [f"P_{i}" for i in np.arange(0, protect_feat.shape[1])]
            )

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        _, y = check_X_y(protect_feat, y)
        protect_feat, legit_factor = check_X_y(protect_feat, legit_factor)

        check_columns_match(self._protect_feat_col_labels, protect_feat)

        class_name = "class_label"
        legitimate_name = "legitimate_feature_name"
        X_p = np.concatenate(
            (protect_feat, legit_factor.reshape(-1, 1), y.reshape(-1, 1)), axis=1
        )
        X_p = pd.DataFrame(
            X_p,
            columns=(
                protect_feat_test_col_names.tolist() + [legitimate_name, class_name]
            ),
        )

        csp_dict = {}

        for t in X_p[class_name].unique():
            for protected_feature in protect_feat_test_col_names:
                for p in X_p[protected_feature].unique():
                    for f in X_p[legitimate_name].unique():
                        p_f_df = X_p[
                            (X_p[protected_feature] == p) & (X_p[legitimate_name] == f)
                        ]
                        csp_p_f_t = None
                        if p_f_df.shape[0] != 0:
                            csp_p_f_t = (
                                p_f_df[p_f_df[class_name] == t].shape[0]
                            ) / p_f_df.shape[0]
                        csp_dict[(p, f, t)] = csp_p_f_t

        return csp_dict

    def get_EqOdds(self, protect_feat, y, y_pred):
        """
        This function returns the false positive and true positive rate value
        for any given protected level, outcome value and prediction value

        :param protect_feat: array-like, shape (n_samples,1) or (n_samples, n_p)
                The protected feature columns (Race, gender, etc); We could have one or more columns

        :param y: array-like, shape (n_samples,)
                The true target values (class labels in classification).
        :param y_pred: array-like, shape (n_samples,)
                The predicted values (class labels in classification).

        :return eq_dict: a dictionary with key =(p, t, t_pred) and value = P(Y_pred=t_pred|P=p, Y=t)

        """

        if isinstance(protect_feat, pd.DataFrame):
            protect_feat_test_col_names = protect_feat.columns
        else:
            protect_feat_test_col_names = np.array(
                [f"P_{i}" for i in np.arange(0, protect_feat.shape[1])]
            )

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        if isinstance(y, (pd.Series, pd.DataFrame)):
            _, y = check_X_y(protect_feat, y.values.ravel())
        else:
            _, y = check_X_y(protect_feat, y)
        protect_feat, y_pred = check_X_y(protect_feat, y_pred)

        check_columns_match(self._protect_feat_col_labels, protect_feat)

        class_name = "class_label"
        pred_name = "pred_label"
        X_p = np.concatenate(
            (protect_feat, y.reshape(-1, 1), y_pred.reshape(-1, 1)), axis=1
        )
        X_p = pd.DataFrame(
            X_p,
            columns=(protect_feat_test_col_names.tolist() + [class_name, pred_name]),
        )

        eq_dict = {}

        for t in X_p[class_name].unique():
            for t_pred in X_p[class_name].unique():
                for protected_feature in protect_feat_test_col_names:
                    for p in X_p[protected_feature].unique():
                        p_t_df = X_p[
                            (X_p[protected_feature] == p) & (X_p[class_name] == t)
                        ]
                        eq_p_t_t_pred = None
                        if p_t_df.shape[0] != 0:
                            eq_p_t_t_pred = (
                                p_t_df[p_t_df[pred_name] == t_pred].shape[0]
                            ) / p_t_df.shape[0]
                        eq_dict[(p, t, t_pred)] = eq_p_t_t_pred

        return eq_dict

    def get_CondEqOdds(self, protect_feat, legit_factor, y, y_pred):
        """
        This function returns the conditional false negative and true positive rate value
        for any given protected level, outcome value, prediction value and legitimate feature value

        :param protect_feat: array-like, shape (n_samples,1) or (n_samples, n_p)
                The protected feature columns (Race, gender, etc); We could have one or more columns
        :param legit_factor: array-like, shape (n_samples,)
            The legitimate factor column(e.g., prior number of criminal acts)

        :param y: array-like, shape (n_samples,)
                The true target values (class labels in classification).
        :param y_pred: array-like, shape (n_samples,)
                The predicted values (class labels in classification).

        :return ceq_dict: a dictionary with key =(p, f, t, t_pred) and value = P(Y_pred=t_pred|P=p, Y=t, L=f)

        """

        if isinstance(protect_feat, pd.DataFrame):
            protect_feat_test_col_names = protect_feat.columns
        else:
            protect_feat_test_col_names = np.array(
                [f"P_{i}" for i in np.arange(0, protect_feat.shape[1])]
            )

        # This will again convert a pandas df to numpy array
        # but we have the column information from when we called fit
        if isinstance(y, (pd.Series, pd.DataFrame)):
            _, y = check_X_y(protect_feat, y.values.ravel())
        else:
            _, y = check_X_y(protect_feat, y)
        _, y_pred = check_X_y(protect_feat, y_pred)
        protect_feat, legit_factor = check_X_y(protect_feat, legit_factor)

        check_columns_match(self._protect_feat_col_labels, protect_feat)

        class_name = "class_label"
        pred_name = "pred_label"
        legitimate_name = "legitimate_feature_name"
        X_p = np.concatenate(
            (
                protect_feat,
                legit_factor.reshape(-1, 1),
                y.reshape(-1, 1),
                y_pred.reshape(-1, 1),
            ),
            axis=1,
        )
        X_p = pd.DataFrame(
            X_p,
            columns=(
                protect_feat_test_col_names.tolist()
                + [legitimate_name, class_name, pred_name]
            ),
        )

        ceq_dict = {}

        for t in X_p[class_name].unique():
            for t_pred in X_p[class_name].unique():
                for protected_feature in protect_feat_test_col_names:
                    for p in X_p[protected_feature].unique():
                        for f in X_p[legitimate_name].unique():
                            p_f_t_df = X_p[
                                (X_p[protected_feature] == p)
                                & (X_p[legitimate_name] == f)
                                & (X_p[class_name] == t)
                            ]
                            ceq_p_f_t_t_pred = None
                            if p_f_t_df.shape[0] != 0:
                                ceq_p_f_t_t_pred = (
                                    p_f_t_df[p_f_t_df[pred_name] == t_pred].shape[0]
                                ) / p_f_t_df.shape[0]
                            ceq_dict[(p, f, t, t_pred)] = ceq_p_f_t_t_pred

        return ceq_dict

    def fairness_metric_summary(self, metric, new_data=None):
        check_is_fitted(self, ["b_value", "w_value", "p_value"])
        metric_names = ["SP", "CSP", "PE", "CPE"]
        if new_data is None:
            new_data = self.predict(self._X)
        if metric not in metric_names:
            raise ValueError(
                f"metric argument: '{metric}' does not match any of the options: {metric_names}"
            )
        if metric == "SP":
            sp_df = pd.DataFrame(
                self.get_SP(self._protect_feat, new_data).items(),
                columns=["(p,y)", "P(Y=y|P=p)"],
            )
            print(sp_df)
        elif metric == "CSP":
            csp_df = pd.DataFrame(
                self.get_CSP(self._protect_feat, self._legit_factor, new_data).items(),
                columns=["(p, f, y)", "P(Y=y|P=p, L=f)"],
            )
            print(csp_df)
        elif metric == "PE":
            pe_df = pd.DataFrame(
                self.get_EqOdds(self._protect_feat, self._y, new_data).items(),
                columns=["(p, y, y_pred)", "P(Y_pred=y_pred|P=p, Y=y)"],
            )
            print(pe_df)
        elif metric == "CPE":
            cpe_df = pd.DataFrame(
                self.get_CondEqOdds(
                    self._protect_feat, self._legit_factor, self._y, new_data
                ).items(),
                columns=["(p, f, t, t_pred)", "P(Y_pred=y_pred|P=p, Y=y, L=f)"],
            )
            print(cpe_df)
