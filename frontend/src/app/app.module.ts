import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';
import { BooksComponent } from './books/books/books.component';
import { AutoresComponent } from './books/autores/autores.component';
import { GenerosComponent } from './books/generos/generos.component';

@NgModule({
  declarations: [
    AppComponent,
    BooksComponent,
    AutoresComponent,
    GenerosComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
