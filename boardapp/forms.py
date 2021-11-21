from django import forms
from django.forms import widgets

from .models import Board, Flyer, Office


class FlyerPostedForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [ ]
        # exclude = ['status',]

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AddFlyerForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Flyer
        fields = ('board', 'office', 'name', 'image', 'due_date')
    
  
    board = forms.ModelMultipleChoiceField(
        queryset=Board.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


  
class AddOfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'location', 'image')
