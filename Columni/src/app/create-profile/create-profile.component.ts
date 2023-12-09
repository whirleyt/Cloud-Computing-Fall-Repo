import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Auth } from 'aws-amplify';

@Component({
  selector: 'app-create-profile',
  templateUrl: './create-profile.component.html',
  styleUrls: ['./create-profile.component.css']
})
export class CreateProfileComponent {
  user = {
    userID: null,
    schoolID: null,
    isAdmin: false,
    firstName: '',
    lastName: '',
    columbiaEmail: '',
    password: '',
    profilePicture: null,
    major: '',
    jobTitle: '',
    company: '',
    graduationYear: null,
    userDescription: ''
  };

   schoolOptions = [
        { schoolID: 1, schoolName: 'Columbia College' },
        { schoolID: 2, schoolName: 'SEAS' },
        { schoolID: 3, schoolName: 'Columbia Business School' },
        { schoolID: 4, schoolName: 'Graduate School of Arts and Sciences' },
        { schoolID: 5, schoolName: 'School of General Studies' },
        { schoolID: 6, schoolName: 'Columbia Law School' },
        { schoolID: 7, schoolName: 'Mailman School of Public Health' },
        { schoolID: 8, schoolName: 'Columbia University College of Physicians and Surgeons' },
        { schoolID: 9, schoolName: 'SIPA' },
        { schoolID: 10, schoolName: 'Graduate School of Journalism' },
        { schoolID: 11, schoolName: 'School of the Arts' },
        { schoolID: 12, schoolName: 'GSAPP' },
      ];

      graduationYearOptions = Array.from({ length: 10 }, (_, i) => new Date().getFullYear() - i);


  constructor(private router: Router) {}

  async saveProfile() {
    try {
      // Save user profile logic
      const user = await Auth.currentAuthenticatedUser();
      console.log('User profile saved:', this.user, user);
    } catch (error) {
      console.error('Profile save failed:', error);
    }
  }

  onFileSelected(event: any) {
    // Implement logic to handle the selected profile picture file
    const file = event.target.files[0];
    // Process the file as needed
  }

  onYearSelected(event: any) {
    this.user.graduationYear = event;
  }

  returnToLogin() {
    this.router.navigate(['/api/login']);
  }
}
