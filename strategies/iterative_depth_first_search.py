import time
from collections import namedtuple
from queue import LifoQueue

from strategies.abstract_strategy import AbstractStrategy

Node = namedtuple('Node', 'parent_node, depth, state, action')


class IterativeDepthFirstSearch(AbstractStrategy):
    root = None
    goal_node = None

    def find_solution(self):
        self.start_time = time.monotonic()

        depth_limit = 0

        solution_found = False
        while not solution_found:
            depth_limit += 1
            solution_found = self.iddfs(depth_limit)

        self.stop_time = time.monotonic()

    def iddfs(self, depth_limit: int):
        # build and traverse tree
        self.root = Node(
            parent_node=None,
            depth=1,
            state=self.problem.create_initial_state(),
            action="",
        )
        lifo_queue = LifoQueue()
        lifo_queue.put(self.root)

        while not lifo_queue.empty():
            # examine the next node
            this_node = lifo_queue.get()
            # is this node the goal?
            if this_node.state.is_goal_state():
                self.goal_node = this_node
                return True
                break
            # don't add child nodes if max depth is reached
            if this_node.depth >= depth_limit:
                continue
            # add child nodes for each possible action
            for action in this_node.state.get_actions():
                child_node = Node(
                    parent_node=this_node,
                    depth=this_node.depth + 1,
                    state=action(),
                    action=action,
                )
                lifo_queue.put(child_node)
        return False

    def print_solution(self):
        super().print_solution()
        # backtrace from goal_node to root
        path = []
        node = self.goal_node
        while node != self.root:
            path.append(node)
            node = node[0]
        path.reverse()

        for node in path:
            print("Action: {:50} State: {}".format(
                str(node.action), str(node.state)))

    def print_resource_usage_report(self):
        print("Time taken: {:.3f} seconds".format(
            self.stop_time - self.start_time))
