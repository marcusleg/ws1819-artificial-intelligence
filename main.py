#!/bin/python3

from problems.simplified_water_jug_problem import SimplifiedWaterJugProblem
from problems.standard_water_jug_problem import StandardWaterJugProblem
from strategies.breadth_first_search import BreadthFirstSearch

problems = [
    SimplifiedWaterJugProblem,
    StandardWaterJugProblem,
]

for problem in problems:
    problem = problem
    print("Trying to find a solution for", problem.__name__)
    strategy = BreadthFirstSearch(problem)
    strategy.find_solution()
    strategy.print_solution()
    print("\n")
