import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map, pipe } from 'rxjs';
import { enviroment } from 'src/assets/enviroments';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  public user: any;
  constructor(private http: HttpClient) { }

  getCurrentUser(token: string) {
    const subdomain = '/user';
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token.toString()
      })
    };
    return this.http.get<any>(enviroment.backendServer + subdomain, httpOptions)
      .pipe(map((res) => { 
        localStorage.setItem("user", JSON.stringify(res));
        return res;
      }));
  }

  updateUserInfo(userInfo:any){
    const subdomain1 = '/user';
    const subdomain2 = '/edit';
    return this.http.post<any>(enviroment.backendServer+subdomain1+subdomain2, userInfo)
    .pipe(map(
      (res)=>{
        if(res.detail == undefined)
          {
            console.log(res);
            localStorage.removeItem("user")
          }
      }
    ))
  }
}
