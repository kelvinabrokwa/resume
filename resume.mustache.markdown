# {{firstName}} {{lastName}}

{{email}}

{{phone}}

{{address}}

## Experience
{{#experience}}
### [{{company}}]({{webpage}})
  **{{position}}**, {{location}}

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
- #### [{{school}}]({{url}})

  {{degree}}

  {{#details}}
  - {{.}}
  {{/details}}

  Relevant Coursework
  {{#relevantCoursework}}
  - {{.}}
  {{/relevantCoursework}}
  {{^relevantCoursework}}
  {{/relevantCoursework}}

{{/education}}

## Research
{{#research}}
- {{.}}
{{/research}}


## Languages
{{#spokenLanguages}}
- {{.}}
{{/spokenLanguages}}

## Interests
{{#interests}}
  - {{.}}
{{/interests}}
