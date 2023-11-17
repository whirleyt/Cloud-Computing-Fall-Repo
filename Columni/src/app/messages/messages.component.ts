import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
// import { MessageService } from './message.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})

export class MessagesComponent implements OnInit {
  currentPage: number = 1;
  userID: number = 1;
  messages: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private router: Router
//     ,
//     private messageService: MessageService
  ) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.currentPage = +params['page'] || 1;
      this.fetchPosts();
    });
  }

  fetchPosts(): void {
    console.log("userID:" + this.userID + ", page:" + this.currentPage);
//     this.messageService.getMessages(this.userID, this.currentPage)
//       .subscribe((data: any) => {
//         this.messages = data;
//       },
  }

  navigateToPage(page: number): void {
    this.router.navigate(['../', page], { relativeTo: this.route, queryParams: { userID: this.userID } });
  }
}
