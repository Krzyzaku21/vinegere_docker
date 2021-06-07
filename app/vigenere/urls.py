from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.encrypter, name='encrypter'),
    path('score/<int:pk>/', views.score, name='score'),
    path('score2/<pk>/', views.score2, name='score2'),
    path('decrypter/<pk>/', views.decrypter, name='decrypter'),
]
