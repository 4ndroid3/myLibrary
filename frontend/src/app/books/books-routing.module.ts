import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BooksComponent } from './books/books.component';

const routes: Routes = [
    {
      path: '',
    //   component: HomeComponent,
      children: [
        {
          path: 'listado',
          component: BooksComponent,
        },
        {
          path: '**',
          redirectTo: 'listado',
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
  