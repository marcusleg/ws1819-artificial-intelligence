from functools import partial
from queue import Queue
from typing import List

from problems.abstract_problem import (AbstractAction, AbstractProblem,
                                       AbstractState)


def breadth_first_search(problem: AbstractProblem):
    initial_state = problem.create_initial_state()
    actions = problem.get_actions()

    # (parent_node, state, action that lead to this state)
    root = (None, initial_state, "")
    goal_node = None
    fifo_queue = Queue()
    fifo_queue.put(root)

    # build and traverse tree
    while True:
        # examine the next node
        node = fifo_queue.get()
        state = node[1]
        # is this node the goal?
        if problem.is_goal_state(state):
            goal_node = node
            break
        # add new state for each possible action
        for action in actions:
            new_state = partial(action, state)()
            fifo_queue.put((node, new_state, action))

    # backtrace
    path = []
    node = goal_node
    while node != root:
        path.append(node)
        node = node[0]
    path.reverse()

    for node in path:
        print("Action: {:50} State: {}".format(str(node[2]), str(node[1])))
