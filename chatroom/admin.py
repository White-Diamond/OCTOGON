from django.contrib import admin
from .models import Message, UserList

# Register your models here.
admin.site.register(UserList)
admin.site.register(Message)
