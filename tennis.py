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
        result = ""
        if (self.player1_points==self.player2_points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif (self.player1_points >= 4 or self.player2_points >= 4):
            minusResult = self.player1_points - self.player2_points
            if (minusResult==1):
                result ="Advantage " + self.player1_name
            elif (minusResult ==-1):
                result ="Advantage " + self.player2_name
            elif (minusResult>=2):
                result = "Win for " + self.player1_name
            else:
                result ="Win for " + self.player2_name
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
