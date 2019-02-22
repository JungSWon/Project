# Project 04 - Detail

목표

- 영화 추천 사이트의 세부 페이지 구성
- Template Variable을 활용한 Template 제작

준비사항

- Django Web Framework 사용

- 개발 환경 : C9

- 위에 따라 가상환경 설정 및 django를 설치합니다. 

  ``` shell
  soowon:~/workspace $ mkdir pj05
  soowon:~/workspace/pj05 $ cd pj05
  soowon:~/workspace/pj05 $ pyenv virtualenv 3.6.7 pj05-venv
  soowon:~/workspace/pj05 $ pyenv local pj05-venv 
  (pj05-venv) soowon:~/workspace/pj05 $ pip install django
  ```



##  Django Setting

####  1. Django Project 생성

- 프로젝트명 : 'pj05_detail'

  ``` shell
  (pj05-venv) soowon:~/workspace/pj05 $ django-admin startproject pj05_detail
  ```

####  2. detail 이라는 이름의 앱 생성

- ``` shell
  $ python manage.py startapp detail
  ```

- 어플리케이션 등록 (setting.py)  

  ``` python
  INSTALLED_APPS = [... ,'detail',]
  ```

####  3. 언어 및 시간 설정

- 한국 표준 (setting.py )

  ``` python
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

#### 4. ALLOWED_HOSTS 설정에 `"*"` 추가

- setting.py -  `ALLOWED_HOSTS = ['*']`



##  base.html 구성

####  1. Bootstrap css 추가

- `static` 파일 로 추가 합니다. 

  `../static/css/style.css`

#### 2. Nav Bar 구성

- '페이지 구성'의 링크가 모두 들어 있습니다.
- `Nav Bar` 는 `bootstrap navbar component` 를 활용해서 구성합니다.
  - MySite를 클릭하면 / 로 이동합니다.
  - Q&A를 클릭하면 qna/ 로 이동합니다.
  - Mypage를 클릭하면 mypage/ 로 이동합니다.
  - SignUp을 클릭하면 signup/ 으로 이동합니다.
- 링크들의 위치를 알맞게 구성합니다.
- `favicon`  을 추가합니다.



##  페이지 구성

- 여기에서 사용하는 html 파일들은 base.html 을 `extends` 해서 만듭니다. (/templates/base.html)



####  1. `/`   (/templates/index.html)

- 시맨틱 태그 `header` 와 `footer` 를 사용하여 페이지를 구성합니다.

1. Header
   - Navigation Bar 바로 아래에 위치합니다.
   - 높이는 **350px** , 너비는 **브라우저 전체 영역**입니다.
   - **배경 이미지**를 설정합니다. 
   - Header 영역의 수직/수평 가운데 정렬 위치 에 `h1` 태그를 작성합니다. 
2. Footer
   - 브라우저 최하단에 위치합니다.

   - 높이는 **50px**, 너비는 **브라우저 전체 영역**입니다.

   - 왼쪽에는 **닉네임**, 오른쪽에는 **헤더로 올라가는 링크**로 구성됩니다.

   - bootstrap Utilities의 `Spacing` 을 활용하여 좌우 `padding` 을 만들어줍니다.

     

####  2. `qna/` (/templates/qna.html)

- 사용자의 질문을 받기위한 페이지입니다. 
  - Bootstrap Form 을 사용합니다.
  - 제목, 이메일, 내용 을 위한 `input tag`를 사용합니다.
  - 960px 보다 큰 화면과 992px 보다 작은 화면 에서 알맞게 화면을 구성합니다.



#### 3. `mypage/` (/templates/mypage.html)

- 유저 정보를 출력하는 페이지
  - 사용자의 개인정보와 작성 글을 보여줄 페이지입니다.
  - 화면 좌측엔 사용자의 정보, 우측엔 사용자가 작성한 글 목록을 보여줍니다.
  - 좌측의 사용자 정보는 Bootstrap Card 를 활용해서 구성합니다.
    - 사용자의 이미지는 .round 를 사용하여 원형으로 표시합니다.

      - 이미지가 왜곡되지 않고 원형에 맞게 잘립니다.  

    - 이미지는 장고 프로젝트 내부의 이미지를 스태틱으로 적용시킵니다.

    - 사용자의 정보를 보여주는 Card는 .position-fixed 를 사용하여 스크롤을 아래로

      내리더라도 좌측에 그대로 유지 시켜서 사용자에게 보여줍니다.



####  4. `signup/ ` (/templates/signup.html)

- 회원가입 페이지 
  - Bootstrap Form 을 사용합니다.
  - 이메일, 이름, 비밀번호, 비밀번호 확인 을 위한 input tag를 사용합니다.
  - Bootstrap Grid System 을 사용하여 화면 좌측엔 이미지, 우측엔 데이터를 입력할 폼을
    보여줍니다.



####  5. `<str:not_found>/`  (/templates/notfound.html)

- 위에서 만든 경로를 제외한 다른 요청이 들어오면 보여줄 404페이지입니다.
- variable routing 을 활용하여 사용자가 잘못 입력한 경로를 잘못된 경로라고 표시해줍니다.





##  



아래와 같이 결과물을 제출합니다. 

>05_detail/
>​	pj05_detail/
>​		__init__.py
>​		settings.py
>​		urls.py
>​		wsgi.py
>
>​	detail/  (수정하기)
>​		templates/
>​			...
>​		__init__.py
>​		admin.py
>​		apps.py
>​		models.py
>​		tests.py
>​		urls.py
>​		views.py
>
>​	manage.py
>
>​	README.md



