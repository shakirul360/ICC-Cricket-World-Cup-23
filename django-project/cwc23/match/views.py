from django.shortcuts import render
from match.models import Match

from django.db.models import Q

def matches(request):

    matchData=Match.objects.all()

    if request.method=="GET":
        t1=request.GET.get('search')
        if t1!=None:
            matchData = Match.objects.filter(Q(match_team1__icontains=t1) | Q(match_team2__icontains=t1) | Q(match_venue__icontains=t1))    

    data={
        'matchData':matchData
    }

    return render(request,"matches.html", data)