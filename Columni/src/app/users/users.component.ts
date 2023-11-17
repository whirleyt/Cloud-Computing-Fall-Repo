import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  currentPage: number = 1;
  userID: number= 1;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.currentPage = +params['page'] || 1;
      this.fetchPosts();
    });
  }

  fetchPosts(): void {
    console.log("userID:"+ this.userID+", page:"+ this.currentPage);
  }
}
