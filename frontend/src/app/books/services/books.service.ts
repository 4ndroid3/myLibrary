import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpService } from 'src/app/shared/services/http.service';
import { Libro } from '../interfaces/book';

@Injectable({
  providedIn: 'root'
})
export class BooksService {

  constructor(private http: HttpService) { }

  getBooks(param: {}): Observable<any>{
    return this.http.get('books/libros/', param);
  }

  createBooks(data: object = {}) {
    return this.http.post(`books/libros/`, data);
  }

  getAutors(param: {}): Observable<any> {
    return this.http.get('books/autores/', param);
  }

  getAutor(id: number): Observable<any> {
    return this.http.get(`books/autores/${id}`);
  }
}
