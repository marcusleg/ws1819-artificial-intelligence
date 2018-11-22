from abc import ABC, abstractmethod

from problems.abstract_problem import AbstractProblem


class AbstractStrategy(ABC):

    def __init__(self, problem: AbstractProblem):
        self.problem = problem

    @abstractmethod
    def find_solution(self):
        pass

    @abstractmethod
    def print_solution(self):
        print("Initial State:", self.problem.create_initial_state())

    def print_resource_usage_report(self):
        pass
