from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BoardModel

# Create your views here.

def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

# class BoardList(ListView):
#     template_name = 'list.html'
#     model = BoardModel
#
# class BoardDetail(DetailView):
#     template_name = 'detail.html'
#     model = BoardModel #TODO: DetailModel
