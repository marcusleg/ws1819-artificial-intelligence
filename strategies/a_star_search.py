from dataclasses import dataclass, field
import time
from queue import PriorityQueue

from problems.abstract_problem import AbstractProblemState
from strategies.abstract_strategy import AbstractStrategy


@dataclass(order=True)
class Node:
    priority: int
    cost_so_far: int = field(compare=False)
    parent_node: 'Node' = field(compare=False)
    state: 'AbstractProblemState' = field(compare=False)
    action: str = field(compare=False)


class AStarStrategy(AbstractStrategy):

    def __init__(self, problem):
        super().__init__(problem)

        if self.problem.create_initial_state().heuristic() == None:
            exit("A* can't run without a heuristic")

        self.start_time = None
        self.stop_time = None
        self.root = None
        self.goal_node = None

    def find_solution(self):
        self.start_time = time.monotonic()
        initial_state = self.problem.create_initial_state()
        self.root = Node(
            priority=initial_state.heuristic(),
            parent_node=None,
            state=initial_state,
            cost_so_far=0,
            action=""
        )
        priority_queue = PriorityQueue()
        priority_queue.put_nowait(self.root)

        while not priority_queue.empty():
            # examine the next node
            this_node = priority_queue.get()
            # is this node the goal?
            if this_node.state.is_goal_state():
                self.goal_node = this_node
                break
            # add new state for each possible action
            for action in this_node.state.get_actions():
                cost_so_far = this_node.cost_so_far + 1
                estimated_cost = cost_so_far + this_node.state.heuristic()
                child_node = Node(
                    priority=estimated_cost,
                    cost_so_far=cost_so_far,
                    parent_node=this_node,
                    state=action(),
                    action=action.__name__,
                )
                priority_queue.put(child_node)

        self.stop_time = time.monotonic()

    def print_solution(self):
        super().print_solution()
        path = []
        node = self.goal_node
        while node.state != self.root.state:
            path.append(node)
            node = node.parent_node
        path.reverse()

        for node in path:
            print("Action: {:20} Cost so far: {:3} Heuristic: {:3} State: {}".format(
                str(node.action),
                str(node.cost_so_far),
                str(node.priority - node.cost_so_far),
                str(node.state)
            ))

    def print_resource_usage_report(self):
        print("Time taken: {:.3f} seconds".format(
            self.stop_time - self.start_time))
