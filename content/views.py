from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    return render(request, 'content/index.html')

def hackwon_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    hackwons = Hackwon.objects.filter()

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        hackwons = Hackwon.objects.filter(category=current_category)

    return render(request, 'content/content.html', {'current_category': current_category, 'categories':categories, 'hackwons': hackwons})

def hackwon_detail(request, pk, slug):
    hackwon = get_object_or_404(Hackwon, pk=pk, slug=slug)
    return render(request, 'content/content_detail.html', {'hackwon': hackwon})
