import { Component, Injectable, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
@Injectable()
export class UserComponent implements OnInit {
  /**
   *
   */
  currentUser!: FormGroup;
  constructor() {

  }
  ngOnInit(): void {
    this.currentUser = new FormGroup({
    id: new FormControl<string>(''),
    userName: new FormControl<string>(''),
    firstName: new FormControl<string>(''),
    lastName: new FormControl<string>(''),
    email: new FormControl<string>(''),
    avatar: new FormControl<string>(''),
    phone:new FormControl<string>('')
    })
  }
}
