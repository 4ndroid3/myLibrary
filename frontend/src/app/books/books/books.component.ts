import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs';
import { LibroMin } from '../interfaces/book';
import { BooksService } from '../services/books.service';

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {

  title = 'Frontend';
  raul?: LibroMin[];

  constructor(private booksS: BooksService) {  }
  


  ngOnInit(): void {
    this.booksS.getBooks()
    .pipe(
      map(t => t.results )
    )
    .subscribe(
      (t: LibroMin[]) => { console.log(t)
      this.raul = t;
    }
    )
  }

}
