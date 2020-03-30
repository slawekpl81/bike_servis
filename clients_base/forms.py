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

        widgets = {'date' :forms.SelectDateWidget()}

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'other']
        labels = {
            'name' : 'nazwa',
            'other' : 'opis'
        }

class SearchForm(forms.Form):

    search_name = 'nie określono'
    search_group = 'nie określono'
    search_mark = 'nie określono'
    search_model = 'nie określono'
    search_status = 'wszystkie'
    search_year = 0000

    STATUS_CHOICES = [
        (1, "wszystkie"),
        (2, "zakończone"),
        (3, "aktywne")
    ]
    all_clients = ServisClient.objects.all()
    all_clients_names = [(1, 'nie określono')]
    names = list(set([client.name for client in all_clients]))
    temp = [(number, name) for number, name in enumerate(names, start=2)]
    all_clients_names += temp

    all_groups = Group.objects.all()
    all_groups_names = [(1, 'nie określono')]
    temp = [(number, group.name) for number, group in enumerate(all_groups, start=2)]
    all_groups_names += temp

    all_bikes = Bike.objects.all()
    all_bikes_mark = [(1, 'nie określono')]
    all_bikes_model = [(1, 'nie określono')]
    marks = list(set([bike.mark for bike in all_bikes]))
    models = list(set([bike.model for bike in all_bikes]))
    temp = [(number, mark) for number, mark in enumerate(marks, start=2)]
    all_bikes_mark += temp
    temp = [(number, model) for number, model in enumerate(models, start=2)]
    all_bikes_model += temp

    #client_name = forms.CharField(label='nazwa klienta', max_length=100)
    client_name = forms.ChoiceField(choices=all_clients_names, label='klient')
    #group = forms.CharField(label='grupa', max_length=100)
    group_name = forms.ChoiceField(choices=all_groups_names, label='grupa')
    # bike_mark = forms.CharField(label='marka roweru', max_length=100)
    bike_mark = forms.ChoiceField(choices=all_bikes_mark, label='rower')
    # bike_model = forms.CharField(label='model', max_length=100)
    bike_model = forms.ChoiceField(choices=all_bikes_model, label='model')
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    year_of_servis = forms.CharField(label='rok serwisu', max_length=4, initial='****')

    def wyszukaj(self):
        for number, data in self.all_clients_names:
            if number == int(self['client_name'].value()):
                self.search_name = data

        for number, data in self.all_groups_names:
            if number == int(self['group_name'].value()):
                self.search_group = data