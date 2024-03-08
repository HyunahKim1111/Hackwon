from django.urls import path
from .views import *

app_name = 'content'

urlpatterns = [
    path('', hackwon_in_category, name='hackwon_all'),
    path('detail/<int:pk>/<slug:slug>/', hackwon_detail, name='hackwon_detail'),  # 'hackwon_detail' 뷰의 URL 패턴을 수정했습니다.
    path('<slug:category_slug>/', hackwon_in_category, name='hackwon_in_category'),
    path('vote/<int:hackwon_id>/', hackwon_vote, name='hackwon_vote'),
]