import { Component, OnInit, ElementRef, ViewChild, Renderer2 } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from 'src/app/interface/user';
import { AuthorizeService } from 'src/app/services/authorize.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  isShow = false;
  haveName = false;
  user: any;
  openAddGroup = false;
  openSearch = false;
  public groupId!: string;
  public idGroup:string = "";
  popup = true;
  isSearching = false;
  /**
   *
   */
  constructor(private authorize: AuthorizeService, private userService: UserService, private router: Router) {
    //this.ngOnInit();
  }
  ngOnInit(): void {
    if (localStorage.getItem(this.authorize.token) != undefined) {
    }
    else{
      console.log('not authorize');
      this.router.navigate(['/login']);
    }

  }

  logOutOnclick() {
    this.authorize.logOut();
    this.router.navigate(['/login']);
  }
  openmenu() {
    if (this.isShow) {
      this.isShow = false;
    }
    else {
      this.isShow = true;
    }
  }
  formAddGroup() {
    this.openAddGroup = !this.openAddGroup;
  }
  clickSearching(){
    this.isSearching = true;
    this.popup = !this.popup
  }
  outSearching(){
    this.isSearching = false;
  }
}
