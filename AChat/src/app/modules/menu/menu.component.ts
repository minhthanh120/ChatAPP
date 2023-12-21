import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthorizeService } from 'src/app/services/authorize.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  constructor(private userService: UserService, private authorize: AuthorizeService, private router:Router) {

  }
  ngOnInit(): void {
    if (localStorage.getItem(this.authorize.token) != undefined) {
      this.router.navigate(['/']);
      let token = localStorage.getItem(this.authorize.token);
      let object_token = JSON.parse(token!)
      const access_token = object_token.accessToken;
      this.userService.getCurrentUser(access_token).subscribe(data => {
        this.user = data;
        if (this.user.firstName != null && this.user.lastName != null) {
          this.haveName = true;
        }
      });
    }
    else {
      console.log('not authorize');
      this.router.navigate(['/login']);
    }
  }
  haveName = false;
  user: any;

  logOutOnclick() {
    this.authorize.logOut();
    this.router.navigate(['/login']);
  }
}
