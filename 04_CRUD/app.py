from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///db_flask.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
 

db = SQLAlchemy(app)
db.init_app(app)


# 테이블 생성 
class Movie(db.Model):
    __tablename__= "movies"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String, nullable=False, unique=True)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.DateTime, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.TEXT, nullable=False)
    description = db.Column(db.TEXT, nullable=False)

db.create_all()



@app.route('/')
def index():
    return redirect('/movies')

#첫화면 
#글목록 표시
@app.route('/movies')
def movies():
    print(app.config)
    movies = Movie.query.all()
    return render_template('base.html', movies=movies)
    
    
    
#새글 생성 form 페이지 
@app.route('/movies/new')
def new():
    return render_template('new.html')


#글 생성 페이지  
@app.route('/movies/create',  methods=['POST','GET'])
def create(): 
    title = request.form.get('title')
    title_en = request.form.get('title_en')
    audience = request.form.get('audience')
    
    open_date = datetime.strptime(request.form.get('open_date'),"%Y-%m-%d")
    # date = date.strftime('%Y-%m-%d')

    genre = request.form.get('genre')
    watch_grade = request.form.get('watch_grade')
    score = request.form.get('score')
    poster_url = request.form.get('poster_url')
    description = request.form.get('description')
    
    a = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    db.session.add(a)
    db.session.commit()
    
    return render_template('/fin_create.html')


#글 조회 창
@app.route('/movies/<int:no>')
def show(no):
    m = Movie.query.get(no)
    
    return render_template('/show.html',m=m)
    


#글 수정 form 페이지 
@app.route('/movies/<int:no>/edit')
def edit(no):
    m = Movie.query.get(no)
    
    
    
    return render_template('edit.html',m=m)
     
    
#글 수정 페이지  
@app.route('/movies/<int:no>/update', methods=['POST','GET'])
def update(no):
    
    
    title = request.form.get('title')
    title_en = request.form.get('title_en')
    audience = request.form.get('audience')
    
    open_date = datetime.strptime(request.form.get('open_date'),"%Y-%m-%d")
    
    genre = request.form.get('genre')
    watch_grade = request.form.get('watch_grade')
    score = request.form.get('score')
    poster_url = request.form.get('poster_url')
    description = request.form.get('description')
    
    up = Movie.query.get(no)
    up.title = title
    up.audience = audience
    up.open_date = open_date
    up.genre = genre
    up.watch_grade = watch_grade
    up.score = score
    up.poster_url = poster_url
    up.description = description
    
    db.session.commit()
    
    return redirect('/movies/{}'.format(no))  



    
@app.route('/movies/<int:no>/delete')
def delete(no):
    #해당하는 글을 db에서 삭제한다
    
    delm =Movie.query.get(no)
    db.session.delete(delm)
    db.session.commit()
    
    return redirect('/')
    
    
