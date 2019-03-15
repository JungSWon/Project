from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('',views.movie_list,name ='list'),
    path('<int:movie_id>/',views.movie_detail,name='detail'),
    path('<int:movie_id>/',views.movie_delete,name = 'movie_del'),

    path('<int:movie_id>/scores/new',views.score_new,name = 'score_new'),
    path('<int:movie_id>/scores/<int:score_id>/delete',views.score_new,name = 'score_del'),
]