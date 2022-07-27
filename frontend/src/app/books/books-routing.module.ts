import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BooksComponent } from './pages/books/books.component';
import { CreateBooksPageComponent } from './pages/books/create-books-page/create-books-page.component';
import { ListBooksPageComponent } from './pages/books/list-books-page/list-books-page.component';

const routes: Routes = [
    {
      path: '',
      component: BooksComponent,
      children: [
        {
          path: 'listado',
          component: ListBooksPageComponent,
        },
        {
          path: 'creacion',
          component: CreateBooksPageComponent,
        },
        {
          path: '**',
          redirectTo: '',
        }
      ]
    }
  ]
  
  
  @NgModule({
    imports: [
      RouterModule.forChild( routes )
    ],
    exports: [
      RouterModule
    ]
  })
  export class BooksRoutingModule { }
  