from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),
    path('<int:movie_id>/',views.detail, name='detail'),
    path('<int:movie_id>/edit/',views.edit, name='edit'),
    path('<int:movie_id>/update/',views.update, name='update'),
    path('<int:movie_id>/delete/',views.delete, name='delete'),
]