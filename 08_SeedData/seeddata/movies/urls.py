from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='list'),
    path('<int:movie_id>/detail/', views.movie_detail, name='detail'),
    path('<int:movie_id>/movie_del/', views.movie_delete, name = 'movie_del'),
    path('<int:movie_id>/edit/', views.movie_edit ,name='edit'),
    path('score_new/<int:movie_id>/scores/new/', views.score_new, name = 'score_new'),
    path('score_del/<int:movie_id>/scores/<int:score_id>/delete/', views.score_delete, name = 'score_del'),
]