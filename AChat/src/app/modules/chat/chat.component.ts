import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/app/interface/user';
import { AuthorizeService } from 'src/app/services/authorize.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  isShow = false;
  user:any;
  /**
   *
   */
  constructor(private authorize:AuthorizeService, private router:Router) {
  //this.ngOnInit();
  }
  ngOnInit(): void {
    if(localStorage.getItem(this.authorize.user) != undefined){
      this.router.navigate(['/']);
      this.user = localStorage.getItem(this.authorize.user);
      this.user = JSON.parse(this.user);
      console.log(this.user.email);
    }
    else{
      console.log('not authorize');
      this.router.navigate(['/login']);
    }

    //throw new Error('Method not implemented.');
  }

  logOutOnclick(){
    this.authorize.logOut();
    this.router.navigate(['/login']);
  }
  openmenu(){
    if(this.isShow){
      this.isShow = false;
    }
    else{
      this.isShow = true;
    }
  }
}
