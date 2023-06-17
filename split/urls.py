from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('split/', views.split, name='split'),
    path('download/<tag>/', views.download, name='download'),
    path('loaderdl', views.loaderdl, name='loaderdl'),
    path('about', views.about, name='about')
]