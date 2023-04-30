from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.views.generic import CreateView

def home(request):
    return render(request, 'index.html')


class CreatePostView(CreateView):
    model = Post
    fields = ['name', 'surename', 'group']
    template_name = 'create.html' 

    def get_success_url(self) -> str:
        return reverse('home')
