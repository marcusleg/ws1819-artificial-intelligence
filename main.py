#!/bin/python3
from sys import argv

from problems.simplified_water_jug_problem import SimplifiedWaterJugProblemState
from problems.standard_water_jug_problem import StandardWaterJugProblemState
from problems.eight_puzzle_problem import EightPuzzleProblemState
from strategies.a_star_search import AStarStrategy
from strategies.breadth_first_search import BreadthFirstSearch
from strategies.iterative_depth_first_search import IterativeDepthFirstSearch

problems = [
    SimplifiedWaterJugProblemState,
    StandardWaterJugProblemState,
    EightPuzzleProblemState,
]

strategies = [
    AStarStrategy,
    BreadthFirstSearch,
    IterativeDepthFirstSearch,
]

if len(argv) == 3:
    # select problem and strategy according to provided cli arguments
    problem = problems[int(argv[1])]
    strategy = strategies[int(argv[2])]
else:
    # let user choose problem and strategy at runtime
    problem_index = -1
    while problem_index < 0 or problem_index >= len(problems):
        print("Problems:")
        for index, problem in enumerate(problems):
            print("  ({}) {}".format(index, problem.__name__))
        problem_index = int(input("Select a problem: "))
    problem = problems[problem_index]

    strategy_index = -1
    while strategy_index < 0 or strategy_index >= len(strategies):
        print("Strategies:")
        for index, strategy in enumerate(strategies):
            print("  ({}) {}".format(index, strategy.__name__))
        strategy_index = int(input("Select a strategy: "))
    strategy = strategies[strategy_index]

    print("You can also start this problem/strategy combination with",
          argv[0], problem_index, strategy_index, "\n")

# try to find a solution and print it
strategy_instance = strategy(problem)
print("Trying to find a solution for", problem.__name__,
      "with", strategy_instance.__class__.__name__)
strategy_instance.find_solution()
strategy_instance.print_solution()
strategy_instance.print_resource_usage_report()
print("\n")
