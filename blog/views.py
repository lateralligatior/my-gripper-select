from django.shortcuts import render
from .models import Post
from django.utils import timezone
import os
import pandas as pd

#import pyGithub
#import pandas as pd

#from .readpdfFUNCmain import globaldf

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = {'hi': 'bye'}
    #df = globaldf
    #df = 'hi'
    pd.set_option('display.max_colwidth', -1)
    linelist = []
    directory = os.path.dirname(os.path.realpath(__file__))
    print(directory)
    with open(directory + '\\' + 'testing.txt', mode = 'r', encoding  = 'utf-8') as in_file:
        for line in in_file:
            linelist.append(line)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    postdf = pd.read_csv(directory + '\\' + 'grippercsv.csv')
    
    name = 'neato burrito'
    content = {
            'name' : postdf
            }
    
    #viewdf = pd.read_csv('grippercsv.csv')
    #name = 'Nate'
    return render(request, 'blog/post_list.html', content)