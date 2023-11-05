from django.shortcuts import render
from match.models import Match
# from django.db.models import Q

def matches(request):
    # Your view logic here
    matches =  Match.objects.all() # Fetch all venues from the database
    if request.method=="GET":
        t1=request.GET.get('search')
        if t1!=None:
            matchData = Match.objects.filter(Q(match_team1icontains=t1) | Q(match_team2icontains=t1) | Q(match_venue__icontains=t1))
    
    context = {'matches': matches}


    return render(request, 'matches.html', context)