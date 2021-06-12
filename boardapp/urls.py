from django.urls import path
from .views import listfunc, detailfunc
# from .views import BoardList, BoardDetail

urlpatterns = [
    path('list/', listfunc),
    path('detail/', detailfunc),
    # path('list/', BoardList.as_view()),
    # path('detail/<int:pk>', BoardDetail.as_view()),
]
