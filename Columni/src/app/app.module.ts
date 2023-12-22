import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { MatTabsModule } from '@angular/material/tabs';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AmplifyAuthenticatorModule } from '@aws-amplify/ui-angular';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { CreateProfileComponent } from './create-profile/create-profile.component';
import { JobPostComponent } from './job-post/job-post.component';
import { EventPostComponent } from './event-post/event-post.component';
import { SocialPostComponent } from './social-post/social-post.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { MessagesComponent } from './messages/messages.component';
import { MessageService } from './messages/message.service';

import { UsersComponent } from './users/users.component';
import { PostCommentsComponent } from './post-comments/post-comments.component';
import { PostLikesComponent } from './post-likes/post-likes.component';
import { GuestLoginComponent } from './guest-login/guest-login.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CreateProfileComponent,
    JobPostComponent,
    EventPostComponent,
    SocialPostComponent,
    UserProfileComponent,
    MessagesComponent,
    UsersComponent,
    PostCommentsComponent,
    PostLikesComponent,
    GuestLoginComponent,
    HomeComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    MatCardModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatInputModule,
    MatTabsModule,
    MatSelectModule,
    MatDatepickerModule,
    RouterModule,
    AmplifyAuthenticatorModule,
    HttpClientModule
  ],
  providers: [
    MessageService,


  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
