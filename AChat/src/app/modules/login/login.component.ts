import { Component, Injectable, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { first } from 'rxjs';
import { Config } from 'src/app/interface/config';
import { Login } from 'src/app/interface/login';
import { AuthorizeService } from 'src/app/services/authorize.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
@Injectable()
export class LoginComponent implements OnInit {
  //login: boolean | undefined;
  submitted = false;
  user!: FormGroup;
  //res:any ="";
  constructor(private authorize: AuthorizeService, private router:Router) {

  }
  ngOnInit(): void {
    var usr = localStorage.getItem(this.authorize.user);
    if(usr != null){
      this.router.navigate(['']);
      //return;
    }
    console.log(usr);
    this.user = new FormGroup({
      email:new FormControl<string>('', {nonNullable:true}),
      password:new FormControl<string>('', {nonNullable:true}),
    });
  }
  onSubmit(){
    this.submitted=true;
  }
  login(data:any){
    //this.router.navigate[''];
    console.log(data);
    this.authorize.login(data).pipe(first())
    .subscribe({
      next:()=>{
        this.router.navigate(['']);
      },
      error:error=>{
        console.log(error);
      }
    })
  }
  toIndex(){
    //this.authorize.isLoggedIn = true;
  }
}
