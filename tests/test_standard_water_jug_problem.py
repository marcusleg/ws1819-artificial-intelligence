import unittest

from problems.standard_water_jug_problem import *


class TestProblemStandardWaterJugProblem(unittest.TestCase):

    def test_440_big_to_medium(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = BigToMedium.execute(initial_state)
        expected_state = StandardWaterJugState(3, 5, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_big_to_small(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = BigToSmall.execute(initial_state)
        expected_state = StandardWaterJugState(1, 4, 3)
        self.assertEqual(expected_state, new_state)

    def test_440_medium_to_small(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = MediumToSmall.execute(initial_state)
        expected_state = StandardWaterJugState(4, 1, 3)
        self.assertEqual(expected_state, new_state)

    def test_440_medium_to_big(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = MediumToBig.execute(initial_state)
        expected_state = StandardWaterJugState(8, 0, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_small_to_big(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = SmallToBig.execute(initial_state)
        expected_state = StandardWaterJugState(4, 4, 0)
        self.assertEqual(expected_state, new_state)

    def test_440_small_to_mediun(self):
        initial_state = StandardWaterJugState(4, 4, 0)
        new_state = SmallToMedium.execute(initial_state)
        expected_state = StandardWaterJugState(4, 4, 0)
        self.assertEqual(expected_state, new_state)

    def test_323_small_to_mediun(self):
        initial_state = StandardWaterJugState(3, 2, 3)
        new_state = SmallToMedium.execute(initial_state)
        expected_state = StandardWaterJugState(3, 5, 0)
        self.assertEqual(expected_state, new_state)

    # TODO there's a lot of cases yet to cover
