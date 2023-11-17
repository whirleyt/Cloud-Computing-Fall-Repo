import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { CreateProfileComponent } from './create-profile/create-profile.component';
import { JobPostComponent } from './job-post/job-post.component';
import { EventPostComponent } from './event-post/event-post.component';
import { SocialPostComponent } from './social-post/social-post.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { MessagesComponent } from './messages/messages.component';
import { UsersComponent } from './users/users.component';
import { PostCommentsComponent } from './post-comments/post-comments.component';
import { PostLikesComponent } from './post-likes/post-likes.component';
import { GuestLoginComponent } from './guest-login/guest-login.component';

const routes: Routes = [
  { path: '', redirectTo: 'api/login', pathMatch: 'full' },
  { path: 'api/posts/:postTypeID', redirectTo: 'api/posts/:postTypeID/page/1', pathMatch: 'full' },
  { path: 'api/messages', redirectTo: 'api/messages/:userID/page/:page', pathMatch: 'full' },
  { path: 'api/messages/:userID/:messageThreadID', redirectTo: 'api/messages/:userID/:messageThreadID/page/:page', pathMatch: 'full' },
  { path: 'api/users', redirectTo: 'api/users/page/:page', pathMatch: 'full' },
  { path: 'api/posts/:postTypeID/:postID/comments', redirectTo: 'api/posts/:postTypeID/:postID/comments/page/1', pathMatch: 'full' },
  { path: 'api/posts/:postTypeID/:postID/likes', redirectTo: 'api/posts/:postTypeID/:postID/likes/page/1', pathMatch: 'full' },
  { path: 'api/login', component: LoginComponent },
  { path: 'api/guestLogin', component: GuestLoginComponent },
  { path: 'api/createProfile', component: CreateProfileComponent },
  { path: 'api/posts/1/page/:page', component: SocialPostComponent },
  { path: 'api/posts/1/newPost', component: SocialPostComponent },
  { path: 'api/posts/2/page/:page', component: JobPostComponent },
  { path: 'api/posts/2/newPost', component: JobPostComponent },
  { path: 'api/posts/3/page/:page', component: EventPostComponent },
  { path: 'api/posts/3/newPost', component: EventPostComponent },
  { path: 'api/posts/:postTypeID/:postID/comments/page/1', component: PostCommentsComponent },
  { path: 'api/posts/:postTypeID/:postID/likes/page/1', component: PostLikesComponent },
  { path: 'api/users/page/:page', component: UsersComponent },
  { path: 'api/userProfile/:userID', component: UserProfileComponent },
  { path: 'api/userProfile/:userID/posts/page/:page', component: UserProfileComponent },
  { path: 'api/messages/:userID/page/:page', component: MessagesComponent },
  { path: 'api/messages/:userID/newMessage', component: MessagesComponent },
  { path: 'api/messages/:userID/:messageThreadID/page/:page', component: MessagesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
