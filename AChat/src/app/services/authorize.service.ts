import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, delay, retry, map } from 'rxjs/operators';
import { Login } from '../interface/login';
import { HttpErrorHandler, HandleError } from './http-error-handler.service';
import { enviroment } from 'src/assets/enviroments';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': '*',
    'key': 'x-api-key',
  })
};
@Injectable({
  providedIn: 'root'
})
export class AuthorizeService {
  subdomain:string = "/login"
  isLoggedIn: boolean = false;
  responseStatus: number = 0;
  //private handleError: HandleError;
  constructor(private http: HttpClient,) {
    //this.handleError = httpErrorHandler.createHandleError('AuthorizeService');
  }


  login(login: Login) {
    this.http.post<Login>(enviroment.backendServer+this.subdomain, login, { observe: 'response' })
    .subscribe(
      (data: HttpResponse<any>) => {
        console.log(data.body.status_code);
      },
      (err: HttpErrorResponse) => {
          retry(3);
          console.error('403 status code caught');
      },
    );
  }
}
