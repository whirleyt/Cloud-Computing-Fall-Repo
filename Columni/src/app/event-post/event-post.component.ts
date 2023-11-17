import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-event-post',
  templateUrl: './event-post.component.html',
  styleUrls: ['./event-post.component.css']
})
export class EventPostComponent implements OnInit {
  currentPage: number = 1;
  postTypeID: number= 3;

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
