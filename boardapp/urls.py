from django.urls import path, include
from .views import BoardList, BoardDetail

urlpatterns = [
    path('list/', BoardList.as_view()),
    path('detail/<int:pk>', BoardDetail.as_view()),
]
