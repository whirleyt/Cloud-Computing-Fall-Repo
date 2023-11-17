// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';
//
// @Injectable({
//   providedIn: 'root'
// })
// export class MessageService {
//   private apiUrl = 'https://messages-microservice.ue.r.appspot.com/';
//
//   constructor(private http: HttpClient) { }
//
//   getMessages(userID: number, page: number): Observable<any> {
//        const url = `${this.apiUrl}/api/messages/${userID}?page=${page}`;
//        return this.http.get(url);
//   }
// }
