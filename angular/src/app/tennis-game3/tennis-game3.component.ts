import { Component, OnInit } from '@angular/core';
import {TennisGame} from '../TennisGame';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-tennis-game3',
  templateUrl: './tennis-game3.component.html',
  styleUrls: ['./tennis-game3.component.scss']
})
export class TennisGame3Component implements OnInit, TennisGame {
  private p2 = 0;
  private p1 = 0;
  private p1N = 'player1';
  private p2N = 'player2';
  player1Score = new FormControl(0);

  constructor() { }

  ngOnInit() {
  }

  wonPoint(playerName: string): void {
    if (playerName === 'player1')
      this.p1 += 1;
    else
      this.p2 += 1;
  }

  getScore(): string {
    let s: string;
    if (this.p1 < 4 && this.p2 < 4 && !(this.p1 + this.p2 === 6)) {
      const p: string[] = ['Love', 'Fifteen', 'Thirty', 'Forty'];
      s = p[this.p1];
      return (this.p1 === this.p2) ? s + '-All' : s + '-' + p[this.p2];
    } else {
      if (this.p1 === this.p2)
        return 'Deuce';
      s = this.p1 > this.p2 ? this.p1N : this.p2N;
      return (((this.p1 - this.p2) * (this.p1 - this.p2)) === 1) ? 'Advantage ' + s : 'Win for ' + s;
    }
  }

}
