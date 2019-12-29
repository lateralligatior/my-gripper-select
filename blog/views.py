from django.shortcuts import render
from .models import Post
from django.utils import timezone
#import pyGithub
#import pandas as pd

#from .readpdfFUNCmain import globaldf

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = ['hi', 'bye']
    #df = globaldf
    #df = 'hi'
    #viewdf = pd.read_csv('grippercsv.csv')
    return render(request, 'blog/post_list.html')