from django import forms

from .models import Comments, ServisClient, Bike

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['message', 'author']
        labels = {
            'message' : ('Komentarz'),
            'author' : ('Autor')
        }
        help_texts = {
            'message' : ('Napisz jak możemy ulepszyć nasz system!'),
            'author' : ('Podpisz się żebyśmy wiedzieli kogo szukać :)')
        }

class NewClientForm(forms.ModelForm):
    class Meta:
        model = ServisClient
        fields = ['name', 'phone', 'email', 'mikesz', 'other']

class NewBike(forms.ModelForm):
    class Meta:
        model = Bike
        #fields = '__all__'
        fields = ['name', 'owner', 'type', 'date_made', 'other']