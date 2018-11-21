#/bin/python3

from breadth_first_search import breadth_first_search
from water_jug_problem import State, big_to_small, small_to_big, empty_big, empty_small, fill_big, fill_small

initial_state = State(0, 0)
actions = [
    big_to_small,
    small_to_big,
    fill_big,
    fill_small,
    empty_big,
    empty_small,
]

breadth_first_search(initial_state, actions)
