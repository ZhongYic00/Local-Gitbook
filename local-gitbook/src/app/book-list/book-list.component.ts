import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export class Book implements Object{
  name: string;
  progress: string;
  cover: string;
  description: string;
  constructor(){
    this.name='';
    this.cover='';
    this.description='';
    this.progress='';
  }
}

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class BookListComponent implements OnInit {
  books = Array<Book>();
  constructor(private http:HttpClient) { }

  ngOnInit(): void {
    this.http.get('/books', {observe:'body', responseType: 'text'}).subscribe((data)=>this.books=JSON.parse(data));
  }

}
