import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateMybooksPageComponent } from './pages/mybooks/create-mybooks-page/create-mybooks-page.component';
import { ListMybooksPageComponent } from './pages/mybooks/list-mybooks-page/list-mybooks-page.component';
import { MybooksComponent } from './pages/mybooks/mybooks.component';

const routes: Routes = [
    {
      path: '',
      component: MybooksComponent,
      children: [
        {
          path: 'listado',
          component: ListMybooksPageComponent,
        },
        {
          path: 'creacion',
          component: CreateMybooksPageComponent,
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
  export class MyBooksRoutingModule { }
  