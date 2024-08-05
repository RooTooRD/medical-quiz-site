from django import forms
from .models import Question, Choice

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['choice'] = forms.ModelChoiceField(
            queryset=question.choice_set.all(),
            widget=forms.CheckboxSelectMultiple,
            empty_label=None
        )
        
        # Create a dictionary of choices
        self.choice_dict = {choice.id: choice.text for choice in question.choice_set.all()}