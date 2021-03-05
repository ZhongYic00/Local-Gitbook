import { Component } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Router, NavigationEnd, ChildActivationEnd, ActivatedRoute, ActivationEnd, RouterOutlet } from '@angular/router';
import { routeAnimation } from './animations';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css'],
  animations: [routeAnimation]
})
export class NavigationComponent {
  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  routerState:boolean = true;
  routerStateCode:string = 'active';
  active=true;
  count=0;
  constructor(private router:Router, private breakpointObserver: BreakpointObserver){
      /*this.router.events.subscribe(event => {
        if(event instanceof NavigationEnd)
          console.log(this.active);
        if (event instanceof NavigationEnd && this.active && this.count<10) {
          console.log('change state');
          this.count++;
          // 每次路由跳转改变状态
          this.routerState = !this.routerState;
          this.routerStateCode = this.routerState ? 'active' : 'inactive';
        }
      });*/
  }
  component:any;
  prepareOutlet(outlet:RouterOutlet) {
    //console.log('outlet is',outlet.component==this.component, this.component);
    if(this.component!=outlet.component && this.component){
      this.routerState=!this.routerState;
    }
    this.component=outlet.component;
    return this.routerState;
  }
}
