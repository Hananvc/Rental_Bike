
from django import forms 
from .models import Booking
from .models import users



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'

     
        labels = {
            'Name' :'Name: ',
            'Phone' : 'Phone: ',
            'Email' : 'E-mail: ',
            'Model' :'Model: ',
            
        }

class formupdation(forms.ModelForm):
        class Meta:
            model = users
            fields = ['username','email','first_name']
            widgets= {
                'username' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
                'email': forms.TextInput(attrs={'class' : 'form-control col-3'}),
                'first_name': forms.TextInput(attrs={'class' : 'form-control col-3'}),
                
                }
        





