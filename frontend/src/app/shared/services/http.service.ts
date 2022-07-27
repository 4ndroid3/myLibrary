import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor( private http: HttpClient ) { }

  private formatErrors(error: HttpErrorResponse) {
    return error;
  }

  private handleResponse(res: any) {
    return res;
  }

  get(path: string, params: object = {}): Observable<any> {
    return this.http
    .get<any>(
      `http://127.0.0.1:8000/api/${path}`,
      {
        params: this.setParams(params)
      })
  }

  post(path: string, body: Object = {}): Observable<any> {
    return this.http.post(
      `http://127.0.0.1:8000/api/${path}`,
      body
    )
  }

  setParams(params: object): HttpParams {
    let requestParams = new HttpParams();
    for (const [key, value] of Object.entries(params)) {
      requestParams = requestParams.set(key, value);
    }
    return requestParams;
  }
}
