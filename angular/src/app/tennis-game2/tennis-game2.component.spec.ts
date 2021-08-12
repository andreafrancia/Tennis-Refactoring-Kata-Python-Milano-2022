import {async} from '@angular/core/testing';
import {TennisGame2Component} from './tennis-game2.component';
import {
  TennisComponentTester
} from '../../test/tennisTester';
import {getScoreButton, overallScore, player1ScoreInput, player2ScoreInput} from '../../test/selectors';
import {expectedTennisScores} from '../../test/expectedResults';

describe('Tennis Game 2', () => {
  let tennisTester: TennisComponentTester;

  beforeEach(async(() => {
    tennisTester = new TennisComponentTester();
    tennisTester.beforeEach([TennisGame2Component]);
  }));

  expectedTennisScores.forEach(([player1Score, player2Score, expectedScore]) => {
    it(`should score '${expectedScore}' when player 1 has '${player1Score}' and player 2 has '${player2Score}'`, () => {
      tennisTester.verifyLabelText(overallScore, '');

      tennisTester.setInputValue(player1ScoreInput, player1Score);
      tennisTester.setInputValue(player2ScoreInput, player2Score);
      tennisTester.selectElement(getScoreButton);

      tennisTester.verifyLabelText(overallScore, expectedScore);
    });
  });
});
