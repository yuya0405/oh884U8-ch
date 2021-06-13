from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BoardModel, PostModel
from django.urls import reverse_lazy

# Create your views here.

def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    object.views += 1
    object.save()

    post_list = PostModel.objects.all()
    return render(request, 'detail.html', {'object':object, 'post_list':post_list})

# class BoardList(ListView):
#     template_name = 'list.html'
#     model = BoardModel
#
# class BoardDetail(DetailView):
#     template_name = 'detail.html'
#     model = BoardModel #TODO: DetailModel

class TopicCreate(CreateView):
    template_name = 'topiccreate.html'
    model = BoardModel
    fields = ('topic', 'starter', 'description')
    success_url = reverse_lazy('list')

def messagefunc(request, pk, message_pk):
    post_list = PostModel.objects.all()
    return render(request, 'detail.html', {'post_list':post_list})
