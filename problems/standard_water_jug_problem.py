"""
Formalization of the Water Jug Problem as described here:
https://en.wikipedia.org/wiki/Water_pouring_puzzle#Standard_example
"""

from functools import partial
from typing import List

from problems.abstract_problem import (AbstractAction, AbstractProblem,
                                       AbstractState)


class StandardWaterJugState(AbstractState):

    def __init__(self, gallons_big_jug: int, gallons_medium_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.medium_jug = gallons_medium_jug
        self.small_jug = gallons_small_jug

    def __eq__(self, other):
        return self.big_jug == other.big_jug and self.medium_jug == other.medium_jug and self.small_jug == other.small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.medium_jug) + ", " + str(self.small_jug) + ")"


class StandardWaterJugProblem(AbstractProblem):

    @staticmethod
    def create_initial_state() -> StandardWaterJugState:
        return StandardWaterJugState(8, 0, 0)

    @staticmethod
    def get_actions() -> List[AbstractAction]:
        return [
            BigToSmall.execute,
            BigToMedium.execute,
            MediumToBig.execute,
            MediumToSmall.execute,
            SmallToBig.execute,
            SmallToMedium.execute,
        ]

    @staticmethod
    def is_goal_state(state: StandardWaterJugState) -> bool:
        return state.big_jug == 4 and state.medium_jug == 4 and state.small_jug == 0


class BigToMedium(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = max(0, state.big_jug + state.medium_jug - 5)
        medium = min(5, state.big_jug + state.medium_jug)
        small = state.small_jug
        return StandardWaterJugState(big, medium, small)


class BigToSmall(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = max(0, state.big_jug - (3 - state.small_jug))
        medium = state.medium_jug
        small = min(3, state.big_jug + state.small_jug)
        return StandardWaterJugState(big, medium, small)


class MediumToBig(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = min(8, state.big_jug + state.medium_jug)
        medium = max(0, state.big_jug + state.medium_jug - 8)
        small = state.small_jug
        return StandardWaterJugState(big, medium, small)


class MediumToSmall(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = state.big_jug
        medium = max(0, state.medium_jug + state.small_jug - 3)
        small = min(3, state.medium_jug + state.small_jug)
        return StandardWaterJugState(big, medium, small)


class SmallToMedium(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = state.big_jug
        medium = min(5, state.medium_jug + state.small_jug)
        small = max(0, state.medium_jug + state.small_jug - 5)
        return StandardWaterJugState(big, medium, small)


class SmallToBig(AbstractAction):

    @staticmethod
    def execute(state: StandardWaterJugState) -> StandardWaterJugState:
        big = min(8, state.big_jug + state.small_jug)
        medium = state.medium_jug
        small = max(0, state.big_jug + state.small_jug - 8)
        return StandardWaterJugState(big, medium, small)
