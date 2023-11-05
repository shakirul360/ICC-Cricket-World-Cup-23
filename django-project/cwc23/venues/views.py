from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from venues.models import Venue

# Create your views here.
def venues(request):
    #return HttpResponse("Welcome to Venues Page")
    venues = Venue.objects.all()  # Fetch all venues from the database
    context = {'venues': venues}
    return render(request, 'venues.html', context)

def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, 'venue_detail.html', {'venue': venue})

def index(request):
    context = {'index': 'Welcome to home page'}
    return render(request, 'index.html', context)




