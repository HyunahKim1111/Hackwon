from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

def index(request): # 메인페이지
    return render(request, 'content/index.html')

def hackwon_in_category(request, category_id=None):
    current_category = None
    categories = Category.objects.all()
    query = request.GET.get("q", "")
    
    if query:
        hackwons = Hackwon.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(region__icontains=query) |
            Q(tuition__icontains=query) |
            Q(course__icontains=query) |
            Q(dormitory_available__icontains=query)
        )
    else:
        hackwons = Hackwon.objects.all()
    
    if category_id:
        current_category = get_object_or_404(Category, id=category_id)
        hackwons = hackwons.filter(category=current_category)

    return render(request, 'content/content.html', {
        'current_category': current_category, 
        'categories': categories, 
        'hackwons': hackwons
    })


def hackwon_detail(request, pk):
    hackwon = get_object_or_404(Hackwon, pk=pk)
    return render(request, 'content/content_detail.html', {'hackwon': hackwon})

# 좋아요 기능
@login_required
def hackwon_vote(request, hackwon_id):
    hackwon = get_object_or_404(Hackwon, pk=hackwon_id)
    if request.user in hackwon.voter.all():
        hackwon.voter.remove(request.user)  # 이미 추천했다면 추천 취소
        voted = False
    else:
        hackwon.voter.add(request.user)  # 추천하지 않았다면 추천 추가
        voted = True
    return JsonResponse({'voted': voted, 'total_votes': hackwon.voter.count()})