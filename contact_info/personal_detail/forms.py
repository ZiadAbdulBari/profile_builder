from django import forms
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import FileField, ImageField
from django.forms import fields, widgets,DateInput
from personal_detail.models import AddContact

class AddContactForm(forms.ModelForm):
    
    class Meta:
        model = AddContact
        fields = "__all__"
        widgets={
            'name' : widgets.Input(attrs={'class':'form-control',}),
            'email': widgets.Input(attrs={'class':'form-control',}),
            'dob' : DateInput(attrs={'type':'date','class':'form-control'}),
            'contact_number' : widgets.Input(attrs={'class':'form-control',}),
            'gender' : widgets.RadioSelect(),
            'address' : widgets.Textarea(attrs={'cols': 20, 'rows': 2, 'class':'form-control'}),
            # 'image' :widgets.FileInput(attrs=({'type':'file','required': 'False'}))
        }
        