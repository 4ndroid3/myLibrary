import { Pipe, PipeTransform } from '@angular/core';
import { MiLibro } from '../interfaces/my-book';

@Pipe({
  name: 'imagen'
})
export class ImagenPipe implements PipeTransform {

  transform(miLibro: MiLibro): string {
    if (!miLibro.libro.img_cover) {
      return 'assets/no-image.png';
    } else {
      return miLibro.libro.img_cover
    }
  }

}
