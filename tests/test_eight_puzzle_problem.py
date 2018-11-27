import unittest

from problems.eight_puzzle_problem import EightPuzzleProblemState


class TestEightPuzzleProblem(unittest.TestCase):

    def test_equal(self):
        state1 = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        state2 = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        self.assertEqual(state1, state2)

    def test_not_equal(self):
        state1 = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        state2 = EightPuzzleProblemState([
            8, 2, 3,
            4, 0, 5,
            6, 7, 7
        ])
        self.assertNotEqual(state1, state2)

    def test_bottom_up_zero_centered(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        new_state = initial_state.bottom_up()
        expected_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 7, 5,
            6, 0, 8
        ])
        self.assertEqual(expected_state, new_state)

    def test_top_down_zero_centered(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        new_state = initial_state.top_down()
        expected_state = EightPuzzleProblemState([
            1, 0, 3,
            4, 2, 5,
            6, 7, 8
        ])
        self.assertEqual(expected_state, new_state)

    def test_left_right_zero_centered(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        new_state = initial_state.left_right()
        expected_state = EightPuzzleProblemState([
            1, 2, 3,
            0, 4, 5,
            6, 7, 8
        ])
        self.assertEqual(expected_state, new_state)

    def test_right_left_zero_centered(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        new_state = initial_state.right_left()
        expected_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 5, 0,
            6, 7, 8
        ])
        self.assertEqual(expected_state, new_state)

    def test_left_right_zero_top_middle(self):
        initial_state = EightPuzzleProblemState([
            1, 0, 2,
            3, 4, 5,
            6, 7, 8,
        ])
        new_state = initial_state.left_right()
        expected_state = EightPuzzleProblemState([
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        ])
        self.assertEqual(expected_state, new_state)

    def test_circular_actions(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8,
        ])
        new_state = initial_state.bottom_up()
        new_state = new_state.left_right()
        new_state = new_state.top_down()
        new_state = new_state.right_left()
        expected_state = EightPuzzleProblemState([
            1, 2, 3,
            7, 0, 5,
            4, 6, 8,
        ])
        self.assertEqual(expected_state, new_state)

    def test_calling_action_does_not_change_initial_state(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8,
        ])
        new_state = initial_state.top_down()
        self.assertNotEqual(initial_state, new_state)

    def test_get_actions_zero_centered(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 0, 5,
            6, 7, 8
        ])
        expected_actions = [
            'top_down',
            'bottom_up',
            'left_right',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_top_middle(self):
        initial_state = EightPuzzleProblemState([
            1, 0, 3,
            4, 2, 5,
            6, 7, 8
        ])
        expected_actions = [
            'bottom_up',
            'left_right',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_bottom_middle(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 7, 5,
            6, 0, 8
        ])
        expected_actions = [
            'top_down',
            'left_right',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_left_center(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            0, 4, 5,
            6, 7, 8
        ])
        expected_actions = [
            'top_down',
            'bottom_up',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_right_center(self):
        initial_state = EightPuzzleProblemState([
            1, 2, 3,
            4, 5, 0,
            6, 7, 8
        ])
        expected_actions = [
            'top_down',
            'bottom_up',
            'left_right',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_top_left(self):
        initial_state = EightPuzzleProblemState([
            0, 2, 3,
            4, 5, 1,
            6, 7, 8
        ])
        expected_actions = [
            'bottom_up',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_top_right(self):
        initial_state = EightPuzzleProblemState([
            3, 2, 0,
            4, 5, 1,
            6, 7, 8
        ])
        expected_actions = [
            'bottom_up',
            'left_right',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_bottom_left(self):
        initial_state = EightPuzzleProblemState([
            3, 2, 6,
            4, 5, 1,
            0, 7, 8
        ])
        expected_actions = [
            'top_down',
            'right_left',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_get_actions_zero_bottom_right(self):
        initial_state = EightPuzzleProblemState([
            3, 2, 6,
            4, 5, 1,
            8, 7, 0
        ])
        expected_actions = [
            'top_down',
            'left_right',
        ]
        actual_actions = [
            action.__name__ for action in initial_state.get_actions()]
        self.assertListEqual(expected_actions, actual_actions)

    def test_is_goal_state(self):
        state = EightPuzzleProblemState([
            0, 1, 2,
            3, 4, 5,
            6, 7, 8,
        ])
        self.assertTrue(state.is_goal_state())

    def test_manhatten_distance(self):
        tests = [
            #a, b, distance
            [0, 1, 1],
            [0, 2, 2],
            [0, 3, 1],
            [0, 4, 2],
            [0, 5, 3],
            [0, 6, 2],
            [0, 7, 3],
            [0, 8, 4],
        ]
        for t in tests:
            d = EightPuzzleProblemState.manhatten_distance(t[0], t[1])
            self.assertEqual(d, t[2])

    def test_heuristic(self):
        state = EightPuzzleProblemState([
            0, 2, 3,
            4, 5, 1,
            6, 7, 8
        ])
        self.assertEqual(1 + 1 + 2 + 1 + 1 + 2, state.heuristic())
