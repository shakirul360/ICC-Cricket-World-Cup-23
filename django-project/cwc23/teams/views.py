from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from teams.models import Team

# Create your views here.
def teams(request):
    #return HttpResponse("Welcome to Venues Page")
    teams = Team.objects.all()  # Fetch all venues from the database

    for i in teams:
        print(i.name)
    context = {'teams': teams}
    return render(request, 'team_list.html', context)


def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    context = {'team': team}
    return render(request, 'team_detail.html', context)
