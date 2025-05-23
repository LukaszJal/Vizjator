import { Component } from '@angular/core';
import { DiagramService } from 'src/app/core/services/diagram.service';

@Component({
  selector: 'app-generator',
  templateUrl: './generator.component.html',
  styleUrls: ['./generator.component.scss']
})
export class GeneratorComponent {
  description = '';
  modelType = 'BPMN';
  modelTypes = ['BPMN', 'UML_USE_CASE', 'UML_CLASS', 'UML_SEQUENCE'];
  result: any;

  constructor(private diagramService: DiagramService) {}

  generate() {
    this.diagramService.generateDiagram({
      description: this.description,
      model_type: this.modelType
    }).subscribe(res => {
      this.result = res;
    });
  }
}