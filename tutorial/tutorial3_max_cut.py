import kaiwu as kw
import numpy as np


def solve_max_cut():
    # invert input graph matrix
    matrix = -np.array([
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

    worker = kw.classical.SimulatedAnnealingOptimizer(initial_temperature=100,
                                                      alpha=0.99,
                                                      cutoff_temperature=0.001,
                                                      iterations_per_t=10,
                                                      size_limit=100)
    output = worker.solve(matrix)
    print(output)
    opt = kw.sampler.optimal_sampler(matrix, output, 0)
    best = opt[0][0]
    max_cut = (np.sum(-matrix) - np.dot(-matrix, best).dot(best)) / 4
    print("The obtained max cut is " + str(max_cut) + ".")


if __name__ == "__main__":
    solve_max_cut()
