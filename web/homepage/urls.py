from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.player, name='player')
]