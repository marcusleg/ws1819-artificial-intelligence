from functools import partial
from queue import Queue

from problems.abstract_problem import AbstractProblem
from strategies.abstract_strategy import AbstractStrategy


class BreadthFirstSearch(AbstractStrategy):
    root = None
    goal_node = None

    def find_solution(self):
        # (parent_node, state, action that lead to this state)
        self.root = (None, self.problem.create_initial_state(), "")
        fifo_queue = Queue()
        fifo_queue.put(self.root)

        # build and traverse tree
        while True:
            # examine the next node
            node = fifo_queue.get()
            state = node[1]
            # is this node the goal?
            if self.problem.is_goal_state(state):
                self.goal_node = node
                break
            # add new state for each possible action
            for action in self.problem.get_actions():
                new_state = partial(action, state)()
                fifo_queue.put((node, new_state, action))

    def print_solution(self):
        super().print_solution()
        path = []
        node = self.goal_node
        while node != self.root:
            path.append(node)
            node = node[0]
        path.reverse()

        for node in path:
            print("Action: {:50} State: {}".format(str(node[2]), str(node[1])))
