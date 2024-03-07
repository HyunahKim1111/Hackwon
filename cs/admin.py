from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.StackedInline):  # Answer 모델을 Question 어드민 페이지에 인라인으로 표시하기 위한 클래스
    model = Answer
    extra = 1  # 기본적으로 표시되는 빈 인라인 폼의 수
    can_delete = True  # 관리자가 인라인으로 답변을 삭제할 수 있도록 허용

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'created', 'updated')  # 목록에 표시될 필드
    list_filter = ('created', 'updated', 'author')  # 필터 옵션을 추가
    search_fields = ('subject', 'content', 'author__username')  # 검색 필드 설정
    # prepopulated_fields = {'slug': ('subject',)}  # subject 필드를 기반으로 slug 필드 자동 채우기 설정
    inlines = [AnswerInline]  # Question 어드민 페이지에서 Answer를 인라인으로 표시

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created', 'updated')  # 목록에 표시될 필드
    list_filter = ('created', 'updated', 'author')  # 필터 옵션을 추가
    search_fields = ('content', 'author__username', 'question__subject')  # 검색 필드 설정

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
