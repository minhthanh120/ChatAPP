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
  //isLoggedIn: boolean = false;
  response: string = '';
  public user: any | undefined;
  //private handleError: HandleError;
  constructor(private http: HttpClient,) {
    //this.handleError = httpErrorHandler.createHandleError('AuthorizeService');
  }


  login(login: Login) {
    return this.http.post<any>(enviroment.backendServer+this.subdomain, login)
    .pipe(
      map((user) =>{
        localStorage.setItem(this.user, JSON.stringify(user));
        console.log(localStorage.getItem(this.user));
        //this.isLoggedIn= true;
        return user;
      })
    )
  }
  logOut(){
    localStorage.removeItem(this.user);
  }

  // GetUserName() {
  //   this.http.post<Login>(enviroment.backendServer + this.subdomain, this.login, {responseType: 'text'}).subscribe(result => {
  //     sessionStorage.setItem("UserName", result);
  //     alert(sessionStorage.getItem("UserName"));
  //   }, error => console.log(error));}
}
