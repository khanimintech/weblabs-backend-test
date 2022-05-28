from email import message
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ad..'    

    })) 
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Soyad..'    

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'nümunə@gmail.com'    

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Mesaj...'    

    }))

    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'message']
