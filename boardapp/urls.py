from django.urls import path
from .views import listfunc, detailfunc, TopicCreate, ReplyCreate
# from .views import BoardList, BoardDetail

urlpatterns = [
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
    # path('list/', BoardList.as_view()),
    # path('detail/<int:pk>', BoardDetail.as_view()),
    path('topiccreate/', TopicCreate.as_view(), name='topiccreate'),
    # path('detail/<int:pk>/<int:message_pk>', messagefunc, name='message'),
    path('replycreate/<int:topic_id>/', ReplyCreate.as_view(), name='replycreate'),
]
