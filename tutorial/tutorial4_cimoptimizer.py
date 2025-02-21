import kaiwu as kw
import numpy as np


def solve_tsp():
    """
    新手教程2 - 旅行商问题示例
    """
    # Import distance matrix
    w = np.array([[0, 0, 1, 1, 0],
                  [0, 0, 1, 0, 1],
                  [1, 1, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [0, 1, 1, 1, 0]])

    # Get the number of nodes
    n = w.shape[0]

    # Create qubo variable matrix
    x = kw.qubo.ndarray((n, n), "x", kw.qubo.Binary)

    # Get sets of edge and non-edge pairs
    edges = [(u, v) for u in range(n) for v in range(n) if w[u, v] != 0]
    no_edges = [(u, v) for u in range(n) for v in range(n) if w[u, v] == 0]

    def is_edge_used(x, u, v):
        return kw.qubo.quicksum([x[u, j] * x[v, j + 1] for j in range(-1, n - 1)])

    qubo_model = kw.qubo.QuboModel()
    # TSP path cost
    qubo_model.set_objective(kw.qubo.quicksum([w[u, v] * is_edge_used(x, u, v) for u, v in edges]))

    # Node constraint: Each node must belong to exactly one position
    qubo_model.add_constraint(x.sum(axis=0) == 1, "sequence_cons", penalty=5)

    # Position constraint: Each position can have only one node
    qubo_model.add_constraint(x.sum(axis=1) == 1, "node_cons", penalty=5)

    # Edge constraint: Pairs without edges cannot appear in the path
    qubo_model.add_constraint(kw.qubo.quicksum([is_edge_used(x, u, v) for u, v in no_edges]),
                              "connect_cons", penalty=5)

    # Perform calculation using SA optimizer
    kw.utils.set_log_level("INFO")
    kw.utils.CheckpointManager.save_dir = '/tmp'
    optimizer = kw.cim.CIMOptimizer(user_id="79048663116022001", sdk_code="z0rr6SgvotjDaAk2bCjlKSMVU7qeCv",
                                    task_name="tsp6")

    solver = kw.solver.SimpleSolver(optimizer)

    sol_dict, qubo_val = solver.solve_qubo(qubo_model)
    if sol_dict is None:
        return
    # Check the hard constraints for validity and path length
    unsatisfied_count, res_dict = qubo_model.verify_constraint(sol_dict)
    print("unsatisfied constraint: ", unsatisfied_count)
    print("value of constraint term", res_dict)

    # Calculate the path length using path_cost
    path_val = kw.qubo.get_val(qubo_model.objective, sol_dict)
    print('path_cost: {}'.format(path_val))


if __name__ == "__main__":
    solve_tsp()
