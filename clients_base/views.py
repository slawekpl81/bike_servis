from django.http import HttpResponse
from django.shortcuts import render
from .models import Bike, Comments, ServisClient, Servis
from .forms import CommentForm, NewClientForm, NewBike, NewServis



# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'index.html', {})


def clients(request):
    all_clients = ServisClient.objects.all()
    all_bikes = Bike.objects.all()
    all_servises = Servis.objects.all()
    context = ''
    for client in all_clients:
        context += '<tr>'

        context += f'<td> <a href="{client.id}"> {client.name}</a></td>'
        context += f'<td>{client.phone}</td>'
        context += f'<td>{client.email}</td>'
        context += f'<td>{"TAK" if client.mikesz else " "}</td>'
        context += '</tr>'
        for count, bike in enumerate(all_bikes):
            if bike.owner == client:
                context += '<tr>'
                context += f'<td> </td>'
                context += f'<td> </td>'
                context += f'<td> </td>'
                context += f'<td> </td>'
                context += f'<td><a href="bike/{bike.id}">{bike.name}</a></td>'
                context += f'<td>{bike.type}</td>'
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

    return render(request, 'clients.html', {'text' : context})

def comments(request, *args, **kwargs):
    all_comments = Comments.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()
    view_dict = {'comments': all_comments,
                 'form': form}
    return render(request, 'comments.html', view_dict)

def new_client(request):
    clients_number = ServisClient.objects.all().__len__()
    form = NewClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewClientForm()
    context= {'numbers_of' : clients_number,
              'form' : form}
    return render(request, 'new_client.html', context)

def new_bike(request):
    bikes_number = Bike.objects.all().__len__()
    form = NewBike(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewBike()
    context= {'numbers_of' : bikes_number,
              'form' : form}
    return render(request, 'new_bike.html', context)

def new_servis(request):
    servises_number = Servis.objects.all().__len__()
    form = NewServis(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewServis()
    context= {'numbers_of' : servises_number,
              'form' : form}
    return render(request, 'new_servis.html', context)

def client(request, client_id):
    client_one = ServisClient.objects.get(pk=client_id)
    form = NewClientForm(request.POST or None, instance=client_one)
    if form.is_valid():
        form.save()
    context= {'numbers_of' : client_id,
              'form' : form}
    return render(request, 'new_client.html', context)

def bike(request, bike_id):
    bike_one = Bike.objects.get(pk=bike_id)
    form = NewBike(request.POST or None, instance=bike_one)
    if form.is_valid():
        form.save()
    context= {'numbers_of' : bike_id,
              'form' : form}
    return render(request, 'new_bike.html', context)

def servis(request, servis_id):
    servis_one = Servis.objects.get(pk=servis_id)
    form = NewServis(request.POST or None, instance=servis_one)
    if form.is_valid():
        form.save()
    context= {'numbers_of' : servis_id,
              'form' : form}
    return render(request, 'new_servis.html', context)