from django import forms

from .models import Comments, ServisClient, Bike, Servis, Group


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['message', 'author']
        labels = {
            'message': ('Komentarz'),
            'author': ('Autor')
        }
        # help_texts = {
        #     'message': ('Napisz jak możemy ulepszyć nasz system!'),
        #     'author': ('Podpisz się żebyśmy wiedzieli kogo szukać :)')
        # }


class NewClientForm(forms.ModelForm):
    class Meta:
        model = ServisClient
        fields = ['name', 'phone', 'email', 'group', 'other']
        labels = {
            'name': 'nazwa',
            'phone': 'telefon',
            'email': 'email',
            'group': 'grupa',
            'other': 'inne',
        }


class NewBike(forms.ModelForm):
    class Meta:
        model = Bike
        # fields = '__all__'
        fields = ['mark', 'model', 'owner', 'type', 'year_made', 'other']
        labels = {
            'mark': 'producent',
            'model': 'model',
            'owner': 'właściciel',
            'type': 'typ',
            'year_made': 'rok produkcji',
            'other': 'inne'}


class NewServis(forms.ModelForm):
    class Meta:
        model = Servis
        # fields = '__all__'
        fields = ['date', 'status', 'bike', 'servis_range', 'other']
        labels = {'date':'data',
                  'status':'serwis zakończony',
                  'bike':'rower',
                  'servis_range':'zakres serwisu',
                  'other':'uwagi'}


class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'other']
        labels = {
            'name' : 'nazwa',
            'other' : 'opis'
        }
