# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        score = Score(self.player1_points, self.player2_points)

        if score.is_love_all():
            return "Love-All"
        if score.is_fifteen_all():
            return "Fifteen-All"
        if score.is_thirty_all():
            return "Thirty-All"
        if score.players_have_tied_score():
            return "Deuce"
        if score.advantage_for_player_1():
            return "Advantage " + self.player1_name
        if score.advantage_for_player_2():
            return "Advantage " + self.player2_name
        if score.player1_won():
            return "Win for " + self.player1_name
        if score.player2_won():
            return "Win for " + self.player2_name

        result = ""
        points_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        result += points_names[self.player1_points]
        result += "-"
        result += points_names[self.player2_points]
        return result


class Score:
    def __init__(self, player1_points, player2_points):
        self.player1_points = player1_points
        self.player2_points = player2_points

    def players_have_tied_score(self):
        return self.player1_points == self.player2_points

    def almost_one_of_the_players_is_winning(self):
        return self.player1_points >= 4 or self.player2_points >= 4

    def advantage_for_player_1(self):
        return self.almost_one_of_the_players_is_winning() and \
               self.player1_points - self.player2_points == 1

    def advantage_for_player_2(self):
        return self.almost_one_of_the_players_is_winning() and \
               self.player2_points - self.player1_points == 1

    def player1_won(self):
        return self.almost_one_of_the_players_is_winning() and \
               self.player1_points - self.player2_points >= 2

    def player2_won(self):
        return self.almost_one_of_the_players_is_winning() and \
               self.player2_points - self.player1_points >= 2

    def is_love_all(self):
        return self.player1_points == self.player2_points == 0

    def is_fifteen_all(self):
        return self.player1_points == self.player2_points == 1

    def is_thirty_all(self):
        return self.player1_points == self.player2_points == 2
