#!/bin/python3

from mpi4py import MPI
from problems.standard_water_jug_problem import StandardWaterJugProblemState
from strategies.iterative_depth_first_search import IterativeDepthFirstSearch

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()


problem = StandardWaterJugProblemState
strategy = IterativeDepthFirstSearch(problem)

# coordination
solution_found = False
if rank == 0:
    batch = 0

while not solution_found:
    # distribute tasks
    if rank == 0:
        num_worker_nodes = size - 1
        n = [batch * num_worker_nodes + i for i in range(size)]
    else:
        n = None
    n = MPI.COMM_WORLD.scatter(n, root=0)

    # compute results
    if rank == 0:
        data = None
    else:
        if strategy.iddfs(n):
            # solution found
            data = (True, n, strategy.get_solution())
        else:
            # no solution found
            data = (False, n, None)

    # collect results
    data = MPI.COMM_WORLD.gather(data, root=0)
    if rank == 0:
        for i in range(1, size):
            if data[i][0]:
                print("Node", i, "found a solution for depth_limit =",
                      data[i][1], "=>", data[i][2])
                solution_found = True
            else:
                print(
                    "Node", i, "did not find a solution for depth_limit =", data[i][1])

    # coordination
    if rank == 0:
        batch += 1
    solution_found = MPI.COMM_WORLD.bcast(solution_found, root=0)
