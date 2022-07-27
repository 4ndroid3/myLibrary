import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BooksService } from './services/books.service';
import { BooksComponent } from './pages/books/books.component';
import { AutoresComponent } from './pages/autores/autores.component';
import { GenerosComponent } from './pages/generos/generos.component';
import { BooksRoutingModule } from './books-routing.module';
import { CreateBookFormComponent } from './components/create-book-form/create-book-form.component';
import { ListBooksPageComponent } from './pages/books/list-books-page/list-books-page.component';
import { CreateBooksPageComponent } from './pages/books/create-books-page/create-books-page.component';
import { ReactiveFormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    BooksComponent,
    AutoresComponent,
    GenerosComponent,
    CreateBookFormComponent,
    ListBooksPageComponent,
    CreateBooksPageComponent
  ],
  imports: [
    CommonModule,
    BooksRoutingModule,
    ReactiveFormsModule
  ],
  providers: [BooksService],
})
export class BooksModule { }
