from typing import List

from problems.abstract_problem import AbstractProblemState


class SimplifiedWaterJugProblemState(AbstractProblemState):

    def __init__(self, gallons_big_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.small_jug = gallons_small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.small_jug) + ")"

    @staticmethod
    def create_initial_state() -> 'SimplifiedWaterJugProblemState':
        return SimplifiedWaterJugProblemState(0, 0)

    def get_actions(self):
        return [
            self.big_to_small,
            self.small_to_big,
            self.empty_big,
            self.empty_small,
            self.fill_big,
            self.fill_small,
        ]

    def big_to_small(self) -> 'SimplifiedWaterJugProblemState':
        big = max(0, self.big_jug + self.small_jug - 3)
        small = min(3, self.big_jug + self.small_jug)
        return SimplifiedWaterJugProblemState(big, small)

    def small_to_big(self) -> 'SimplifiedWaterJugProblemState':
        big = min(4, self.big_jug + self.small_jug)
        small = max(0, self.big_jug + self.small_jug - 4)
        return SimplifiedWaterJugProblemState(big, small)

    def empty_big(self) -> 'SimplifiedWaterJugProblemState':
        return SimplifiedWaterJugProblemState(0, self.small_jug)

    def empty_small(self) -> 'SimplifiedWaterJugProblemState':
        return SimplifiedWaterJugProblemState(self.big_jug, 0)

    def fill_big(self) -> 'SimplifiedWaterJugProblemState':
        return SimplifiedWaterJugProblemState(4, self.small_jug)

    def fill_small(self) -> 'SimplifiedWaterJugProblemState':
        return SimplifiedWaterJugProblemState(self.big_jug, 3)

    def is_goal_state(self) -> bool:
        return self.big_jug == 2
