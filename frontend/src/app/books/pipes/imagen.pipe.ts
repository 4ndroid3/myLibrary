import { Pipe, PipeTransform } from '@angular/core';
import { Libro } from '../interfaces/book';

@Pipe({
  name: 'imagen'
})
export class ImagenPipe implements PipeTransform {

  transform(libro: Libro): string {
    if (!libro.img_cover) {
      return 'assets/no-image.png';
    } else {
      return libro.img_cover
    }
  }
}
