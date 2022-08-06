import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../material/material/material.module';
import { MybooksComponent } from './pages/mybooks/mybooks.component';
import { CreateMybooksPageComponent } from './pages/mybooks/create-mybooks-page/create-mybooks-page.component';
import { ListMybooksPageComponent } from './pages/mybooks/list-mybooks-page/list-mybooks-page.component';
import { EstanteriasComponent } from './pages/estanterias/estanterias.component';
import { MyBooksRoutingModule } from './mybooks-routing.module';



@NgModule({
  declarations: [
    MybooksComponent,
    CreateMybooksPageComponent,
    ListMybooksPageComponent,
    EstanteriasComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MaterialModule,
    MyBooksRoutingModule
  ],
  providers: [],
})
export class MyBooksModule { }
