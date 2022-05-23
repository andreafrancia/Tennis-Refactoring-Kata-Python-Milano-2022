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

    def players_have_tied_score(self):
        return self.player1_points==self.player2_points

    def score(self):
        result = ""
        if self.players_have_tied_score():
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif self.almost_one_of_the_players_is_winning():
            if self.advantage_for_player_1():
                result = "Advantage " + self.player1_name
            elif self.advantage_for_player_2():
                result = "Advantage " + self.player2_name
            elif self.player1_won():
                result = "Win for " + self.player1_name
            else:
                result = "Win for " + self.player2_name
        else:
            for i in range(1,3):
                if (i==1):
                    tempScore = self.player1_points
                else:
                    result+="-"
                    tempScore = self.player2_points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result

    def almost_one_of_the_players_is_winning(self):
        return self.player1_points >= 4 or self.player2_points >= 4

    def advantage_for_player_1(self):
        return self.player1_points - self.player2_points == 1

    def advantage_for_player_2(self):
        return self.player2_points - self.player1_points == 1

    def player1_won(self):
        return self.player1_points - self.player2_points >= 2
