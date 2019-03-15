from django.shortcuts import render , get_object_or_404, redirect
from .models import Movie, Score

# 영화목록 GET/movies/
def movie_list(request):
    movies = Movie.objects.all()
    context ={'movies':movies}
    return render(request,'movie/list.html',context)

# 영화정보조회 GET/movies/1/
# 평점목록 GET/movies/1/
def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie,id = movie_id)
    score = movie.score_set.all()
    context = {'movie':movie, 'score':score}
    return render(request,'movie/detail.html',context)

# 영화정보삭제 POST/movies/1/delete/
def movie_delete(request,movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    if request.method == 'POST':
        movie.delete()
    return redirect('list')


# 평점생성 POST/movies/1/scores/new/
def score_new(request,movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    if request.method == 'POST':
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie = movie
        score.save()
    return redirect('detail',movie_id)


# 평점 삭제 POST/movies/1/scores/1/delete/
def score_delete(request,movie_id,score_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
    return redirect('detail',movie_id)
