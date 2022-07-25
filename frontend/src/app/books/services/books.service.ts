import { Injectable } from '@angular/core';
import { HttpService } from 'src/app/shared/services/http.service';

@Injectable({
  providedIn: 'root'
})
export class BooksService {

  constructor(private http: HttpService) { }

  getBooks() {
    this.http.get()
  }
}
