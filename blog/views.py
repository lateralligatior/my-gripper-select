from django.shortcuts import render
from .models import Post
from django.utils import timezone
#import pyGithub

#from .readpdfFUNCmain import globaldf

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #df = globaldf
    #df = 'hi'
    return render(request, 'blog/post_list.html', {'posts': posts})