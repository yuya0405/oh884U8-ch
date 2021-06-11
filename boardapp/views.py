from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BoardModel

# Create your views here.

class BoardList(ListView):
    template_name = 'list.html'
    model = BoardModel
