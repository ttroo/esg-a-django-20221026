from django.urls import path
from blog import views


urlpatterns = [
    # 해당주소로 요청이 생기면 이 함수가 처리를 해줄거얌
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
]