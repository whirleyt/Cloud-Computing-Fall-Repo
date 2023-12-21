import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  getMessages(userID: number, page: number): Observable<any> {
       const url = `${this.apiUrl}/api/messages/1`;
       return this.http.get(url);
  }
}
