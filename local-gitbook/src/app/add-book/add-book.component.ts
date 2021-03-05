import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-add-book',
  templateUrl: './add-book.component.html',
  styleUrls: ['./add-book.component.css']
})
export class AddBookComponent implements OnInit {

  constructor(private http:HttpClient) { }

  ngOnInit(): void {
    let itv=setInterval(()=>this.http.get('addBook',{responseType:'text',observe:'body'}).subscribe(
      (data)=>{
        this.serverProgress=data;
        if(data==''){
          clearInterval(itv);
        }
      }
      ),500);
  }
  book={
    name:'',
    url:'',
    description:''
  };
  onSubmit(){
    console.log('addbook',this.book);
    this.http.post('addBook', JSON.stringify(this.book), {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).subscribe(
    );
    history.go(-1);
  }
  cancel(){history.go(-1);}
  serverProgress='';
}