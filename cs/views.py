from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # 사용자에게 메시지를 보여주기 위해 import
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required

def question_list(request):
    question_list = Question.objects.all().order_by('-created')  # 질문을 최신순으로 정렬
    paginator = Paginator(question_list, 5)  # 페이지당 15개씩 보여주기

    page_number = request.GET.get('page')  # URL에서 페이지 번호를 가져옴
    page_obj = paginator.get_page(page_number)

    return render(request, 'cs/question_list.html', {'question_list': page_obj})


def question_detail(request, question_id):
    question_detail = Question.objects.get(id=question_id)
    return render(request, 'cs/question_detail.html', {'question_detail':question_detail})


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            try:
                admin_user = User.objects.get(username='admin')
                answer.author = admin_user
                answer.question = question
                answer.save()
                messages.success(request, "답변이 성공적으로 등록되었습니다.")
                return redirect('cs:question_detail', question_id=question_id)  # 수정: 성공적으로 답변을 등록한 후 질문 상세 페이지로 리디렉트
            except User.DoesNotExist:
                messages.error(request, "관리자 계정이 존재하지 않습니다.")
                return redirect('cs:question_detail', question_id=question_id)
        else:
            # 폼이 유효하지 않을 경우, 질문 상세 페이지와 함께 폼을 다시 렌더링
            return render(request, 'cs/question_detail.html', {'question_detail': question, 'form': form})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm()  # 답변 등록 폼 인스턴스 생성
    return render(request, 'cs/question_detail.html', {'question_detail': question, 'form': form})

@login_required
def answer_delete(request, answer_id):
    if request.user.is_authenticated and request.user.is_superuser:  # 관리자 권한 확인
        answer = get_object_or_404(Answer, pk=answer_id)
        question_id = answer.question.id
        answer.delete()
        messages.success(request, "답변이 삭제되었습니다.")
        return redirect('cs:question_detail', question_id=question_id)
    else:
        messages.error(request, "답변을 삭제할 권한이 없습니다.")
        return redirect('cs:question_detail', question_id=question_id)
    

def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            new_question.create_date = timezone.now()
            new_question.save()
            messages.success(request, "질문이 성공적으로 등록되었습니다.")  # 성공 메시지 추가
            return redirect('cs:question_detail', new_question.id)  # 질문 상세 페이지로 리디렉션
    else:
        form = QuestionForm()
    return render(request, 'cs/question_form.html', {'form': form})


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            # 로그인한 사용자가 있을 경우에만 author 필드를 설정
            if request.user.is_authenticated:
                new_question.author = request.user
            new_question.save()
            messages.success(request, "질문이 성공적으로 등록되었습니다.") 
            return redirect('cs:question_detail', new_question.id)
    else:
        form = QuestionForm()
    return render(request, 'cs/question_form.html', {'form': form})


@login_required
def question_update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "질문이 성공적으로 수정되었습니다.")
            return redirect('cs:question_detail', question.id)  # 네임스페이스 반영
    else:
        form = QuestionForm(instance=question)
    return render(request, 'cs/question_update.html', {'form': form, 'question': question})  # 경로 수정


@login_required
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        question.delete()
        messages.success(request, "질문이 성공적으로 삭제되었습니다.")
        return redirect('cs:question_list')  # 네임스페이스 반영
    return render(request, 'cs/question_delete_confirm.html', {'question': question})  # 경로 수정