import { Component, Input, OnInit } from '@angular/core';
import { BooksService } from 'src/app/books/services/books.service';
import { MiLibro } from '../../interfaces/my-book';

@Component({
  selector: 'app-my-book-box',
  templateUrl: './my-book-box.component.html',
  styleUrls: ['./my-book-box.component.scss']
})
export class MyBookBoxComponent implements OnInit {

  @Input() miLibro!: MiLibro;

  constructor(private bookService: BooksService) { }

  ngOnInit(): void {
    this.bookService.getGeneros({})
      .subscribe(
        e => console.log(e)
      )
  }

}
