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
        labels = {'date': 'data',
                  'status': 'serwis zakończony',
                  'bike': 'rower',
                  'servis_range': 'zakres serwisu',
                  'other': 'uwagi'}

        widgets = {'date': forms.SelectDateWidget()}


class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'other']
        labels = {
            'name': 'nazwa',
            'other': 'opis'
        }


class SearchForm(forms.Form):
    search_name = 'wszystkie'
    search_group = 'wszystkie'
    search_mark = 'wszystkie'
    search_status = 'wszystkie'
    search_year = 'wszystkie'

    STATUS_CHOICES = [
        (1, "wszystkie"),
        (2, "zakończone"),
        (3, "aktywne")
    ]
    all_clients = ServisClient.objects.all()
    all_clients_names = [(1, 'wszystkie')]
    names = list(set([client.name for client in all_clients]))
    all_clients_names += [(number, name) for number, name in enumerate(names, start=2)]

    all_groups = Group.objects.all()
    all_groups_names = [(1, 'wszystkie')]
    all_groups_names += [(number, group.name) for number, group in enumerate(all_groups, start=2)]

    all_bikes = Bike.objects.all()
    all_bikes_mark = [(1, 'wszystkie')]
    marks = list(set([bike.mark for bike in all_bikes]))
    all_bikes_mark += [(number, mark) for number, mark in enumerate(marks, start=2)]

    client_name = forms.ChoiceField(choices=all_clients_names, label='klient')
    group_name = forms.ChoiceField(choices=all_groups_names, label='grupa')
    bike_mark = forms.ChoiceField(choices=all_bikes_mark, label='rower')
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    year_of_servis = forms.CharField(label='rok serwisu', max_length=10, initial='wszystkie')

    def wyszukaj(self):
        self.search_name = \
            list(filter(lambda tuple: int(self['client_name'].value()) in tuple, self.all_clients_names))[0][1]

        self.search_group = \
            list(filter(lambda tuple: int(self['group_name'].value()) in tuple, self.all_groups_names))[0][1]

        self.search_mark = \
            list(filter(lambda tuple: int(self['bike_mark'].value()) in tuple, self.all_bikes_mark))[0][1]

        self.search_status = \
            list(filter(lambda tuple: int(self['status'].value()) in tuple, self.STATUS_CHOICES))[0][1]

        self.search_year = self['year_of_servis'].value()
