from django import forms


class Studentform(forms.Form):
    first_name =forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={'class':'from-control'})
        )
    last_name =forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={'class':'from-control'})
        )
    email =forms.CharField(
        max_length=255,
        widget= forms.TextInput(attrs={'class':'from-control'})
        )
    image = forms.FileField(required= False) 
    
    