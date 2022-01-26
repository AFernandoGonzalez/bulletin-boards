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
        fields = ( 'board', 'office', 'name', 'image', 'removed', 'date_posted', 'due_date', 'flyer_creator', 'flyer_edited' , 'date_posted' )

    board = forms.ModelMultipleChoiceField(
        queryset=Board.objects.all(),
        required=True,
        help_text="Select the parent article (if any)",
        widget=forms.CheckboxSelectMultiple,   
    )


  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['board'].required = True
        self.fields['office'].required = True
        self.fields['name'].required = True
        self.fields['image'].required = True
        self.fields['date_posted'].required = True
        self.fields['due_date'].required = True

        self.fields['board'].widget.attrs.update(
            {'class': 'boards-checkbox required', 'placeholder': 'Choose Board', })
        
        self.fields['office'].widget.attrs.update(
            {'class': 'select-office', 'placeholder': 'Select Office'})
        
        self.fields['name'].widget.attrs.update(
            {'class': 'select-name', 'placeholder': 'Title of Flyer'})
        
        self.fields['image'].widget.attrs.update(
            {'class': 'select-image', 'placeholder': ''})
        
        self.fields['date_posted'].widget.attrs.update(
            {'class': 'select-posted_date', 'placeholder': ''})
        
        self.fields['due_date'].widget.attrs.update(
            {'class': 'select-due_date', 'placeholder': ''})


  
class AddOfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ('name', 'location', 'image')
        
