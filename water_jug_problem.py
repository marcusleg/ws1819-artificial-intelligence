#!/bin/python3

from functools import partial


class State:
    big_jug: int
    small_jug: int

    def __init__(self, gallons_big_jug: int, gallons_small_jug: int):
        self.big_jug = gallons_big_jug
        self.small_jug = gallons_small_jug

    def __str__(self) -> str:
        return "(" + str(self.big_jug) + ", " + str(self.small_jug) + ")"


def big_to_small(state: 'State') -> 'State':
    big = max(0, state.big_jug + state.small_jug - 3)
    small = min(3, state.big_jug + state.small_jug)
    return State(big, small)

def small_to_big(state: 'State') -> 'State':
    big = min(4, state.big_jug + state.small_jug)
    small = max(0, state.big_jug + state.small_jug - 4)
    return State(big, small)

def fill_big(state: 'State') -> 'State':
    return State(4, state.small_jug)

def fill_small(state: 'State') -> 'State':
    return State(state.big_jug, 3)

def empty_big(state: 'State') -> 'State':
    return State(0, state.small_jug)

def empty_small(state: 'State') -> 'State':
    return State(state.big_jug, 0)

def goal_reached(state: 'State') -> bool:
    return state.big_jug == 2


if __name__ == "__main__":
    state = State(0, 0)
    path = [fill_big, big_to_small, empty_small, big_to_small, fill_big, big_to_small]
    for action in path:
        state = partial(action, state)()
        print(state)
    print(goal_reached(state))
