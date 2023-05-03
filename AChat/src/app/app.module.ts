import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './modules/login/login.component';
import { RegisterComponent } from './modules/register/register.component';
import { FooterComponent } from './shared/footer/footer.component';
import { HeaderComponent } from './shared/header/header.component';
import { ChatComponent } from './modules/chat/chat.component';
import { MessageComponent } from './modules/chat/message/message.component';
import { HttpClientModule } from '@angular/common/http';
import { ConfigComponent } from './modules/config/config.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthorizeService } from './services/authorize.service';
import { UserComponent } from './modules/user/user.component';
import { AppRoutingModule } from './app-routing.module';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    FooterComponent,
    HeaderComponent,
    ChatComponent,
    MessageComponent,
    ConfigComponent,
    UserComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
  ],
  providers: [
    AuthorizeService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
