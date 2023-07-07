import { Component, OnInit } from '@angular/core';
import { Group } from 'src/app/interface/models';
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
  contact=true;
  group = false;
  groupsmessage:Group[] = [
    {id:"a", groupName:"Nguyễn Van A", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"b", groupName:"Nguyễn Van B", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"d", groupName:"Nguyễn Van C", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"e", groupName:"Nguyễn Van D", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"f", groupName:"Nguyễn Van F", createdTime:"", creatorId:null, members:null, messages:null},
  ]
  usersmessage:Group[] = [
    {id:"a", groupName:"Nguyễn Van X", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"b", groupName:"Nguyễn Van Y", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"d", groupName:"Nguyễn Van Z", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"e", groupName:"Nguyễn Van 1", createdTime:"", creatorId:null, members:null, messages:null},
    {id:"f", groupName:"Nguyễn Van 2", createdTime:"", creatorId:null, members:null, messages:null},
  ]

  public recentMessage: any;
  constructor(public spinnerService:SpinnerService, private authorize: AuthorizeService, private userService: UserService) {

  }
  ngOnInit() {
    let token = localStorage.getItem(this.authorize.token);
    let object_token = JSON.parse(token!)
    const access_token = object_token.access_token;
    this.userService.getRecentMessage(access_token).subscribe();
  }
  switchTab(event:Event){
    if((event.target as Element).id === 'group'){
      if(!this.group){
        this.group = true;
        this.contact = false;
      }
    }
    else if((event.target as Element).id === 'contact'){
      if(!this.contact){
        this.group = false;
        this.contact = true;
      }
    }
  }
}
