# Project 04 - CRUD

목표 

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Template Variable을 활용한 Template 제작
- 영화 추천 사이트의 영화 정보 데이터 관리

준비사항

- Python Web Framework : Flask
-  Python Web Framework 사용을 위한 환경 설정 : C9 

##  



###  데이터베이스

- ORM을 통해서 작성 될 클래스의 이름은 `Movie` , 테이블 명은 `movies` 입니다.

  ``` python
  class Movie(db.Model):
      __tablename__= "movies"
       ... 
  ```

- 다음과 같은 정보를 저장합니다.

  - 모든 필드 값에는 빈 값이 들어갈 수 없습니다. `title` 을 제외한 다른 필드는 중복이 허용됩니다.

  | 필드명      | 자료형   | 설명              |
  | ----------- | -------- | ----------------- |
  | title       | String   | 영화명            |
  | title_en    | String   | 영화명(영문)      |
  | audience    | Interger | 누적 관객수       |
  | open_date   | DateTime | 개봉일            |
  | genre       | String   | 장르              |
  | wqtch_grade | String   | 관람등급          |
  | score       | Float    | 평점              |
  | poster_url  | TEXT     | 포스터 이미지 URL |
  | description | TEXT     | 영화소개          |

  ``` python
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
  ```

  

###  페이지

#### 1. 영화목록 [index]

1. 해당 페이지에 접근하는 URL은 `/movies/` 입니다.

     ```python
     @app.route('/movies')
     ```

2. 데이터베이스에 존재하는 모든 영화 목록이 표시 되며, 각 영화의 `title` ,` score` 가 표시됩니다.

     ```python
     def movies():
         print(app.config)
         movies = Movie.query.all()
         return render_template('base.html', movies=movies)
     ```

     ```html
     {% for m in movies %}
     <tr> 
         <td> {{m.id}}</td>
         <td><a href="/movies/{{m.id}}"> {{m.title}}</a></td>
         <td>{{m.score}}</td>
     </tr>
     {% endfor %}
     ```

3. `title` 을 클릭 시, `해당 영화 정보 조회` 페이지로 이동합니다.

     ```html
     <td><a href="/movies/{{m.id}}"> {{m.title}}</a></td>
     ```

4. 영화 목록 최상단에 `새 영화 등록 링크`가 있으며, 클릭 시 `영화 정보 생성 Form` 페이지로 이동합니다.

     ```html
     <a href='/movies/new' class="btn_base" role="button" aria-pressed="true"> 
     새 영화 등록 링크 </a>
     ```

5. html, css 및 bootstrap를 사용하여 페이지를 구성하였습니다.

6. 템플릿은 `base.html` 입니다.	



#### 2. 영화정보 생성 Form [new]

1. 해당 페이지에 접근하는 URL은` /movies/new/` 입니다.

   ```python
   @app.route('/movies/new')
   def new():
       return render_template('new.html')
   ```

2. 영화 정보를 작성할 수 있는 Form이 표시 되며, 다음과 같은 input들을 가지고 있습니다.

   | 필드명      | HTML tag | input type |
   | ----------- | -------- | ---------- |
   | title       | input    | text       |
   | title_en    | input    | text       |
   | audience    | input    | number     |
   | open_date   | input    | date       |
   | genre       | input    | text       |
   | watch_grade | input    | text       |
   | score       | input    | number     |
   | poster_url  | input    | text       |
   | description | textarea | 없음       |

   아래는 코드이해를 돕기 위하여 bootstrap 적용 전 기본 html 코드를 작성했습니다.

   bootstrap이 적용된 html은 제출된 html 파일을 참고 바랍니다. 

   ```html
   <div class="form-group">    
       title: <input type='text' name='title'><br>
       title_en: <input type='text' name='title_en'><br>
       audience: <input type='number' min=0 name='audience'><br>
       open_date: <input type='date' name='open_date'><br>
       genre: <input type='text' name='genre'><br>
       watch_grade: <input type='text' name='watch_grade'><br>
       score: <input type='number' name='score' max=5 min=0 step=0.5><br>
       poster_url: <input type='text' name='poster_url'><br>
       description:<br> <textarea class="form-control" rows="5" name='description'>	</textarea>
   </div>
   ```

3. -1. 작성된 정보는 Submit 버튼 클릭 시 `영화 정보 생성` 페이지로 생성 요청(request)과 함께 전송됩니다.

   -2. 요청을 보내는 방식(method)은 POST를 사용하였습니다.

   ```html
   <form action='/movies/create' method = "POST">
       <div class="form-group">  
           ...
       </div>
       <button type="submit" class="btn btn-primary">Form Submit</button>
   </form>
   ```

4. `score` 는 사용자로부터 최소 0점에서 최대 5점까지 0.5 점 간격으로 받을 수 있습니다.

   ``` html
   score: <input type='number' name='score' max=5 min=0 step=0.5><br>
   ```

   

#### 3. 영화정보 생성 [create]

1. 해당 페이지에 접근하는 URL은 `/movies/create/` 입니다.

     ```python
     @app.route('/movies/create',  methods=['POST','GET'])
     def create(): 
     ```

2. -1. 이전 페이지로부터 전송 받은 데이터를 데이터베이스에 저장합니다.

     -2. 개봉일은 datetime을 사용하여 받아옵니다.

     ```python
     title = request.form.get('title')
     title_en = request.form.get('title_en')
     audience = request.form.get('audience')
     open_date = datetime.strptime(request.form.get('open_date'),"%Y-%m-%d")
     ...
     
     a = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
     
     db.session.add(a)
     db.session.commit()
     ```

