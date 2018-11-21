#!/bin/python3

from problems.simplified_water_jug_problem import SimplifiedWaterJugProblem
from problems.standard_water_jug_problem import StandardWaterJugProblem
from strategies.breadth_first_search import BreadthFirstSearch

problems = [
    SimplifiedWaterJugProblem,
    StandardWaterJugProblem,
]

strategies = [
    BreadthFirstSearch,
]

for problem in problems:
    for strategy in strategies:
        strategy_instance = BreadthFirstSearch(problem)
        print("Trying to find a solution for", problem.__name__,
              "with", strategy_instance.__class__.__name__)
        strategy_instance.find_solution()
        strategy_instance.print_solution()
        print("\n")
