from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from player.models import Player


# Create your views here.
def players(request):
    #return HttpResponse("Welcome to Venues Page")
    players = Player.objects.all()  # Fetch all venues from the database
    context = {'players': players}
    return render(request, 'player_list.html', context)
    # return HttpResponse("PlayerListPage")


def player_info(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'player_info.html', {'player': player})
    