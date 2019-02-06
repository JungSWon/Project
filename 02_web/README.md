#  Project 02 - WEB

**목표**

- WEB 프론트엔드에 대한 이해
- 영화 추천 사이트를 위한 HTML를 통한 웹 페이지 마크업 및 레이아웃 구성
- CSS를 통한 선택자 활용 및 웹 페이지 꾸미기
- Bootstrap을 활용한 HTML/CSS, JS Component 활용
- 반응형 웹 페이지 구현



**준비 사항**

1. HTML/CSS, Bootstrap 환경 구성

  - Visual Studio Code
  - [Bootstrap](https://getbootstrap.com/)

2. 웹 페이지를 위한 Assets 다운로드

  - 제공된 자료를 다운받아
    - assets 폴더에서 이미지를 활용했습니다.
    - 구글 스프레드 시트의 data를 참고하여 입력했습니다.
    - 결과물에 관한 예시이미지를 참고하였습니다. 

3. 아래는 홈페이지를 만드는 과정에서 활용한 링크입니다.

  - [google font](https://fonts.google.com/)

  - [color-hex](https://www.color-hex.com/)

    

## 1. 영화 추천 사이트를 위한 레이아웃 구성 (1)

### 1-1. HTML 

-  `<!DOCTYPE html>` DOCTYPE 은 html입니다.
- `<html lang="ko">` html 의 언어는 한국어(ko)입니다.
- `<meta charset="UTF-8">` meta 태그에 인코딩 설정을 UTF-8로 설정합니다.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` meta 태그에 기본 viewport 설정합니다.
- `<title>영화추천사이트</title>`title 태그는 영화추천사이트 라고 설정 합니다.



### 1-2. Nav Bar

#### - 필수사항

- 최상단에 위치합니다.

- Item List는 우측 정렬입니다.

  ```CSS
  .collapse.navbar-collapse {justify-content: flex-end;}
  ```

- 반응형으로 구성되어 일정 수준 이하에서는 item이 숨김(토글러,버거바) 처리 됩니다.

  ```html
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
  </button>
  ```

- Sticky navigation bar로 구성됩니다.

  ```html
  <nav class="navbar navbar-expand-sm navbar-light bg-fad sticky-top">
  ```

  

#### - 선택사항

- 배경색에 투명도를 주어 sticky타입인 nav bar 뒤로 컨텐츠가 비칩니다. 

  ``` CSS
  .navbar {background-color: rgba(210, 208, 222, 0.8)}
  ```

-  로고 폰트와 스타일을 적용합니다.

  ``` CSS
  .navbar-brand, .footer-brand { font-family: 'Baloo Thambi', cursive;
      font-size: 28px; line-height: 1;font-weight: 700;}
  ```

  

### 1-3. Header

#### - 필수사항

- Navigation Bar 바로 아래에 위치합니다.

- 높이는 350px , 너비는 브라우저 전체 영역입니다.

  ```CSS
  #cover{height: 350px; background-size: cover;}
  ```

- 이미지는 선택적으로 활용 가능하되 반드시 배경 이미지가 있어야 합니다.

  ```CSS
  #cover{ background-image: url('../02.web/assets/film1.jpg');}
  ```

- Header 영역의 수직/수평 가운데 정렬 위치에 h2 태그를 사용하여 작성 해주세요.

  ```html
  <h2 class="cover-title">노잼영화 보기엔<br>인생이 짧다!<br></h2>
  ```

  ```CSS
  .cover-title{display: flex;justify-content: center;}
  ```

  

#### - 선택사항

- 배경 이미지에 css 속성 background-* 를 활용합니다.

  ```CSS
  #cover{ background-size: cover;
      	background-position: center center;}
  ```

  



### 1-4. Footer

#### - 필수사항

- 브라우저 최하단에 위치합니다.

- 높이는 50px 이상, 너비는 브라우저 전체 영역입니다.

  ```CSS
  #footer{ height: 200px; display: flex; align-items: flex-end; }
  ```

- 왼쪽에는 본인의 이름 혹은 닉네임, 오른쪽에는 헤더로 올라가는 링크로 구성됩니다.

  ```html
   <footer id="footer" >
          <div class="container">
              <div class="row">
                  <div class="col-2"><p class="footer-copy">&copy; 2019 SWon</p</div>
                  <div class="col-4"><h2 class='footer-brand'>logoortxt</h2></div>
                  <div class="col-4"><h3 class='footer-title'>INFORMATION</h3></div>
                  <div class="col-2"><a href="#" class="top"><img src=".." alt="></a>
  ```

- Footer는 padding이 좌우로 3rem

  ```CSS
  #footer{padding: 0 3rem;}
  ```

  

#### - 선택사항

- 좌측에 닉네임과 함께 카피라이트 표기합니다.

  ``` html
  <p class="footer-copy">&copy; 2019 SWon</p>
  ```

- 상단으로 올라가는 버튼을 이미지에 링크합니다. 

  ```HTML
  <a href="#" class="top"><img src="../02.web/assets/Arrows-Right-Arrow-icon.png" alt=""></a> 
  ```

### 1-5. Font 설정

- 3가지의 폰트를 활용하였습니다. 

  ```html
  <link href="https://fonts.googleapis.com/css?family=Baloo+Thambi|Noto+Sans+KR:400,700,900|Work+Sans:400,700,900" rel="stylesheet">
  ```

  ```CSS
  html{font-family: 'Work Sans', sans-serif;
      font-family: 'Noto Sans KR', sans-serif;}
  .navbar-brand, .footer-brand {font-family: 'Baloo Thambi', cursive;}
  ```

  

## 2.영화 추천 사이트를 위한 레이아웃 구성 (2)

### 2-1. 레이아웃

####  - 필수사항

- 영화 리스트는 container에 속합니다.

  ```html
  <section id="movies">
      <div class="container">
          <header class="subtitle-header"
  ```

  

#### - 선택사항

- 배경 패딩 및 색상을 지정해줍니다.

  ```CSS
  #movies{padding: 30px; background-color: aliceblue;}
  ```

  

###  2-2. subtitle

#### - 필수사항

- subtitle 영역은 위 아래 margin이 3rem입니다.

  ```css
  .subtitle{ margin: 3rem; }
  ```

- 글씨 부분은 h3 태그입니다.

  ```html
  <h3 class="subtitle">영화 목록</h3>
  ```

- 밑줄은 너비가 70px이고, 색상은 자유롭게 해주세요.

  ``` css
  .line-border{ height: 0px; width: 70px; border: solid 1px; color: #063e60; }
  ```

  

#### - 선택사항

- 추가문구를 넣어주고 스타일을 적용합니다.

  ```html
   <p class='sub-text'>영화 쏙쏙 골라보기</p>
  ```

  ``` CSS
  .sub-text{ display: flex;  justify-content: center;  font-weight: 100;  
      font-size: 12px;  letter-spacing: 0.5;  margin-bottom: 10rem; }
  ```

  



### 2-3. Card view

#### - 필수사항

- 카드는 총 6개이며, 반응형으로 배치합니다. 한 줄에 보이는 카드의 갯수는 다음과 같이 구성됩니다.
  576px 미만 : 1개/ 576px 이상 768px 미만 : 2개/ 768px 이상 992px 미만 : 3개/ 992px 이상 : 4개

  ```html
  <div class="row"> <div class="card_view col-lg-3 col-md-4 col-sm-6 col-xs-12">
  ```

- 카드는 각각 위 아래 margin이 1rem입니다.

  ```CSS
  .card_view{ margin: 1rem 0;}
  ```

- 이미지는 제공된 이미지를 활용 합니다. 이미지 alt 속성에 값을 지정하여 서버 혹은 경로 오류로 인해 이미지를 읽어 오지 못할 경우 해당 속성값으로 대체합니다.

  ```html
  <img src="assets/20176251.jpg" class="card-img-top" alt="영화1" data-target="#movie1_modal" data-toggle='modal'>
  ```

- 이미지 밑에는 h4 태그를 활용하여 영화 제목을 작성합니다.

  영화 제목 옆에는 네이버 영화 평점을 작성한다.

  ```html
  <h4 class='card-title'>내안의 그놈 <span class="badge-low">8.69</span></h4>
  ```

- 영화 평점은 9점 이상인 경우 청색 계열로, 9점 미만인 경우는 어두운 계열의 색으로 지정한다.

  ```CSS
  .badge-low{background-color: #cee1ed;}
  .badge-high{background-color: #063e60;}
  ```

  ```html
  <h4 class='card-title'>내안의 그놈 <span class="badge-low">8.69</span></h4>...
  <h4 class='card-title'>말모이<span class="badge-high">9.04</span></h4>
  ```

- 제목 및 평점과 내용에는 구분선이 있습니다.

  구분선 아래에는 영화 장르와 개봉일을 작성합니다.

  ``` html
  <h4 class='card-title'>말모이<span class="badge-high">9.04</span></h4>
  	<hr class='card-line'>
      <p class="card-text">드라마<br>개봉일:2019.01.09</p>
  ```

- 가장 아래에는 네이버 영화 상세 정보 링크를 생성합니다. 링크는 새 창에서 열립니다.

  ``` html
  <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=152632" class="btn btn-primary" target="_blank">영화정보 보러가기</a>
  ```

  

##  3. 영화 상세보기

### 3-1. Modal 

이미지를 클릭하면, 영화 상세 정보와 추가 이미지가 보입니다.

#### - 필수사항

-  카드뷰의 이미지를 클릭하면 modal이 뜨도록 구성 합니다.

  ``` html
  <div class="modal fade" id="movie1_modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel1" aria-hidden="true">
          <div class="modal-dialog" role="document">
              <div class="modal-content">
              <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel1">내안의 그놈</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
  ...
  ```

- Modal의 상단에 영화의 한글명과 영문명을 같이 작성합니다.

  ```html
  <h5 class="modal-title" id="exampleModalLabel1">내안의 그놈 - The Dude in Me</h5>
  ```

- Modal의 헤더 아래에 내용을 포함한 carousel로 구성합니다. 

  ```html
  <div id="carouselExampleIndicators1" class="carousel slide" data-ride="carousel">
      ...
  ```

  

#### - 선택사항 

- carousel의 첫 사진을 어둡게 처리하고 그 위에 영화 내용을 얹습니다. 

  ```html
  <div class="carousel-inner">
      <div class="carousel-item active">
          <div class="image-cover">
              <img src="assets/20176251-1.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption d-none d-md-block">
                  <h5>나 너니? 너 나니??<br>... 
  ```

  ``` css
  .image-cover {position: relative;}
  .image-cover::before {content: "";  position: absolute;
      top: 0; left: 0;  right: 0;  bottom: 0;
      background: linear-gradient(to top, rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.25));}
  ```

  

