from django.http import HttpResponse
from django.shortcuts import render
from .models import Bike, Comments, ServisClient
from .forms import CommentForm, NewClientForm, NewBike


# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'index.html', {})


def clients(request, *args, **kwargs):
    return render(request, 'clients.html', {})

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