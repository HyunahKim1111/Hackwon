from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q

@login_required
def blog_list(request):
    query = request.GET.get('q', '')
    if query:
        blogs = Blog.objects.filter(
            Q(text__icontains=query) | Q(author__username__icontains=query)
        ).distinct()
    else:
        blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs, 'query': query})

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
            return redirect('blog:blog_list')
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

# 좋아요 기능    
@login_required
def blog_like(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False
    else:
        blog.likes.add(request.user)
        liked = True
    return JsonResponse({'total_likes': blog.likes.count(), 'liked': liked})
