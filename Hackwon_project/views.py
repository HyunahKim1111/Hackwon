from django.shortcuts import render


def index(request): # 메인페이지
    return render(request, 'index.html')