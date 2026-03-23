from django.forms import CheckboxInput, ModelForm, TextInput, Textarea,  ValidationError
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   
    class Meta:
            model = Snippet
            # Описываем поля, которые будем заполнять в форме
            fields = ['name', 'lang', 'code', 'public']
            labels = {"name": "", "lang": "", "code": "", "public": "Public(checked) / Private(unchecked)"}
            widgets = {
                "name": TextInput(attrs={
                    "class": "form-control",
                    "placeholder": "Название сниппета",
                    "style": "max-width: 400px"
                }),
                "code": Textarea(attrs={
                    "placeholder": "Код сниппета",
                    "rows": 5,
                    "class": "input-large",
                    'style': 'width: 50% !important; resize: vertical !important;'
                }),
                "public": CheckboxInput(attrs={"value": "True"})
            }

    def clean_name(self):
       """Метод для проверки длины поля"""
       snippet_name = self.cleaned_data.get('name')
       if snippet_name is  not None and len(snippet_name) >3:
           return snippet_name
       raise ValidationError('Snippets name too short.')
       
