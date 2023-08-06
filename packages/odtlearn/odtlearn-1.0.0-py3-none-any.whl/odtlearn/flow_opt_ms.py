from odtlearn import ODTL
from odtlearn.opt_pt import OptimalPrescriptiveTree


class FlowOPTMultipleSink(OptimalPrescriptiveTree):
    def __init__(
        self,
        solver,
        depth,
        time_limit,
        num_threads,
        verbose,
    ) -> None:

        super().__init__(
            solver,
            depth,
            time_limit,
            num_threads,
            verbose,
        )

    def _tree_struc_variables(self):
        self._b = self._solver.add_vars(
            self._tree.Nodes, self._X_col_labels, vtype=ODTL.BINARY, name="b"
        )
        self._p = self._solver.add_vars(
            self._tree.Nodes + self._tree.Leaves, vtype=ODTL.BINARY, name="p"
        )
        self._w = self._solver.add_vars(
            self._tree.Nodes + self._tree.Leaves,
            self._treatments,
            vtype=ODTL.CONTINUOUS,
            lb=0,
            name="w",
        )

    def _flow_variables(self):
        self._zeta = self._solver.add_vars(
            self._datapoints,
            self._tree.Nodes + self._tree.Leaves,
            self._treatments,
            vtype=ODTL.CONTINUOUS,
            lb=0,
            name="zeta",
        )
        self._z = self._solver.add_vars(
            self._datapoints,
            self._tree.Nodes + self._tree.Leaves,
            vtype=ODTL.CONTINUOUS,
            lb=0,
            name="z",
        )

    def _define_variables(self):
        self._tree_struc_variables()
        self._flow_variables()

    def _tree_structure_constraints(self):
        # sum(b[n,f], f) + p[n] + sum(p[m], m in A(n)) = 1   forall n in Nodes
        self._solver.add_constrs(
            (
                self._solver.quicksum(self._b[n, f] for f in self._X_col_labels)
                + self._p[n]
                + self._solver.quicksum(self._p[m] for m in self._tree.get_ancestors(n))
                == 1
            )
            for n in self._tree.Nodes
        )

        # p[n] + sum(p[m], m in A(n)) = 1   forall n in Leaves
        self._solver.add_constrs(
            (
                self._p[n]
                + self._solver.quicksum(self._p[m] for m in self._tree.get_ancestors(n))
                == 1
            )
            for n in self._tree.Leaves
        )

        # sum(w[n,k], k in treatments) = p[n]
        self._solver.add_constrs(
            (
                self._solver.quicksum(self._w[n, k] for k in self._treatments)
                == self._p[n]
            )
            for n in self._tree.Nodes + self._tree.Leaves
        )

    def _flow_constraints(self):
        # z[i,n] = z[i,l(n)] + z[i,r(n)] + zeta[i,n]    forall i, n in Nodes
        for n in self._tree.Nodes:
            n_left = int(self._tree.get_left_children(n))
            n_right = int(self._tree.get_right_children(n))
            self._solver.add_constrs(
                (
                    self._z[i, n]
                    == self._z[i, n_left]
                    + self._z[i, n_right]
                    + self._solver.quicksum(
                        self._zeta[i, n, k] for k in self._treatments
                    )
                )
                for i in self._datapoints
            )

        for n in self._tree.Leaves:
            self._solver.add_constrs(
                self._solver.quicksum(self._zeta[i, n, k] for k in self._treatments)
                == self._z[i, n]
                for i in self._datapoints
            )

    def _arc_constraints(self):
        # z[i,l(n)] <= sum(b[n,f], f if x[i,f]<=0)    forall i, n in Nodes
        for i in self._datapoints:
            self._solver.add_constrs(
                (
                    self._z[i, int(self._tree.get_left_children(n))]
                    <= self._solver.quicksum(
                        self._b[n, f]
                        for f in self._X_col_labels
                        if self._X.at[i, f] <= 0
                    )
                )
                for n in self._tree.Nodes
            )

        # z[i,r(n)] <= sum(b[n,f], f if x[i,f]=1)    forall i, n in Nodes
        for i in self._datapoints:
            self._solver.add_constrs(
                (
                    self._z[i, int(self._tree.get_right_children(n))]
                    <= self._solver.quicksum(
                        self._b[n, f]
                        for f in self._X_col_labels
                        if self._X.at[i, f] == 1
                    )
                )
                for n in self._tree.Nodes
            )

        # zeta[i,n] <= w[n,T[i]] for all n in N+L, i
        for n in self._tree.Nodes + self._tree.Leaves:
            for k in self._treatments:
                self._solver.add_constrs(
                    self._zeta[i, n, k] <= self._w[n, k] for i in self._datapoints
                )

        self._solver.add_constrs(self._z[i, 1] == 1 for i in self._datapoints)

    def _define_constraints(self):
        self._tree_structure_constraints()
        self._flow_constraints()
        self._arc_constraints()
