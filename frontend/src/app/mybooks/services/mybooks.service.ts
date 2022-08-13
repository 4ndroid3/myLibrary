import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpService } from 'src/app/shared/services/http.service';

@Injectable({
  providedIn: 'root'
})
export class MybooksService {

  constructor(private http: HttpService) { }

  getMyBooks(param: {}): Observable<any>{
    return this.http.get('user-books/libros/', param);
  }

  createMyBooks(data: object = {}) {
    return this.http.post(`user-books/libros/`, data);
  }
}
