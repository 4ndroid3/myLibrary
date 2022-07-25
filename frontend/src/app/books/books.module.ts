import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BooksService } from './services/books.service';
import { BooksComponent } from './books/books.component';
import { AutoresComponent } from './autores/autores.component';
import { GenerosComponent } from './generos/generos.component';
import { BooksRoutingModule } from './books-routing.module';



@NgModule({
  declarations: [
    BooksComponent,
    AutoresComponent,
    GenerosComponent
  ],
  imports: [
    CommonModule,
    BooksRoutingModule
  ],
  providers: [BooksService],
})
export class BooksModule { }
