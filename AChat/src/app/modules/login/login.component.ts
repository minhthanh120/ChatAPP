import { Component, Injectable, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
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
  login: boolean | undefined;
  submitted = false;
  user!: FormGroup;
  constructor(private authorizeService: AuthorizeService) {

  }
  ngOnInit(): void {
    this.user = new FormGroup({
      email:new FormControl<string>('', {nonNullable:true}),
      password:new FormControl<string>('', {nonNullable:true}),
    });
  }
  onSubmit(){
    this.submitted=true;
  }
  authorize(data:any){
    console.log(data)
    if(!data.email || !data.password){
      console.log(data.email+" "+data.password);
      return;
    }
    console.log("ok");
    this.authorizeService.login(data);
  }
}
