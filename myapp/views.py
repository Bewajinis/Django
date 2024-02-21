from multiprocessing import context
from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


post = [
    {
        'author': 'Bewaj Emmy',
        'title': 'My Dear Club',
        'content': 'The name of my favorite football club is Mnachester United',
        'date_posted': '23th January, 2020',
    },
    {
        'author': 'Tolu Ruthny',
        'title': 'My Biz Brand is OUt',
        'content': 'The name of my business brand is Ravish Bite',
        'date_posted': '30th January, 2024',
    }
        
]



# Create your views here.
def home(request):
     context = {
          'posts': Post.objects.all()
     }
     return render(request, 'myblog/home.html', context)

def about(request):
    return render(request, 'myblog/about.html',{'title': "About Page"})