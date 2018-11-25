from functools import partial
from typing import List

from problems.abstract_problem import AbstractProblem, AbstractState


class SimplifiedWaterJugState(AbstractState):

    def __init__(self, gallons_big_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.small_jug = gallons_small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.small_jug) + ")"

    def get_actions(self):
        return [
            self.big_to_small,
            self.small_to_big,
            self.empty_big,
            self.empty_small,
            self.fill_big,
            self.fill_small,
        ]

    def big_to_small(self):
        big = max(0, self.big_jug + self.small_jug - 3)
        small = min(3, self.big_jug + self.small_jug)
        return SimplifiedWaterJugState(big, small)

    def small_to_big(self):
        big = min(4, self.big_jug + self.small_jug)
        small = max(0, self.big_jug + self.small_jug - 4)
        return SimplifiedWaterJugState(big, small)

    def empty_big(self):
        return SimplifiedWaterJugState(0, self.small_jug)

    def empty_small(self):
        return SimplifiedWaterJugState(self.big_jug, 0)

    def fill_big(self):
        return SimplifiedWaterJugState(4, self.small_jug)

    def fill_small(self):
        return SimplifiedWaterJugState(self.big_jug, 3)


class SimplifiedWaterJugProblem(AbstractProblem):

    @staticmethod
    def create_initial_state() -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(0, 0)

    @staticmethod
    def is_goal_state(state: SimplifiedWaterJugState) -> bool:
        return state.big_jug == 2
