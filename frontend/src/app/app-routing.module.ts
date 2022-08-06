import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'libros',
    loadChildren: () => import('./books/books.module').then( m => m.BooksModule )
  },
  {
    path: 'mislibros',
    loadChildren: () => import('./mybooks/mybooks.module').then( m => m.MyBooksModule )
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
