import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { map, switchMap, tap } from 'rxjs';
import { Autor, Libro } from 'src/app/books/interfaces/book';
import { MiLibro } from '../../interfaces/my-book';
import { MybooksService } from '../../services/mybooks.service';
import {formatDate} from '@angular/common';

@Component({
  selector: 'app-mybooks',
  templateUrl: './mybooks.component.html',
  styleUrls: ['./mybooks.component.scss']
})
export class MybooksComponent implements OnInit {


  current_date = formatDate(new Date(), 'yyyy-MM-dd', 'en');
  libros!: MiLibro[];
  autores: Autor[] = [];
  total_hojas: number = 0;
  total_libros: number = 0;
  total_autores: number = 0;
  filtros = this.fb.group({
    fecha_leido_mayor: [ '' ],
    fecha_leido_menor: [ this.current_date ],
  })

  constructor(private myBooksService: MybooksService,
              private fb: FormBuilder) { }

  ngOnInit(): void {
    this.buscar()

  }

  buscar() {
    this.autores      = [];
    this.total_hojas  = 0;
    this.total_libros = 0;
    this.total_autores = 0;
    const params = {
      fecha_leido_mayor: this.filtros.value['fecha_leido_mayor'],
      fecha_leido_menor: this.filtros.value['fecha_leido_menor']
    }
    this.myBooksService.getMyBooks( params )
    .pipe(
      map(t => t.results ),
      tap( (libros: MiLibro[]) => {

        libros.forEach(libro => {
          this.total_hojas += libro.libro?.hojas
          
          const autor = this.autores?.find( autor => {
            return autor.id === libro?.libro?.autor?.id;
          })          
          if (!autor) {
            this.autores?.push(libro?.libro?.autor);
          }
          
        });
        this.total_libros = libros.length
        this.total_autores = this.autores.length;
      } )
      )
      .subscribe( libros => {
        this.libros = libros
      })
  }

}
