import { Component } from '@angular/core';
import { pageAnimation } from './navigation/animations';
import { RouterOutlet } from '@angular/router'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [pageAnimation]
})
export class AppComponent {
  title = 'local-gitbook';
  routerState:boolean = true;
  component: any;
  constructor(){}
  prepareOutlet(outlet:RouterOutlet) {
    // console.log(outlet.component==this.component, this.routerState);
    if(outlet.component!=this.component){
      this.routerState=!this.routerState;
    }
    this.component=outlet.component;
    return this.routerState;
  }
}
