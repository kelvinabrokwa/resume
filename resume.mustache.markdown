# {{firstName}} {{lastName}}

## Experience
{{#experience}}
- ### [{{company}}]({{webpage}})
  {{position}}
  {{location}}
  Details
    {{#details}}
    - {{.}}
    {{/details}}
{{/experience}}

## Skills
{{#skills}}
- {{skill}}
  {{#items}}
  - {{.}}
  {{/items}}
{{/skills}}

## Education
{{#education}}
- {{school}}
  {{degree}}
  {{#details}}
  {{.}}
  {{/details}}
  Relevant Coursework
  {{#relevantCoursework}}
  - {{.}}
  {{/relevantCoursework}}
  {{^relevantCoursework}}
  - none
  {{/relevantCoursework}}
{{/education}}
