import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, FormBuilder, Validators} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  email=  new FormControl('', [Validators.required, Validators.email]);
  teacherid = new FormControl('', [Validators.required, Validators.pattern(/^[A-Z]{1,4}\d{6}$/)]);
  password=  new FormControl('', [Validators.required, Validators.pattern(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/)]);

  hide = true;


  constructor(private http: HttpClient) {
   }

  ngOnInit(): void {
  }

  onSubmit()
  {
    var formData: any = {};
    formData["email"] = this.email.value;
    formData["teacherid"] = this.teacherid.value;
    formData["password"] = this.password.value;
    this.http.post('http://localhost:4433/signup', formData).subscribe(
    (response) => console.log(response),
    (error) => console.log(error)
  )
    
  }

  getEmailError() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }
    return this.email.hasError('email') ? 'Not a valid email' : '';
    
  }

  getTeacherIDError()
  {
    if (this.teacherid.hasError('required')) {
      return 'You must enter a value';
    }
    return this.teacherid.hasError('pattern') ? 'Not a valid teacher id' : '';

  }

  getPasswordError()
  {
    if (this.password.hasError('required')) {
      return 'You must enter a value';
    }
     return this.password.hasError('pattern') ? 'Not a valid password' : '';
  }

}
