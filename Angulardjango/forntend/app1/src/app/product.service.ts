import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http : HttpClient) { }

   


}
