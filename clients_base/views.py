from django.http import HttpResponse
from django.shortcuts import render
from .models import Bike, Comments

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'index.html', {})

def clients(request, *args, **kwargs):
    return render(request, 'clients.html', {})

def comments(request, *args, **kwargs):
    all_comments = Comments.objects.all()
    print('KOM')
    #print(all_comments)
    simple_dict = {'comments': all_comments}
    for com in simple_dict['comments']:
        print(com)
    dict_comments = {comment.author:comment for comment in all_comments}
    #print(dict_comments)
    return render(request, 'comments.html', simple_dict)
