import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class DiagramService {
  constructor(private http: HttpClient) {}

  generateDiagram(payload: any): Observable<any> {
    return this.http.post('/api/generate-diagram', payload);
  }
}