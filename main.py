#!/bin/python3

from problems.water_jug_problem import WaterJugProblem
from strategies.breadth_first_search import BreadthFirstSearch

problem = WaterJugProblem
strategy = BreadthFirstSearch(problem)

strategy.find_solution()
strategy.print_solution()
