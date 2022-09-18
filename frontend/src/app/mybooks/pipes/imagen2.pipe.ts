import { Pipe, PipeTransform } from '@angular/core';
import { Libro } from 'src/app/books/interfaces/book';

@Pipe({
  name: 'imagen2'
})
export class Imagen2Pipe implements PipeTransform {

  transform(libro: Libro): string {
    if (!libro.img_cover) {
      return 'assets/no-image.png';
    } else {
      return libro.img_cover
    }
  }
}