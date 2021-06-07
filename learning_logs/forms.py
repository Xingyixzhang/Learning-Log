from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm): # class TopicForm inherits ModelForm
    class Meta:     # tells django which model to base the form on and which fields to include in the form.
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # widgets attribute:
        # a widget is a HTML form element. Included to override Gjango's default widget choices.
        # Textarea element customizes the input widget for the field 'text' so the text area would be 80 columns wide instead of the default 40 to allow user enough room to write meaningful entries.
