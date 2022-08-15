import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from '../material/material/material.module';
import { MybooksComponent } from './pages/mybooks/mybooks.component';
import { CreateMybooksPageComponent } from './pages/mybooks/create-mybooks-page/create-mybooks-page.component';
import { ListMybooksPageComponent } from './pages/mybooks/list-mybooks-page/list-mybooks-page.component';
import { EstanteriasComponent } from './pages/estanterias/estanterias.component';
import { MyBooksRoutingModule } from './mybooks-routing.module';
import { MybooksService } from './services/mybooks.service';
import { MyBookBoxComponent } from './components/my-book-box/my-book-box.component';
import { ImagenPipe } from './pipes/imagen.pipe';



@NgModule({
  declarations: [
    MybooksComponent,
    CreateMybooksPageComponent,
    ListMybooksPageComponent,
    EstanteriasComponent,
    MyBookBoxComponent,
    ImagenPipe
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MaterialModule,
    MyBooksRoutingModule
  ],
  providers: [MybooksService],
})
export class MyBooksModule { }
