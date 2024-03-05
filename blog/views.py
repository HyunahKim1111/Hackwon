from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs':blogs})

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    fields = ['photo','text']
    template_name = 'blog/detail.html'

class BlogUploadView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['photo', 'text']
    template_name = 'blog/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else: 
            return self.render_to_response({'form':form})
        
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/'
    template_name = 'blog/delete.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['photo','text']
    template_name = 'blog/update.html'
    
