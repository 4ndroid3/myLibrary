import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor( private http: HttpClient ) { }

  get() {
    return this.http.get<any>('http://127.0.0.1:8000/api/',)
  }
}
