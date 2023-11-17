import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private router: Router) {}

  login()
  {
    console.log('Username: ' + this.username);
    console.log('Password: ' + this.password);
    var socialPostID= 1;
    this.router.navigate(['api/posts/'+ socialPostID]);
  }

  createProfile()
  {
   this.router.navigate(['api/createProfile']);
  }

  guestLogin()
   {
     this.router.navigate(['api/guestLogin']);
   }
}
