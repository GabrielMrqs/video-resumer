import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {
  private API_URL = 'http://localhost:5000/api/resume';

  constructor(private http: HttpClient) { }

  getResume(url: string): Observable<string> {
    return this.http.get<string>(`${this.API_URL}/${url}`);
  }
}