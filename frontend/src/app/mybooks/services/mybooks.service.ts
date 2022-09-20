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

  getMyBook( id: number ) {
    return this.http.get(`user-books/libros/${id}/`);
  }

  createMyBooks(data: object = {}) {
    return this.http.post(`user-books/libros/`, data);
  }

  getEstantes(param: {}): Observable<any>{
    return this.http.get('user-books/estanterias/', param);
  }

  getEstante( id: number ) {
    return this.http.get(`user-books/estanterias/${id}/`);
  }

  createEstante(data: object = {}) {
    return this.http.post(`user-books/estanterias/`, data);
  }


}
