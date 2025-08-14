# pylint: disable=<R0801>
"""
TSP问题调用真机求解
"""
import numpy as np
import pandas as pd
import kaiwu as kw


def is_edge_used(var_x, var_u, var_v):
    """
    Determine whether the edge (u, v) is used in the path.

    Args:
        var_x (ndarray): Decision variable matrix.

        var_u (int): Start node.

        var_v (int): End node.

    Returns:
        ndarray: Decision variable corresponding to the edge (u, v).
    """
    return kw.qubo.quicksum([var_x[var_u, j] * var_x[var_v, j + 1] for j in range(-1, n - 1)])


if __name__ == '__main__':
    # Import distance matrix
    w = np.array([[0, 1, 2],
                  [1, 0, 0],
                  [2, 0, 0]])
    # Get the number of nodes
    n = w.shape[0]

    # Create qubo variable matrix
    x = kw.qubo.ndarray((n, n), "x", kw.qubo.Binary)

    # Get sets of edge and non-edge pairs
    edges = [(u, v) for u in range(n) for v in range(n) if w[u, v] != 0]
    no_edges = [(u, v) for u in range(n) for v in range(n) if w[u, v] == 0]

    qubo_model = kw.qubo.QuboModel()
    # TSP path cost
    qubo_model.set_objective(kw.qubo.quicksum([w[u, v] * is_edge_used(x, u, v) for u, v in edges]))

    # Node constraint: Each node must belong to exactly one position
    qubo_model.add_constraint(x.sum(axis=0) == 1, "sequence_cons", penalty=5.0)

    # Position constraint: Each position can have only one node
    qubo_model.add_constraint(x.sum(axis=1) == 1, "node_cons", penalty=5.0)

    # Edge constraint: Pairs without edges cannot appear in the path
    qubo_model.add_constraint(kw.qubo.quicksum([is_edge_used(x, u, v) for u, v in no_edges]),
        "connect_cons", penalty=20.0)

    qubo_mat = qubo_model.get_matrix()
    pd.DataFrame(qubo_mat).to_csv("tsp.csv", index=False, header=False)