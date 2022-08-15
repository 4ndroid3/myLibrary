import { Component, OnInit } from '@angular/core';
import { MybooksService } from 'src/app/mybooks/services/mybooks.service';
import { MiLibro } from 'src/app/mybooks/interfaces/my-book';
import { map } from 'rxjs';

@Component({
  selector: 'app-list-mybooks-page',
  templateUrl: './list-mybooks-page.component.html',
  styleUrls: ['./list-mybooks-page.component.scss']
})
export class ListMybooksPageComponent implements OnInit {

  misLibros!: MiLibro[];

  constructor(private myBooksService: MybooksService) { }

  ngOnInit(): void {
    let params = {}
    this.myBooksService.getMyBooks(params)
      .pipe(
        map(t => t.results )
      )
      .subscribe(       
        (t: MiLibro[]) => { 
          this.misLibros = t;
        }
      )
  }
}
