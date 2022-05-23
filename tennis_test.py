# -*- coding: utf-8 -*-
import unittest

import pytest
from tennis import TennisGame1

from tennis_unit_test import test_cases, play_game

class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game1(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennis2(unittest.TestCase):

    def test_Score_Game1(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())
