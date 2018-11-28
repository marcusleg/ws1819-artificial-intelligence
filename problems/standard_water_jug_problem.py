"""
Formalization of the Water Jug Problem as described here:
https://en.wikipedia.org/wiki/Water_pouring_puzzle#Standard_example
"""

from problems.abstract_problem import AbstractProblemState


class StandardWaterJugProblemState(AbstractProblemState):

    def __init__(self, gallons_big_jug: int, gallons_medium_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.medium_jug = gallons_medium_jug
        self.small_jug = gallons_small_jug

    def __eq__(self, other):
        return self.big_jug == other.big_jug and self.medium_jug == other.medium_jug and self.small_jug == other.small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.medium_jug) + ", " + str(self.small_jug) + ")"

    @staticmethod
    def create_initial_state() -> 'StandardWaterJugProblemState':
        return StandardWaterJugProblemState(8, 0, 0)

    def get_actions(self):
        return [
            self.big_to_medium,
            self.big_to_small,
            self.medium_to_big,
            self.medium_to_small,
            self.small_to_big,
            self.small_to_medium,
        ]

    def big_to_medium(self) -> 'StandardWaterJugProblemState':
        big = max(0, self.big_jug + self.medium_jug - 5)
        medium = min(5, self.big_jug + self.medium_jug)
        small = self.small_jug
        return StandardWaterJugProblemState(big, medium, small)

    def big_to_small(self) -> 'StandardWaterJugProblemState':
        big = max(0, self.big_jug - (3 - self.small_jug))
        medium = self.medium_jug
        small = min(3, self.big_jug + self.small_jug)
        return StandardWaterJugProblemState(big, medium, small)

    def medium_to_big(self) -> 'StandardWaterJugProblemState':
        big = min(8, self.big_jug + self.medium_jug)
        medium = max(0, self.big_jug + self.medium_jug - 8)
        small = self.small_jug
        return StandardWaterJugProblemState(big, medium, small)

    def medium_to_small(self) -> 'StandardWaterJugProblemState':
        big = self.big_jug
        medium = max(0, self.medium_jug + self.small_jug - 3)
        small = min(3, self.medium_jug + self.small_jug)
        return StandardWaterJugProblemState(big, medium, small)

    def small_to_medium(self) -> 'StandardWaterJugProblemState':
        big = self.big_jug
        medium = min(5, self.medium_jug + self.small_jug)
        small = max(0, self.medium_jug + self.small_jug - 5)
        return StandardWaterJugProblemState(big, medium, small)

    def small_to_big(self) -> 'StandardWaterJugProblemState':
        big = min(8, self.big_jug + self.small_jug)
        medium = self.medium_jug
        small = max(0, self.big_jug + self.small_jug - 8)
        return StandardWaterJugProblemState(big, medium, small)

    def is_goal_state(self) -> bool:
        return self.big_jug == 4 and self.medium_jug == 4 and self.small_jug == 0
