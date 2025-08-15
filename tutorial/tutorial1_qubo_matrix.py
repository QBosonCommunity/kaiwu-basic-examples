# Import numpy and kaiwu
import numpy as np
import pandas as pd
import kaiwu as kw
kw.common.CheckpointManager.save_dir = "/tmp"
kw.license.init(user_id="xxxxxxx", sdk_code="xxxxxxx")


# Import distance matrix
w = np.array([[ 0, 13, 11, 16,  8],
              [13,  0,  7, 14,  9],
              [11,  7,  0, 10,  9],
              [16, 14, 10,  0, 12],
              [ 8,  9,  9, 12,  0]])

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
qubo_model.add_constraint(x.sum(axis=0) == 1, "sequence_cons", penalty=20.0)

# Position constraint: Each position can have only one node
qubo_model.add_constraint(x.sum(axis=1) == 1, "node_cons", penalty=20.0)

# Edge constraint: Pairs without edges cannot appear in the path
qubo_model.add_constraint(kw.qubo.quicksum([is_edge_used(x, u, v) for u, v in no_edges]),
    "connect_cons", penalty=20.0)
# Perform calculation using SA optimizer
# optimizer = kw.cim.PrecisionReducer(optimizer, 8)  # 8位精度
solver = kw.solver.SimpleSolver(kw.classical.SimulatedAnnealingOptimizer(initial_temperature=100,
                                                                         alpha=0.99,
                                                                         cutoff_temperature=0.001,
                                                                         iterations_per_t=10,
                                                                         size_limit=100))

sol_dict, qubo_val = solver.solve_qubo(qubo_model)    
print(sol_dict)
print(qubo_val)