3. '영화 정보 생성이 완료되었습니다.' 메시지와 함께 `영화 목록` 으로 이동하는 링크를 표시합니다.

     ``` html
     <form action = "/movies" class="fin">
         <button type="button" class="btn">메시지</button>
     </form>
     ```

     

#### 4. 영화 정보 조회 [show]

1. 해당 페이지에 접근하는 URL은` /movies/1/` ,` /movies/2/` 등 이며, 숫자 부분은 데이터베이스에 저장된 영화 정보의 Primary Key가 동적으로 할당됩니다. 

     ```python
     @app.route('/movies/<int:no>')
     def show(no):
         m = Movie.query.get(no)
         return render_template('/show.html',m=m)
     ```

2. 해당 Primary Key를 가진 영화의 모든 정보가 표시됩니다.

     ```html
     <h1 class="display-4">{{m.title}}</h1>
     {{m.title_en}} <br> 
     관객수 : {{m.audience}} <br> 
     개봉일 : {{m.open_date}}<br> 
     {{m.genre}}<br> 
     {{m.watch_grade}}<br> 
     평점: {{m.score}}<br> 
     {{m.poster_url}}<br> 
     {{m.description}}<br>
     ```

3. 영화 정보의 최하단에는 `목록` , `수정` , `삭제` 링크가 있으며, 클릭 시 각각 `영화 목록` , `해당 영화 정
     보 수정 Form` , `해당 영화 정보 삭제` 페이지로 이동합니다.

     ```html
     <a class="btn" href="/movies/{{m.id}}/edit" role="button">수정</a>
     <a class="btn" href="/movies/{{m.id}}/delete" role="button">삭제</a>
     <a class="btn" href="/movies" role="button">목록</a>
     ```

     

#### 5. 영화정보 수정 Form [edit]

1. 해당 페이지에 접근하는 URL은` /movies/1/edit/` ,` /movies/2/edit/` 등 이며, 숫자 부분은 데이터베이스에 저장된 영화 정보의 Primary Key가 동적으로 할당됩니다.

     ```python
     @app.route('/movies/<int:no>/edit')
     def edit(no):
         m = Movie.query.get(no)
         return render_template('edit.html',m=m)
     ```

2. 해당 Primary Key를 가진 영화 정보를 수정할 수 있는 Form을 생성합니다.

     - 아래와 같이 value=' ' 값 안에 데이터베이스의 정보를 불러와  이전 정보가 입력된 채로 표시됩니다.

     ```html
     <div class="form-group">    
         title: <input type='text' name='title' value='{{m.title}}'><br>
         title_en: <input type='text' name='title_en' value='{{m.title_en}}'><br>
     ...
         poster_url: <input type='text' name='poster_url' value='{{m.poster_url}}'><br>
         description:<br> <textarea class="form-control" rows="5" name='description'>{{m.description}}</textarea>
         <br>
     </div>
     ```

3. -1. 정보는 Submit 버튼 클릭 시 `영화 정보 수정 `페이지로 수정 요청(request)과 함께 전송됩니다.

     -2. 요청을 보내는 방식(method)은 POST를 사용하였습니다.

     ``` html
     <form action='/movies/{{m.id}}/update' method = "POST">...</form>
     ```

     

####  6. 영화정보 수정 [update]

1. 해당 페이지에 접근하는 URL은 `/movies/1/update/` , `/movies/2/update/ `등 이며, 숫자 부분은 데이터베이스에 저장된 영화 정보의 Primary Key가 동적으로 할당됩니다.

     ```python
     @app.route('/movies/<int:no>/update', methods=['POST','GET'])
     def update(no):
     ```

2. 해당 Primary Key를 가진 영화 정보를 이전 페이지로부터 전송 받은 데이터로 변경하여 데이터베이스에 저장합니다.

     ```python
     title = request.form.get('title')
     title_en = request.form.get('title_en')
     audience = request.form.get('audience')
     open_date = datetime.strptime(request.form.get('open_date'),"%Y-%m-%d")
     ...
     
     up = Movie.query.get(no)
     up.title = title
     up.audience = audience
     ...
     
     db.session.commit()
     ```

3. 해당 페이지에서 수정한 영화 정보를 조회하는 `영화 정보 조회`페이지로 Redirect 합니다.

     ```python
     return redirect('/movies/{}'.format(no))  
     ```

     

####  7. 영화 정보 삭제 [delete]

1. 해당 페이지에 접근하는 URL은 `/movies/1/delete/` ,` /movies/2/delete/` 등 이며, 숫자 부분은 데이터베이스에 저장된 영화 정보의 Primary Key가 동적으로 할당됩니다.

     ```python
     @app.route('/movies/<int:no>/delete')
     def delete(no):
     ```

2. 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다.

     ```python
     delm =Movie.query.get(no)
     db.session.delete(delm)
     db.session.commit()
     ```

3. `영화 정보 목록 `페이지로 Redirect 합니다.

   ```python
   return redirect('/')
   ```

   



##  

제출 

- 작성한 모든 파일은 04_crud 디렉토리에 아래와 같이 위치하였습니다.

>04_crud/
>​	README.md
>​	app.py
>​	db_flask.sqlite3
>​	templates/
>​		index.html
>​		edit.html
>​		new.html
>​		show.html
>​		base.html

