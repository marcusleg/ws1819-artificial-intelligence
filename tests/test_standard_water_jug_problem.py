import unittest

from problems.standard_water_jug_problem import *


class TestProblemStandardWaterJugProblem(unittest.TestCase):

    def test_initial_state_is_not_goal_state(self):
        initial_state = StandardWaterJugProblemState.create_initial_state()
        self.assertFalse(initial_state.is_goal_state())

    def test_is_goal_state_with_correct_goal(self):
        state = StandardWaterJugProblemState(4, 4, 0)
        self.assertTrue(state.is_goal_state())

    def test_440_big_to_medium(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.big_to_medium()
        expected_state = StandardWaterJugProblemState(3, 5, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_big_to_small(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.big_to_small()
        expected_state = StandardWaterJugProblemState(1, 4, 3)
        self.assertEqual(expected_state, new_state)

    def test_440_medium_to_small(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.medium_to_small()
        expected_state = StandardWaterJugProblemState(4, 1, 3)
        self.assertEqual(expected_state, new_state)

    def test_440_medium_to_big(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.medium_to_big()
        expected_state = StandardWaterJugProblemState(8, 0, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_small_to_big(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.small_to_big()
        expected_state = StandardWaterJugProblemState(4, 4, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_small_to_medium(self):
        initial_state = StandardWaterJugProblemState(4, 4, 0)
        new_state = initial_state.small_to_medium()
        expected_state = StandardWaterJugProblemState(4, 4, 0)
        self.assertEqual(expected_state, new_state)

    def test_323_small_to_medium(self):
        initial_state = StandardWaterJugProblemState(3, 2, 3)
        new_state = initial_state.small_to_medium()
        expected_state = StandardWaterJugProblemState(3, 5, 0)
        self.assertEqual(expected_state, new_state)
