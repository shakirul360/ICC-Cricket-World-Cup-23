from django.shortcuts import render
from news.models import News

# Create your views here.
def lateNews(request):
    
    newsData=News.objects.all()

    data={
        'newsData':newsData
    }

    return render(request,"lateNews.html", data)