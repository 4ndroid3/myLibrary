import { Component, OnInit } from '@angular/core';
import { MybooksService } from 'src/app/mybooks/services/mybooks.service';

@Component({
  selector: 'app-list-mybooks-page',
  templateUrl: './list-mybooks-page.component.html',
  styleUrls: ['./list-mybooks-page.component.scss']
})
export class ListMybooksPageComponent implements OnInit {

  constructor(private myBooksService: MybooksService) { }

  ngOnInit(): void {
    let params = {}
    this.myBooksService.getMyBooks(params)
      .subscribe( books => console.log(books))
  }

}
