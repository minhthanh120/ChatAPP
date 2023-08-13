import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-recent',
  templateUrl: './recent.component.html',
  styleUrls: ['./recent.component.css']
})
export class RecentComponent {
  constructor(private router:Router){}
  onSelect(message: string=''){
    this.router.navigate(['/message', message])
  }
}
