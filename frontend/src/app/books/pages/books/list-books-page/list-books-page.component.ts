import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs';
import { Libro } from 'src/app/books/interfaces/book';
import { BooksService } from 'src/app/books/services/books.service';

@Component({
  selector: 'app-list-books-page',
  templateUrl: './list-books-page.component.html',
  styleUrls: ['./list-books-page.component.css']
})
export class ListBooksPageComponent implements OnInit {

  libros?: Libro[];

  constructor(private booksS: BooksService) {  }
  


  ngOnInit(): void {
    this.booksS.getBooks()
    .pipe(
      map(t => t.results )
    )
    .subscribe(
      (t: Libro[]) => { 
      this.libros = t;
    }
    )
  }

}
