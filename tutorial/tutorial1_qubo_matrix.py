import numpy as np
import kaiwu as kw
import pandas as pd

# Define the input adjacency matrix for the graph
adj_matrix = np.array([
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0]])

# Get the number of nodes in the graph
num_nodes = len(adj_matrix)

# Create a QUBO variable array 'x' with 'num_nodes' variables
# each representing a node in the graph
x = kw.qubo.ndarray(num_nodes, 'x', kw.qubo.Binary)

# Define the objective function for the QUBO model of Max cut problem
obj = -x.T @ adj_matrix @ (1 - x)

# parse QUBO
obj = kw.qubo.make(obj)

# Extract the QUBO matrix and store it in a pandas DataFrame
qubo_matrix = kw.qubo.qubo_model_to_qubo_matrix(obj)['qubo_matrix']

# Check whether the QUBO matrix satisfy the precision requirement
kw.qubo.check_qubo_matrix_bit_width(qubo_matrix)

# Save the QUBO matrix to a CSV file without including index or header
df = pd.DataFrame(qubo_matrix)
csv_file_path = 'qubo_matrix.csv'
df.to_csv(csv_file_path, index=False, header=False)
