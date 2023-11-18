import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-social-post',
  templateUrl: './social-post.component.html',
  styleUrls: ['./social-post.component.css']
})

export class SocialPostComponent implements OnInit {
  currentPage: number = 1;
  postTypeID: number = 1;
  pageSize: number  = 10;
  newPostContent: string = '';
  isPost: boolean = false;
  displayedPosts: any[] = [];

  posts = Array.from({ length: 30 }, (_, i) => ({
        postID: i + 1,
        userID: 1,
        firstName: 'Tara',
        lastName: 'Whirley',
        postTypeID: 1,
        postContent: `This is dummy post content for social post ${i + 1}`,
        creationDT: new Date().toISOString()
  }));

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.currentPage = +params['page'] || 1;
      this.fetchPosts();
      this.getDummyPosts();
    });
  }

  fetchPosts(): void {
    console.log("postTypeID:"+ this.postTypeID+", page:"+ this.currentPage);
  }

  getDummyPosts() {
        const startIndex = (this.currentPage - 1) * this.pageSize;
        const endIndex = startIndex + this.pageSize;
        return this.displayedPosts = this.posts.slice(startIndex, endIndex);
  }

  createPost() {
      this.isPost= !this.isPost;
    }

    savePost(){
      console.log("new post content: "+ this.newPostContent);
    }
}
