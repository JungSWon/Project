# Project01 명세	

##  1. 영화진흥위원회 오픈 API

(1)  API키는 환경변수로 저장합니다.

(2) 기준일(마지막 일자)은 2019년 1월 13일입니다.

(3) 조회기간은 총 10주입니다. 

(4) 주간(월~일)까지 기간의 데이터를 조회합니다.

(5) 수집된 데이터에서 영화대표코드 , 영화명 , 해당일 누적관객수 , 해당일 을 기록합니다.

(6)  lastday를 기점으로 일주일단위의 데이터를 조회합니다.

```python
#(1)
api_key = os.getenv('KOBIS_API_KEY') 
#(2)
lastday = datetime(2019, 1, 13)
#.. 중략 .. 
name_li = [] 
#(3)
for i in range(10): today = lastday.strftime('%Y%m%d')
#(4) weekGb=0
    rank_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={api_key}&targetDt={today}&weekGb=0' 
    res = requests.get(rank_url)   
    ranking = res.json()  
    rank_list = ranking.get('boxOfficeResult').get('weeklyBoxOfficeList')        
#(5)
    for li in rank_list:
        f = open('boxoffice.csv','a',encoding='utf-8', newline='')
        movie_set = csv.writer(f)   
        list_set = [li.get('movieCd'),li.get('movieNm'),li.get('audiAcc'),today]
        if li.get('movieNm') not in name_li:
            movie_set.writerow(list_set)
            name_li.append(li.get('movieNm'))
        f.close()
#(6)
    lastday += timedelta(days= -7)
    
```

(7) 다양성 영화/상업 영화를 모두 포함합니다. : 요청변수 Default

(8) 한국/외국 영화를 모두 포함합니다. : 요청변수 Default 

(9) 모든 상영지역을 포함합니다. : 요청변수 Default

(10) 해당일 누적관객수 는 중복시 최신 정보를 반영하여야 합니다. 



## 2. 영화진흥위원회 오픈 API (영화상세정보)

(1) 영화별로 다음과 같은 내용을 저장합니다. 

- 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 개봉연도 , 상영시간 , 장르 , 감독명 , 관람등급 , 배우1 , 배우2 , 배우3

(2) 배우의 경우 최대 3명입니다. 영화에 따라 1~2명일 수도 있습니다.

(3) 해당 결과를 movie.csv에 저장합니다.

```python
for cd in r_li:
    detail_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={api_key}&movieCd={cd}'
        
    res = requests.get(detail_url)
    details = res.json()
    dtls = details.get("movieInfoResult").get('movieInfo')
#(3)
    f = open('movie.csv','a',encoding='utf-8', newline='')
    movie_detail_set = csv.writer(f) 
    detail_basic_set = 
#(1)   
[dtls.get('movieCd'),dtls.get('movieNm'),dtls.get("movieNmEn"),dtls.get("movieNmOg"),dtls.get("prdtYear"),dtls.get("showTm")]

    #장르
    genr_str = ''   
    for g in dtls.get('genres'):
        genr_str += g.get('genreNm') + '/'
    detail_basic_set.append(genr_str[:-1]) #마지막'/'빼기
    #감독
    direc_str = ''   
    for d in dtls.get('directors'):
        direc_str += d.get('peopleNm') +'/'
    detail_basic_set.append(direc_str[:-1])
    #관람등급
    detail_basic_set.append(dtls.get('audits')[0].get('watchGradeNm'))
#(2)
    #배우들 
    i = 0
    for a in dtls.get('actors'):
        detail_basic_set.append(a.get('peopleNm'))
        i+=1
        if i ==3:
            break
    
    movie_detail_set.writerow(detail_basic_set)
    f.close()
```





# 3. 네이버 영화검색 API

\(1) 영화명을 통해 요청합니다.

(2) 영화별로 다음과 같은 내용을 저장합니다. 

- 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하이퍼텍스트 link , 유저 평점

(3) 해당 결과를 movie_naver.csv에 저장합니다.

```python
#(3)
f = open('movie.csv','r',encoding='utf-8')
movies = csv.reader(f)
mv_nm = [(li[0],li[1]) for li in movies]
mv_nm = mv_nm[1:]
f.close()
#(1)
for name in mv_nm:    
    url =f"https://openapi.naver.com/v1/search/movie.json?query={name[1]}&yearfrom=2000&yearto=2019"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.get(url, headers=headers)
    doc = response.json()
    pp(doc)
#(2)
    li = doc.get('items')[0]
    f = open('movie_naver.csv', 'a', encoding="utf-8", newline="")
    search_a = csv.writer(f)
    mo_se = [name[0], li.get('image'), li.get('link'), li.get('userRating')]
    search_a.writerow(mo_se)
    f.close()

```



## 영화 포스터 이미지 저장

(1) 이미지URL

(2) 응답받은 결과를 파일로 저장합니다. 저장시 반드시 wb 옵션으로 저장하시기 바랍니다.

(3) 저장되는 파일명은 images 폴더 내에 영진위 영화 대표코드.jpg 입니다.

``` python
f = open('movie_naver.csv','r',encoding='utf-8')
movie = csv.reader(f)
mv_li = [(li[0],li[1]) for li in movie]
mv_li = mv_li[1:]
f.close()

os.mkdir('images')
os.chdir('C:\\Users\\SOOWON_J\\Project\\movie\\images')

for url in mv_li:
    res = requests.get(url[1])
    ctt = res.content
#(2),(3)
    f = open(f'{url[0]}.jpg','wb')
    f.write(ctt)
    f.close()
```



