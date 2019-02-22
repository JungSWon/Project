from django.shortcuts import render, redirect
from .models import Movie


#영화목록 : /movies/
def index(request):
    #DB의 영화목록 가져오기
    movies = Movie.objects.all()
    context = {'movies':movies,}
    return render(request,'movies/index.html',context)
    

def new(request):
    return render(request, 'movies/new.html')
    
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url,description=description)
    movie.save()
    return redirect('index')

    
#영화정보조회 : /movies/1/
def detail(request,movie_id):
    #아이디에 해당하는 영화정보 DB가져오기
    movie = Movie.objects.get(id=movie_id)
    context = {'movie':movie,}
    return render(request,'movies/detail.html', context)
    
#수정 : /movies/
def edit(request, movie_id):
    #아이디에 맞게 (수정할)DB불러오기
    movie = Movie.objects.get(id=movie_id)
    context ={'movie':movie,}
    return render(request, 'movies/edit.html',context)
    
#수정완료
def update(request, movie_id):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie.objects.get(id=movie_id)
    movie.title = title
    movie.audience = audience
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()
    return redirect('detail', movie.id)

#삭제
def delete(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('index')