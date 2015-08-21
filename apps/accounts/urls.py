from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from .views import login

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
