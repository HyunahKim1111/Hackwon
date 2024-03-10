from django.shortcuts import render
from .forms import RegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()  # User 모델 저장

            # Profile 모델 생성 및 저장
            profile = Profile(user=new_user)
            profile.phone = request.POST.get('phone', '')
            profile.address = request.POST.get('address', '')
            profile.gender = request.POST.get('gender', '')
            profile.nickname = request.POST.get('nickname', '')
            profile.age = request.POST.get('age', 0)
            profile.save()

            # 사용자 로그인 처리
            login(request, new_user)
            return redirect('index')  # 또는 회원가입 완료 페이지로 리디렉션
    else:
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form': user_form})
