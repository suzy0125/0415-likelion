from django.shortcuts import render, get_object_or_404, redirect
from .models import Suzy

# Create your views here.
def home(request):
    posts = Suzy.objects
    return render (request, 'selfintroduction/home.html', {'posts':posts})

def post(request):
    return render (request, 'selfintroduction/post.html')