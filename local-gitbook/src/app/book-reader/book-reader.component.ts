import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-book-reader',
  templateUrl: './book-reader.component.html',
  styleUrls: ['./book-reader.component.css']
})
export class BookReaderComponent implements OnInit {

  name='' as string;
  history='' as string;
  constructor( private route: ActivatedRoute, public sanitizer:DomSanitizer) { }
  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.name=params.get('bookname') as string;
      this.history=params.get('history') as string | '';
      console.log(this.name,this.history);
    });
  }

}
