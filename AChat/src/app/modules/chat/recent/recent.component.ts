import { Component, OnInit } from '@angular/core';
import { Route, Router } from '@angular/router';
import { SpinnerService } from 'src/app/services/spinner.service';

@Component({
  selector: 'app-recent',
  templateUrl: './recent.component.html',
  styleUrls: ['./recent.component.css']
})
export class RecentComponent implements OnInit {
  constructor(private router:Router, public spinnerService:SpinnerService){}
  ngOnInit(): void {
    this.currentTab = 'tab-1';
  }
  currentTab :any;
  onSelect(message: string=''){
    this.router.navigate(['/message', message])
  }
  switchTab(event:any){
    var target = event.currentTarget;
    this.currentTab = target.id;;
  }
  compareTab(tab:any){
    if(this.currentTab === tab){
      return true;
    }
    return false;
  }
}
