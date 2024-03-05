from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('upload/', BlogUploadView.as_view(), name='blog_upload'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
]