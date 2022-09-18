import { Component, OnInit } from '@angular/core';
import { Autor, Libro } from '../../interfaces/book';
import { BooksService } from '../../services/books.service';
import { FormGroup, FormControl } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { map } from 'rxjs';

@Component({
  selector: 'app-create-book-form',
  templateUrl: './create-book-form.component.html',
  styleUrls: ['./create-book-form.component.scss']
})
export class CreateBookFormComponent implements OnInit {

  createdData: object = {}
  libro?: Libro;
  
  formBook = new FormGroup({
    autor_id: new FormControl(''),
    genero_id: new FormControl(''),
    nombre: new FormControl(''),
    anio_publicacion: new FormControl(''),
    hojas: new FormControl(''),
  })

  autores!: Autor[]
  autorSeleccionado!: Autor | undefined;
  termino: string = '';

  generosList: string[] = ['Autoayuda', 'Aventura', 'CienciaFicción', 'Fantasía', 'Heroica', 'Thriller', 'Suspenso', 'Terror', 'Novela', 'Western', 'Historia'];
  generosDict = new Map([
    ['Autoayuda', 17],
    ['Aventura', 16],
    ['CienciaFicción', 15],
    ['Fantasía', 19],
    ['Heroica', 25],
    ['Thriller', 18],
    ['Suspenso', 20],
    ['Terror', 21],
    ['Novela', 22],
    ['Western', 23],
    ['Historia', 24],
  ])
  
  generosId: any = []

  constructor(private bService: BooksService,) {}

  ngOnInit(): void {
  
  }
  
  onSubmit() {
    this.formBook.controls['autor_id'].setValue(this.autorSeleccionado!.id.toString())
    this.convertirGeneroId(this.formBook.value['genero_id']);
    this.formBook.controls['genero_id'].setValue(this.generosId)
    this.createdData = this.formBook.value
    this.bService.createBooks(this.createdData).subscribe()
    this.formBook.reset()
  }

  buscando() {
    let params = {
      nombre: this.formBook.value['autor_id']
    }
    this.bService.getAutors( params )
      .pipe(
        map(t => t.results )
      )
      .subscribe( autores => this.autores = autores )
    console.log(this.termino)
  }

  opcionSeleccionada( event: MatAutocompleteSelectedEvent) {
    if (!event.option.value) {
      this.autorSeleccionado = undefined;
      return;
    }

    const autor: Autor = event.option.value;
    this.termino = autor.nombre;

    this.bService.getAutor( autor.id )
      .subscribe( autor => {
        this.autorSeleccionado = autor;
      });
  }

  convertirGeneroId(generosSelec: any) {
    if (generosSelec.length > 0) {
      
      for (let entry of this.generosDict.entries()) {
        generosSelec.forEach((element:any) => {
          if (entry[0] === element) {
            this.generosId.push(entry[1])
          }
        });
      }
    }
  } 



}
