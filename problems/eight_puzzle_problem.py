#from problem.abstract_problem import AbstractProblemState
from problems.abstract_problem import AbstractProblemState


class EightPuzzleProblemState(AbstractProblemState):
    # Grid positions are defined as such:
    # 0 1 2
    # 3 4 5
    # 6 7 8

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
        if self.empty_field_pos() > 2:
            actions.append(self.top_down)
        if self.empty_field_pos() < 6:
            actions.append(self.bottom_up)
        if self.empty_field_pos() not in [0, 3, 6]:
            actions.append(self.left_right)
        if self.empty_field_pos() not in [2, 5, 8]:
            actions.append(self.right_left)
        return actions

    def is_goal_state(self):
        return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def empty_field_pos(self) -> int:
        """Returns the index of the field containing the zero"""
        return self.state.index(0)

    def swap_pos(self, i, j):
        self.state[i], self.state[j] = self.state[j], self.state[i]

    def top_down(self) -> 'EightPuzzleProblemState':
        """Move tile above the 0 down"""
        p0 = self.empty_field_pos()
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - 3] = new_state[p0 - 3], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def bottom_up(self) -> 'EightPuzzleProblemState':
        """Move tile below the 0 up"""
        p0 = self.empty_field_pos()
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + 3] = new_state[p0 + 3], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def left_right(self) -> 'EightPuzzleProblemState':
        """Move tile left of 0 right"""
        p0 = self.empty_field_pos()
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - 1] = new_state[p0 - 1], new_state[p0]
        return EightPuzzleProblemState(new_state)

    def right_left(self) -> 'EightPuzzleProblemState':
        """Move tile right of 0 left"""
        p0 = self.empty_field_pos()
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + 1] = new_state[p0 + 1], new_state[p0]
        return EightPuzzleProblemState(new_state)

if __name__ == "__main__":
    state = EightPuzzleProblemState.create_initial_state()
    for action in state.get_actions():
        new_state = action()
        print(new_state)
