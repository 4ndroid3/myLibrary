import { Component } from '@angular/core';
import { HttpService } from './shared/services/http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Frontend';
  raul = 'a';

  constructor(private httpS: HttpService) {  }
  
  prueba() {
    this.httpS.get().subscribe(
      t => { console.log(t),
      this.raul = t;}
    )
  }

}
