# 08_django - Seed Data

#### 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작

- Seed Data를 활용한 DB 설계

- Django Form을 통해 입력받은 데이터 유효성 검증


#### 준비사항

- Python Web Framework
  - Django 2.1.x
  - Python 3.6.x
- 샘플 영화 정보
  - 프로젝트08_database 코드를 활용하여 데이터 생성 

##  



###  데이터베이스 설계

#### 1-1. 테이블 관계

- `db.sqlite3`에서 테이블간의 관계는 아래와 같습니다. 

  - ```mermaid
    graph LR;
    A(Genre) --1:N--> B(Movie);
    B --1:N--> C(Score);
    ```

- Genre

  | 필드명 | 자료형  | 설명        |
  | ------ | ------- | ----------- |
  | id     | Integer | Primary Key |
  | name   | String  | 장르 구분   |

- Movie

  | 필드명      | 자료형  | 설명                                                         |
  | ----------- | ------- | ------------------------------------------------------------ |
  | id          | Integer | Primary Key                                                  |
  | title       | String  | 영화명                                                       |
  | audience    | Integer | 누적 관객수                                                  |
  | poster_url  | Text    | 포스터 이미지 URL                                            |
  | description | Text    | 영화 소개                                                    |
  | genre_id    | Integer | Genre의 Primary Key (id값)<br />Genre가 삭제되어도 Movie에 영향을 주지 않는다. |

- Score

  | 필드명   | 자료형  | 설명                                                         |
  | -------- | ------- | ------------------------------------------------------------ |
  | id       | Integer | Primary Key                                                  |
  | content  | String  | 한줄평 (평가 내용)                                           |
  | score    | Integer | 평점                                                         |
  | movie_id | Integer | Movie의 Primary Key (id값)<br />Movie가 삭제되면 해당 score도 삭제된다. |

###  Seed Data 반영

1. 주어진 `movie.json` 과 `genre.json` 을 `movies/fixtures/` 디렉토리로 옮깁니다.

2. 아래의 명령어를 통해 반영합니다.

   ``` shell 
   $ python manage.py loaddata genre.json 
   Installed 11 object(s) from 1 fixture(s)
   $ python manage.py loaddata movie.json 
   Installed 10 object(s) from 1 fixture(s)
   ```

3. `admin.py` 에 `Genre` 와 `Movie` 클래스를 등록한 후, `/admin` 을 통해 실제로 데이터베이스에 반영
   되었는지 확인합니다. 

###  `movies` APP

>  Genre는 CRUD를 만들지 않습니다.

####  영화 생성을 위한 사용자 Form

1. 영화목록 에서 a 태그 혹은 버튼을 만듭니다. 
  - Form 요청URL: `GET/movies/new `
2. 템플릿 파일 이름은 `form.html` 으로, 영화 수정 페이지와 같이 공유합니다.
3. `id` 를 제외한 모든 필드에 맞는 `form` 과 `input` 을 제공합니다.
4. poster_url 필드 대신 poster_image를 통해 미디어 파일 업로드 기능을 이용할 수 있습니다.

####  영화 생성

1. 요청 처리 URL: `POST /movies/new` 
2. 검증을 통해 
   - 유효한 경우 데이터베이스에 저장하고,
   - 유효하지 않은 경우 오류 메시지와 함께 `form.html` 을 반환합니다.
3. 데이터베이스에 저장되면, 영화 정보 조회 `GET /movies/<int:movie_pk>` 로 redirect 합니다.

####  영화 수정을 위한 사용자 Form

1. 영화 정보 조회 페이지에서 a 태그 혹은 버튼을 만듭니다. 
  - Form 요청 URL: `GET /movies/<int:movie_pk>/edit`
2. 템플릿 파일 이름은 `form.html` 으로, 영화 생성 페이지와 같이 공유합니다.
3. `id` 를 제외한 모든 필드에 맞는 `form` 과 `input` 을 제공합니다.
4. poster_url 필드 대신 poster_image를 통해 미디어 파일 업로드 기능을 이용할 수 있습니다.

####  영화수정

1. 요청 처리 URL: `POST /movies/<int:movie_pk>/edit`
2. 검증을 통해 
  - 유효한 경우 데이터베이스에 변경내용을 저장 하며, 
  - 유효하지 않은경우 경우 오류 메시지와 함께 `form.html` 을 반환합니다.
3. 데이터베이스에 수정되면, 영화 정보 조회 `GET /movies/<int:movie_pk>` 로 redirect 합니다.

####  평점 생성

1. 영화 정보 조회 페이지에서 `form `을 통해 평점을 작성할 수 있습니다.
2. 평점 생성 URL : `POST /movies/1/scores/new `, `POST /movies/2/scores/new` 등 
  - 동적으로 할당되는 부분이 존재합니다. 
  - 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
3. 검증을 통해 
  - 유효한 경우 데이터베이스에 저장을 하며, 
  - 유효하지 않은 경우 영화 정보 조회 페이지로 Redirect 합니다.
4. 데이터베이스에 저장되면, 해당하는 영화의 영화 정보 조회 페이지로 Redirect 합니다.



##  



