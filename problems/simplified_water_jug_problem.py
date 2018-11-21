from functools import partial
from typing import List

from problems.abstract_problem import AbstractAction, AbstractProblem, AbstractState


class SimplifiedWaterJugState(AbstractState):

    def __init__(self, gallons_big_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.small_jug = gallons_small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.small_jug) + ")"


class SimplifiedWaterJugProblem(AbstractProblem):

    @staticmethod
    def create_initial_state() -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(0, 0)

    @staticmethod
    def get_actions() -> List[AbstractAction]:
        return [
            BigToSmall.execute,
            SmallToBig.execute,
            EmptyBig.execute,
            EmptySmall.execute,
            FillBig.execute,
            FillSmall.execute,
        ]

    @staticmethod
    def is_goal_state(state: SimplifiedWaterJugState) -> bool:
        return state.big_jug == 2


class BigToSmall(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        big = max(0, state.big_jug + state.small_jug - 3)
        small = min(3, state.big_jug + state.small_jug)
        return SimplifiedWaterJugState(big, small)


class SmallToBig(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        big = min(4, state.big_jug + state.small_jug)
        small = max(0, state.big_jug + state.small_jug - 4)
        return SimplifiedWaterJugState(big, small)


class EmptyBig(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(0, state.small_jug)


class EmptySmall(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(state.big_jug, 0)


class FillBig(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(4, state.small_jug)


class FillSmall(AbstractAction):

    @staticmethod
    def execute(state: SimplifiedWaterJugState) -> SimplifiedWaterJugState:
        return SimplifiedWaterJugState(state.big_jug, 3)


if __name__ == "__main__":
    state = SimplifiedWaterJugProblem.create_initial_state()
    path = [
        FillBig.execute,
        BigToSmall.execute,
        EmptySmall.execute,
        BigToSmall.execute,
        FillBig.execute,
        BigToSmall.execute,
    ]
    for action in path:
        state = partial(action, state)()
        print(state)
    print(SimplifiedWaterJugProblem.goal_reached(state))
