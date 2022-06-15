from dataclasses import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.http import JsonResponse
from .models import Post
# Create your views here.
#CRUD with respect to CBV
class About(TemplateView):
    template_name='about.html'

class Example(View):
    def get(self,request):# if request.method==='GET'
        return JsonResponse("Welcome to CBV",safe=False)
    def post(self,request):# if request.method==='POST'
        data=request.POST.get('username')
        return JsonResponse("Welcome to CBV POST",safe=False)

class AddPost(CreateView):
    model=Post
    fields='__all__'
    success_url= reverse_lazy('home')

class DispPost(ListView):
    model=Post
    fields='__all__'
    context_object_name='ourposts'
    success_url= reverse_lazy('home')

class PostDetail(DetailView):
    model=Post
    fields='__all__'
    context_object_name='singlepost'

class UpdatePost(UpdateView):
    model=Post
    fields='__all__'
    success_url= reverse_lazy('home')

class DeletePost(DeleteView):
    model=Post
    fields='__all__'
    success_url= reverse_lazy('home')



# {"posts":post}
#  for post in posts
