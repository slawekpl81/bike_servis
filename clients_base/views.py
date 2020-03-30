from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bike, Comments, ServisClient, Servis, Group
from .forms import CommentForm, NewClientForm, NewBike, NewServis, NewGroup, SearchForm



# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'index.html', {})

@login_required()
def clients(request):

    form = SearchForm(request.POST or None)
    if form.is_valid():
        form.wyszukaj()
        #form = CommentForm()

    if form.search_name == 'nie określono':
        all_clients = ServisClient.objects.all()
    else:
        all_clients = ServisClient.objects.filter(name=form.search_name)
    if form.search_group == 'nie określono':
        all_groups = Group.objects.all()
    else:
        all_groups = Group.objects.filter(name=form.search_group)
    all_bikes = Bike.objects.all()
    all_servises = Servis.objects.all()

    context = ''
    for client in all_clients:
        if client.group in all_groups:
            context += '<tr>'
            context += f'<td> <a href="{client.id}"> {client.name}</a></td>'
            context += f'<td>{client.phone}</td>'
            context += f'<td>{client.email}</td>'
            context += f'<td><a href="group/{client.group.id}">{client.group}</td>'
            context += '</tr>'
            for count, bike in enumerate(all_bikes):
                if bike.owner == client:
                    context += '<tr>'
                    context += f'<td> </td>'
                    context += f'<td> </td>'
                    context += f'<td> </td>'
                    context += f'<td> </td>'
                    context += f'<td><a href="bike/{bike.id}">{bike.mark}</a></td>'
                    context += f'<td>{bike.model}</td>'
                    context += '</tr>'
                    for servis in all_servises:
                        if servis.bike == bike:
                            context += '<tr>'
                            context += f'<td> </td>'
                            context += f'<td> </td>'
                            context += f'<td> </td>'
                            context += f'<td> </td>'
                            context += f'<td> </td>'
                            context += f'<td> </td>'
                            context += f'<td><a href="servis/{servis.id}">{servis.date}</a></td>'
                            context += f'<td>{servis.servis_range[:20]}...</td>'
                            context += '</tr>'


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
    context= {'group' : form}
    return render(request, 'new_client.html', context)