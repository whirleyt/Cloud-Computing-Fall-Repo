import { Component } from '@angular/core';
import { Router, NavigationEnd, Event as NavigationEvent } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Columni';
  shouldDisplayHeader: boolean;

    constructor(private router: Router) {
      this.shouldDisplayHeader = !['/', '/api/login', '/api/createProfile', '/api/guestLogin'].includes(
        this.router.url
      );

      this.router.events.subscribe((event) => {
        if (event instanceof NavigationEnd) {
          this.shouldDisplayHeader = !['/', '/api/login', '/api/createProfile', '/api/guestLogin'].includes(
            event.url || ''
          );
        }
      });
    }

    navigateTo(route: string): void {
      this.router.navigate([route]);
    }
}
