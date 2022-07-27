import { Component, OnInit } from '@angular/core';
import { Libro } from '../../interfaces/book';
import { BooksService } from '../../services/books.service';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-create-book-form',
  templateUrl: './create-book-form.component.html',
  styleUrls: ['./create-book-form.component.css']
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
  constructor(private bService: BooksService) {}

  ngOnInit(): void {
  }
  
  onSubmit() {
    this.createdData = this.formBook.value
    this.bService.createBooks(this.createdData).subscribe()
    this.formBook.reset()
  }



}
