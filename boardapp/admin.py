from django.contrib import admin
from .models import BoardModel, PostModel

# Register your models here.

admin.site.register(BoardModel)
admin.site.register(PostModel)
