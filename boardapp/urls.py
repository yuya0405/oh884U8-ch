from django.urls import path, include
from .views import BoardList

urlpatterns = [
    path('list/', BoardList.as_view()),
]
