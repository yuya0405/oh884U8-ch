from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BoardModel

# Create your views here.

def listfunc(request):
    return render(request, 'list.html', {'some':100})

def detailfunc(request):
    return render(request, 'detail.html', {})

# class BoardList(ListView):
#     template_name = 'list.html'
#     model = BoardModel
#
# class BoardDetail(DetailView):
#     template_name = 'detail.html'
#     model = BoardModel #TODO: DetailModel
