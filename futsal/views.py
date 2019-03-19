from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Player
from .forms import PlayerForm


def index(request):
    context = {
        "allPlayers": [
            {
                'name': 'Bishal',
                'age': 18,
                'place': 'Koteshwor'
            },
            {
                'name': 'Mohan',
                'age': 20,
                'place': 'Narephant'
            },
            {
                'name': 'Bhim',
                'age': 22,
                'place': 'Balkumari'
            },
        ],
        "player": Player.objects.all()
    }
    return render(request, "futsal/index.html", context)


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            all_players = Player.objects.all
            return render(request, "futsal/add_player.html", {'all_players': all_players})
    else:
        form = PlayerForm()

    return render(request, "futsal/add_player.html", {'form': form})


def details(request):
    return render(request, "futsal/details.html", {"player": Player.objects.all()})


def contact(request):
    return render(request, "futsal/contact.html", {})


def add_team(request):
    form = PlayerForm()
    return render(request, "futsal/add_team.html", {'form': form})

