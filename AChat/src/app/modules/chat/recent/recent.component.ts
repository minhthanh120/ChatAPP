import { Component, OnInit } from '@angular/core';
import { AuthorizeService } from 'src/app/services/authorize.service';
import { SpinnerService } from 'src/app/services/spinner.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-recent',
  templateUrl: './recent.component.html',
  styleUrls: ['./recent.component.css']
})
export class RecentComponent implements OnInit {
  /**
   *
   */
  public recentMessage: any;
  constructor(public spinnerService:SpinnerService, private authorize: AuthorizeService, private userService: UserService) {

  }
  ngOnInit() {
    let token = localStorage.getItem(this.authorize.token);
    let object_token = JSON.parse(token!)
    const access_token = object_token.access_token;
    this.userService.getRecentMessage(access_token).subscribe();
  }
}
