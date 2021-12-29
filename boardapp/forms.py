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
    date_posted = forms.DateField(widget=DateInput)
    class Meta:
        model = Flyer
        fields = ('board', 'office', 'name', 'image', 'date_posted', 'due_date')
    
  
    board = forms.ModelMultipleChoiceField(
        queryset=Board.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['board'].widget.attrs.update(
            {'class': 'boards-checkbox', 'placeholder': 'Username'})

    

    username = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))




  
class AddOfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'location', 'image')
