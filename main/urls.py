from ast import Delete
from django.urls import path
from django.views.generic import TemplateView

from .views import About,Example,DeletePost, AddPost,DispPost,PostDetail,UpdatePost

urlpatterns=[
    path('temp',TemplateView.as_view(template_name='index.html')),
    path('about',About.as_view()),
    path('exp',Example.as_view()),
    path('addpost',AddPost.as_view()),
    path('all', DispPost.as_view(),name='home'),
    path('detail/<pk>',PostDetail.as_view(),name='detail'),
    path('update/<pk>',UpdatePost.as_view()),
    path('delete/<pk>',DeletePost.as_view(), name='delete')
    ]
#.as_view()