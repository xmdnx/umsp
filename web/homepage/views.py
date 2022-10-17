from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Track

def index(request):
    tracks_list = Track.objects.all()
    return render(request, 'homepage/index.html', {'tracks_list': tracks_list})

def player(request, id):
    try:
        a = Track.objects.get(id=id)
    except:
        raise Http404('Песня не найдена!')

    return render(request, 'homepage/player.html', {'track': a})
