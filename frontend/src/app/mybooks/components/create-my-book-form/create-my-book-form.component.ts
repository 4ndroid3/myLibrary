import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { map } from 'rxjs';
import { Libro } from 'src/app/books/interfaces/book';
import { BooksService } from 'src/app/books/services/books.service';
import { MybooksService } from "src/app/mybooks/services/mybooks.service";

@Component({
  selector: 'app-create-my-book-form',
  templateUrl: './create-my-book-form.component.html',
  styleUrls: ['./create-my-book-form.component.scss']
})
export class CreateMyBookFormComponent implements OnInit {

  formMyBook = this.fb.group({
    libro_id: [ '', [Validators.required] ],
    estante_id: [ '' ],
    fecha_leido: [ '', [Validators.required] ],
  })

  libros: Libro[] = [];
  libroSeleccionado: Libro | undefined;
  termino: string = '';

  constructor( private fb: FormBuilder,
               private myBooksService: MybooksService,
               private booksService: BooksService) { }

  ngOnInit(): void {
  }

  

  guardar() {
    this.formMyBook.controls['libro_id'].setValue(this.libroSeleccionado!.id.toString())
    console.log(this.formMyBook.value)
    this.myBooksService.createMyBooks(this.formMyBook.value).subscribe(
      data => console.log(data)
    )
    console.log('Guardado')
    this.formMyBook.reset()
  }

  
  buscando() {
    let params = {
      nombre: this.formMyBook.value['libro_id']
    }
    this.booksService.getBooks( params )
    .pipe(
      map(t => t.results )
      )
      .subscribe( libros => {
        this.libros = libros
      })
    }

    opcionSeleccionada( event: MatAutocompleteSelectedEvent) {
      if (!event.option.value) {
        this.libroSeleccionado = undefined;
        return;
      }
  
      const libro: Libro = event.option.value;
      this.termino = libro.nombre;
  
      this.booksService.getBook( libro.id )
        .subscribe( libro => {
          this.libroSeleccionado = libro;
        });
    }

  }