from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    newss = News.objects.order_by('-date')
    return render(request, 'news/news.html', {'newss': newss})