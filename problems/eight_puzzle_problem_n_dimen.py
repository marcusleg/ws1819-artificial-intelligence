from problems.abstract_problem import AbstractProblemState
import numpy as np
import random as ran


class EightPuzzleProblemStateNDim(AbstractProblemState):
    # Grid positions are defined as such:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, heuristic=0, n=3):
        self.goal_state = self.get_goal_state(n)  # depending on dimension we create new goal state
        self.state = self.create_initial_state_state(self)  # state # shuffles the goal_state and checks if it is decidable
        self.use_heuristic_num = heuristic
        self.n = n  # dimension

    def __str__(self):
        # return self.state[:3] + "\n" + self.state[3:6] + "\n" +
        # self.state[7:]
        s = self.state
        output_array = ""
        for i in range(0, self.n ** 3):
            output_array += "%d\t" % self.state[i]
            if (i + 1) % self.n == 0:
                output_array += "\n"
            if (i + 1) % (self.n ** 2) == 0:
                output_array += "\n"
        return output_array # changed the method of showing array # "\n{} {} {}\n{} {} {}\n{} {} {}\n".format(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])

    def __eq__(self, other):
        return self.state == other.state

    @staticmethod
    def create_initial_state(heuristic=0):
        return EightPuzzleProblemStateNDim(heuristic, 3)

    def get_actions(self):
        actions = []
        if self.tile_position(0) % (self.n ** 2) > 2:
            actions.append(self.top_down)
        if self.tile_position(0) % (self.n ** 2) < 6:
            actions.append(self.bottom_up)
        if self.tile_position(0) % (self.n ** 2) not in [0, 3, 6]:
            actions.append(self.left_right)
        if self.tile_position(0) % (self.n ** 2) not in [2, 5, 8]:
            actions.append(self.right_left)
        if self.tile_position(0) > (self.n ** 2 - 1):
            actions.append(self.foward_backwards)
        if self.tile_position(0) < (2 * self.n ** 2):
            actions.append(self.backwards_forwards)
        return actions

    def get_heuristics(self):
        return [
            self.heuristic_manhatten_distance,
            self.heuristic_incorrectly_placed,
        ]

    def heuristic(self):
        return self.get_heuristics()[self.use_heuristic_num]()

    def heuristic_incorrectly_placed(self) -> int:
        """Number of tiles that are not in the correct position"""
        incorrectly_placed = 0
        for i in range(1, self.n ** 3):
            if self.tile_position(i) != self.goal_state.index(i):
                incorrectly_placed += 1
        return incorrectly_placed

    def heuristic_manhatten_distance(self) -> int:
        """Sum of Manhatten distances for each tile from current position to goal position"""
        sum_of_distances = 0
        for i in range(self.n ** 3):
            sum_of_distances += self.manhatten_distance(
                self.tile_position(i),
                self.goal_state.index(i)
            )
        return sum_of_distances

    @staticmethod
    def manhatten_distance(a: int, b: int) -> int:  # Marcus, I cannot understand for what this method is... that is why I cannot change it
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

    def top_down(self) -> 'EightPuzzleProblemStateNDim':
        """Move tile above the 0 down"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - self.n] = new_state[p0 - self.n], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def bottom_up(self) -> 'EightPuzzleProblemStateNDim':
        """Move tile below the 0 up"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + self.n] = new_state[p0 + self.n], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def left_right(self) -> 'EightPuzzleProblemStateNDim':
        """Move tile left of 0 right"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - 1] = new_state[p0 - 1], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def right_left(self) -> 'EightPuzzleProblemState':
        """Move tile right of 0 left"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + 1] = new_state[p0 + 1], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def foward_backwards(self) -> 'EightPuzzleProblemStateNDim':
        """Move tile forward of 0 backwards"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 - self.n ** 2] = new_state[p0 - self.n ** 2], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def backwards_forwards(self) -> 'EightPuzzleProblemStateNDim':
        """Move tile backwards of 0 forward"""
        p0 = self.tile_position(0)
        new_state = self.state.copy()
        new_state[p0], new_state[p0 + self.n ** 2] = new_state[p0 + self.n ** 2], new_state[p0]
        return EightPuzzleProblemStateNDim(new_state, self.use_heuristic_num)

    def is_decidable(self) -> bool:
        """Checks if the problem decidable or not"""
        inv = 0
        for i in range(0, self.n ** 3 - 1):
            if self.state[i] != 0:
                for j in range(0, i - 1):
                    if self.state[j] > self.state[i]:
                        inv += 1

        for  i in range(0, self.n ** 3 - 1):
            if self.state[i] == 0:
                inv += 1 + i / 4

        return inv % 2 if False else True

    def get_goal_state(n) -> []:
        goal_state = np.array(range(0, n ** 3))
        return goal_state

    def create_initial_state_state(self):
        self.state = self.goal_state
        ran.shuffle(self.state)
        while not self.is_decidable(self):
            self.state = self.goal_state
            ran.shuffle(self.state)
        return self.state

