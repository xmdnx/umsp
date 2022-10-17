from django.http import HttpResponse
from django.shortcuts import render
from .models import Track

def index(request):
    tracks_list = Track.objects.all()
    return render(request, 'homepage/index.html', {'tracks': tracks_list})
