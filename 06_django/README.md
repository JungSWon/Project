#  06_django

#### 목표

- 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- Template Variable을 활용한 Template 제작
- 영화 추천 사이트의 영화 정보 데이터 관리



####  준비사항

- Python Web Framework
  - Django 2.1.x
  - Python 3.6.x

- 샘플 영화 정보
  - 대표적인 영화 총 6개의 정보가 포함된 data.csv
  - 첫번째 프로젝트 01_movie/ 코드 활용

##  



###  1. 데이터베이스

- ORM을 통해서 작성될 클래스의 이름은 Movie 이며, 다음과 같은 정보를 저장합니다.

  | 필드명      | 자료형  | 설명              |
  | ----------- | ------- | ----------------- |
  | title       | String  | 영화명            |
  | audience    | Integer | 누적 관객수       |
  | genre       | String  | 장르              |
  | score       | Float   | 평점              |
  | poster_url  | Text    | 포스터 이미지 url |
  | description | Text    | 영화 소개         |

- migration 후 생성된 테이블을 확인 합니다.

  ``` shell
  (proj06-venv) soowon:~/workspace/PROJ06 $ python manage.py makemigrations
  Migrations for 'movies':
    movies/migrations/0001_initial.py
      - Create model Movie
  (proj06-venv) soowon:~/workspace/PROJ06 $ python manage.py migrate
  Running migrations:
     ... 
    Applying movies.0001_initial... OK
    Applying sessions.0001_initial... OK
  (proj06-venv) soowon:~/workspace/PROJ06 $ python manage.py dbshell 
  sqlite> .tables
  ...
  movies_movie 
  ```

- data.csv 파일에서 데이터를 불러와 db에 저장합니다.

  - csv파일을 프로젝트 폴더 안에 추가합니다.
  - csv파일의 헤더를 삭제 후 아래와 같이 테이블에 추가합니다. 

  ```shell
  (proj06-venv) soowon:~/workspace/PROJ06 $ python manage.py dbshell  
  sqlite> .mode csv
  sqlite> .import data.csv movies_movie
  sqlite> select * from movies_movie;
  ```


###  2. 페이지

####  1. 영화목록

- 해당 페이지에 접근하는 URL은 /movies/ 입니다.
- 데이터베이스에 존재하는 모든 영화의 목록이 표시 되며, 각 영화의 title , score 가 표시
  됩니다.
- title 을 클릭 시, 해당 영화 정보 조회 페이지로 이동합니다.

#### 2. 영화정보조회

- 해당 페이지에 접근하는 URL은 /movies/1/등 이며,영화 정보의 Primary Key가 동적으로 들어갑니다.
- 해당 Primary Key를 가진 영화의 모든 정보가 표시됩니다.
- 영화 정보의 최하단에는 목록 , 수정 , 삭제 링크가 있으며, 클릭 시 각각 영화 목록 , 해당 영
  화 정보 수정 Form , 해당 영화 정보 삭제 페이지로 이동합니다.

#### 3. 영화정보삭제

- 해당 페이지에 접근하는 URL은 /movies/1/delete/등 이며, Primary Key가 동적으로 들어갑니다.
- 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다.
- 영화 정보 목록 페이지로 Redirect 합니다.



##   