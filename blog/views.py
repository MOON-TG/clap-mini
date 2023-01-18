from django.shortcuts import render
from .models import Info
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
   model = Info
   ordering = '-pk'
   paginate_by = 1




# def index(request):
#    posts = Post.objects.all()
#    return render(
#       request,
#       'blog/index.html',
#       {
#          'posts':posts,
#       }
#    )