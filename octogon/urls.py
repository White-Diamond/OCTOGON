from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('messageboard/', include("messageboard.urls")),
    path('profilepage/', include("profilepage.urls")),
    path('chatroom/', include('chatroom.urls')),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
]

