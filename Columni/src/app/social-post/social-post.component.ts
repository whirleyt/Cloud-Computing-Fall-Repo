import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-social-post',
  templateUrl: './social-post.component.html',
  styleUrls: ['./social-post.component.css']
})
export class SocialPostComponent implements OnInit {
  currentPage: number = 1;
  postTypeID: number= 1;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.currentPage = +params['page'] || 1;
      this.fetchPosts();
    });
  }

  fetchPosts(): void {
    console.log("postTypeID:"+ this.postTypeID+", page:"+ this.currentPage);
  }
}
