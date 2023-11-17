import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-job-post',
  templateUrl: './job-post.component.html',
  styleUrls: ['./job-post.component.css']
})

export class JobPostComponent implements OnInit {
  currentPage: number = 1;
  postTypeID: number= 2;

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
