from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bike, Comments, ServisClient, Servis, Group
from .forms import CommentForm, NewClientForm, NewBike, NewServis, NewGroup, SearchForm
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return connection
#connection.close()

def home(request, *args, **kwargs):
    return render(request, 'index.html', {})

@login_required()
def clients(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.wyszukaj()

    search_name = f"and clients_base_servisclient.name like '{form.search_name}'"
    search_mark = f"and clients_base_bike.mark like '{form.search_mark}'"
    search_group = f"and clients_base_group.name like '{form.search_group}'"
    search_year = f"and strftime('%Y', clients_base_servis.date) = '{form.search_year}'"
    connection_sqllite = create_connection(db_file='C:\\Users\\slawo\\PycharmProjects\\serwisrowerowy\\db.sqlite3')
    cursor = connection_sqllite.cursor()
    query = (f"select \
                clients_base_servisclient.id, \
                clients_base_servisclient.name, \
                clients_base_servisclient.phone, \
                clients_base_servisclient.email, \
                clients_base_group.id, \
                clients_base_group.name, \
                clients_base_bike.id, \
                clients_base_bike.mark, \
                clients_base_bike.model, \
                clients_base_servis.id, \
                clients_base_servis.date, \
                clients_base_servis.servis_range, \
                clients_base_servis.status \
            from  \
                clients_base_servisclient, \
                clients_base_group, \
                clients_base_bike, \
                clients_base_servis \
            where  \
                clients_base_servisclient.group_id = clients_base_group.id and \
                clients_base_bike.owner_id = clients_base_servisclient.id and \
                clients_base_servis.bike_id = clients_base_bike.id \
                {search_name if form.search_name != 'wszystkie' else ''} \
                {search_group if form.search_group != 'wszystkie' else ''} \
                {search_mark if form.search_mark != 'wszystkie' else ''} \
                {search_year if form.search_year != 'wszystkie' else ''} \
                {'and clients_base_servis.status = false' if form.search_status == 'aktywne' else ''} \
                {'and clients_base_servis.status = true' if form.search_status == 'zakończone' else ''} \
             order by \
                clients_base_servisclient.name \
                ")
    print(query)
    cursor.execute(query)

    context = ''
    for row in cursor:
        context += '<tr>'
        context += f'<td><a href="{row[0]}">{row[1]}</td>'
        context += f'<td>{row[2]}</td>'
        context += f'<td>{row[3]}</td>'
        context += f'<td><a href="group/{row[4]}">{row[5]}</td>'
        context += f'<td><a href="bike/{row[6]}">{row[7]}</td>'
        context += f'<td>{row[8]}</td>'
        context += f'<td><a href="servis/{row[9]}">{row[10]}</td>'
        context += f'<td>{row[11]}</td>'
        context += f'<td>{"aktywny" if not row[12] else "zakończony"}</td>'
        context += '<tr>'

    connection_sqllite.close()
    return render(request, 'clients.html', {'text' : context, 'form': form})

@login_required()
def comments(request, *args, **kwargs):
    all_comments = Comments.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()
    view_dict = {'comments': all_comments,
                 'form': form}
    return render(request, 'comments.html', view_dict)

@login_required()
def new_client(request):
    clients_number = ServisClient.objects.all().__len__()
    form = NewClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewClientForm()
    context= {'new_client' : form}
    return render(request, 'new_client.html', context)

@login_required()
def new_bike(request):
    bikes_number = Bike.objects.all().__len__()
    form = NewBike(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewBike()
    context= {'new_bike' : form}
    return render(request, 'new_client.html', context)

@login_required()
def new_servis(request):
    servises_number = Servis.objects.all().__len__()
    form = NewServis(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewServis()
    context= {'new_servis' : form}
    return render(request, 'new_client.html', context)

@login_required()
def new_group(request):
    #servises_number = Servis.objects.all().__len__()
    form = NewGroup(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewGroup()
    context= {'new_group' : form}
    return render(request, 'new_client.html', context)

@login_required()
def client(request, client_id):
    client_one = ServisClient.objects.get(pk=client_id)
    form = NewClientForm(request.POST or None, instance=client_one)
    if form.is_valid():
        form.save()
    context= {'client' : form}
    return render(request, 'new_client.html', context)

@login_required()
def bike(request, bike_id):
    bike_one = Bike.objects.get(pk=bike_id)
    form = NewBike(request.POST or None, instance=bike_one)
    if form.is_valid():
        form.save()
    context= {'bike' : form}
    return render(request, 'new_client.html', context)

@login_required()
def servis(request, servis_id):
    servis_one = Servis.objects.get(pk=servis_id)
    form = NewServis(request.POST or None, instance=servis_one)
    if form.is_valid():
        form.save()
    context= {'servis' : form}
    return render(request, 'new_client.html', context)

@login_required()
def group(request, group_id):
    group_one = Group.objects.get(pk=group_id)
    form = NewGroup(request.POST or None, instance=group_one)
    if form.is_valid():
        form.save()
    context = {'group' : form}
    return render(request, 'new_client.html', context)