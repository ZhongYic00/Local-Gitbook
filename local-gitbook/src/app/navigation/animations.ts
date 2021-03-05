import { trigger, transition, animate, style, query, group } from '@angular/animations';

export const routeAnimation =
  trigger('routeAnimation', [
    transition(':enter', [
      style({
        position: 'absolute',
        width: '100%'
      }),
      animate('0.5s ease-in-out')
    ]),
    transition('* => *', [
      query(':leave', style({ transform: 'translateX(0)', position: 'absolute', width: '100%'}), { optional: true }),
      query(':enter', style({ transform: 'translateX(100%)', position: 'absolute', width: '100%'}), { optional: true }),

      group([
        query(':leave', animate('.5s ease-in-out', style({transform: 'translateX(-100%)', width: '100%'})), { optional: true }),
        query(':enter', animate('.5s ease-in-out', style({transform: 'translateX(0)', width: '100%'})), { optional: true })
      ])
    ])
  ]);
export const pageAnimation =
  trigger('pageAnimation', [
    transition(':enter', [
      style({
        position: 'absolute',
        width: '100%',
        opacity: 0
      }),
      animate('0.5s ease-in-out')
    ]),
    transition('* => *', [
      query(':leave', style({ opacity: 0, position: 'absolute', width: '100%'}), { optional: true }),
      query(':enter', style({ opacity: 0, position: 'absolute', width: '100%'}), { optional: true }),

      group([
        query(':leave', animate('.5s ease-in-out', style({opacity: 0, width: '100%'})), { optional: true }),
        query(':enter', animate('.5s ease-in-out', style({opacity: 1, width: '100%'})), { optional: true })
      ])
    ])
  ])