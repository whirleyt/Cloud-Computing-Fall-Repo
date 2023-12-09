import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Auth } from 'aws-amplify';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private router: Router) {}

  async login() {
    try {
      const user = await Auth.signIn(this.username, this.password);
      console.log('User signed in:', user);
      this.router.navigate(['/api/posts']); // Adjust the route as needed
    } catch (error) {
      console.error('Login failed:', error);
    }
  }

  createProfile() {
    this.router.navigate(['/api/createProfile']);
  }

  guestLogin() {
    this.router.navigate(['/api/guestLogin']);
  }
}
