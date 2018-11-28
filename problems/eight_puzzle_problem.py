#from problem.abstract_problem import AbstractProblemState
from problems.abstract_problem import AbstractProblemState


class EightPuzzleProblemState(AbstractProblemState):
    # Grid positions are defined as such:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, state):
        self.state = state

    def __str__(self):
        # return self.state[:3] + "\n" + self.state[3:6] + "\n" +
        # self.state[7:]
        s = self.state
        return "\n{} {} {}\n{} {} {}\n{} {} {}\n".format(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])

    def __eq__(self, other):
        return self.state == other.state

    @staticmethod
    def create_initial_state():
        # return EightPuzzleProblemState([7, 2, 4, 5, 0, 6, 8, 3, 1])
        return EightPuzzleProblemState([3, 1, 2, 4, 7, 5, 6, 8, 0])

    def get_actions(self):
        actions = []
        if self.tile_position(0) > 2:
            actions.append(self.top_down)
        if self.tile_position(0) < 6:
            actions.append(self.bottom_up)
        if self.tile_position(0) not in [0, 3, 6]:
            actions.append(self.left_right)
        if self.tile_position(0) not in [2, 5, 8]:
            actions.append(self.right_left)
        return actions

    def heuristic(self) -> int:
        sum_of_distances = 0
        for i in range(1, 9):
            sum_of_distances += self.manhatten_distance(
                self.tile_position(i),
                self.goal_state.index(i)
            )
        return sum_of_distances

    @staticmethod
    def manhatten_distance(a: int, b: int) -> int:
        a_x = a % 3
        a_y = int(a / 3)
        b_x = b % 3
        b_y = int(b / 3)
        return int(abs(a_x - b_x) + abs(a_y - b_y))

    def is_goal_state(self):
        return self.state == self.goal_state

    def tile_position(self, n: int) -> int:
        """Returns the index of the field containing n"""
        return self.state.index(n)

    def top_down(self) -> 'EightPuzzleProblemState':
        """Move tile above the 0 down"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - 3] = new_state[p0 - 3], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def bottom_up(self) -> 'EightPuzzleProblemState':
        """Move tile below the 0 up"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + 3] = new_state[p0 + 3], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def left_right(self) -> 'EightPuzzleProblemState':
        """Move tile left of 0 right"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - 1] = new_state[p0 - 1], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def right_left(self) -> 'EightPuzzleProblemState':
        """Move tile right of 0 left"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + 1] = new_state[p0 + 1], new_state[p0]
        return EightPuzzleProblemState(new_state)
