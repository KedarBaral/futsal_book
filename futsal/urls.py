from django.urls import path
from . import views

app_name = 'futsal'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_player/', views.add_player, name='add_player'),
    path('details/', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('add_team/', views.add_team, name='add_item'),
]
