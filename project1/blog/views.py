from django.shortcuts import render
from .forms import BlogForm
from .models import Blog

# Create your views here.

def addBlogView(request):
    form = BlogForm()
    template_name = 'blog/add.html'
    context = {'form' : form}
    if request.method == 'POST':
        form =BlogForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template_name,context)