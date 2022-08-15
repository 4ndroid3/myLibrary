import { Component, Input, OnInit } from '@angular/core';
import { map } from 'rxjs';
import { Libro } from 'src/app/books/interfaces/book';
import { BooksService } from 'src/app/books/services/books.service';

@Component({
  selector: 'app-book-box',
  templateUrl: './book-box.component.html',
  styleUrls: ['./book-box.component.scss']
})
export class BookBoxComponent implements OnInit {
  
  @Input() libro!: Libro;

  constructor() { }

  ngOnInit(): void {

  }

}
