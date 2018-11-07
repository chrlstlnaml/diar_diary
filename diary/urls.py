from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^diary_book/$', views.diary_book, name='diary_book'),
]