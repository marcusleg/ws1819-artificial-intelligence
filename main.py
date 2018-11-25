#!/bin/python3

from problems.simplified_water_jug_problem import SimplifiedWaterJugProblemState
from problems.standard_water_jug_problem import StandardWaterJugProblemState
from strategies.breadth_first_search import BreadthFirstSearch
from strategies.iterative_depth_first_search import IterativeDepthFirstSearch

problems = [
    SimplifiedWaterJugProblemState,
    StandardWaterJugProblemState,
]

strategies = [
    BreadthFirstSearch,
    IterativeDepthFirstSearch,
]

for problem in problems:
    for strategy in strategies:
        strategy_instance = strategy(problem)
        print("Trying to find a solution for", problem.__name__,
              "with", strategy_instance.__class__.__name__)
        strategy_instance.find_solution()
        strategy_instance.print_solution()
        strategy_instance.print_resource_usage_report()
        print("\n")
