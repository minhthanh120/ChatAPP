import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './modules/login/login.component';
import { RegisterComponent } from './modules/register/register.component';
import { ChatComponent } from './modules/chat/chat.component';
import { UserComponent } from './modules/user/user.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { MessageComponent } from './modules/chat/message/message.component';

const routes:Routes=[
  {path:'login', component:LoginComponent},
  {path:'register', component:RegisterComponent},
  {path:'', component:ChatComponent, children:[
    {path:'message/:id', component:MessageComponent},
  ]
},
  {path:'user', component:UserComponent},
  {path:'**', component:PagenotfoundComponent},
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes),
  ],
  exports:[RouterModule]
})
export class AppRoutingModule { }
