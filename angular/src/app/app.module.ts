import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TennisGame2Component } from './tennis-game2/tennis-game2.component';
import { TennisGame1Component } from './tennis-game1/tennis-game1.component';
import { TennisGame3Component } from './tennis-game3/tennis-game3.component';

@NgModule({
  declarations: [
    AppComponent,
    TennisGame2Component,
    TennisGame1Component,
    TennisGame3Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
