import requests
import csv
import os 
from pprint import pprint as pp
from datetime import datetime, timedelta

'''
##요청
1. 주간(월~일)까지 기간의 데이터를 조회합니다.
2. 조회 기간은 총 10주이며, 기준일(마지막 일자)은 2019년 1월 13일입니다.
3. 다양성 영화/상업 영화를 모두 포함하여야 합니다.
4. 한국/외국 영화를 모두 포함하여야 합니다.
5. 모든 상영지역을 포함하여야 합니다.

##결과 
수집된 데이터에서 영화 대표코드 , 영화명 , 해당일 누적관객수 , 해당일 을 기록합니다.
해당일 누적관객수 는 중복시 최신 정보를 반영하여야 합니다. 
예) 영화 아쿠아맨이 20190113 기준 50,000명이고, 20190106 기준 5,000명이면 50,000명이 저장되어야 합니다.
해당 결과를 boxoffice.csv 에 저장합니다.
'''


api_key = os.getenv('KOBIS_API_KEY') 
lastday = datetime(2019, 1, 13)

f = open('boxoffice.csv','w',encoding='utf-8',newline='') #newline으로 결과.csv 줄띄움 없애기  
movie = csv.writer(f)   
movie.writerow(['movie_code','titile','audience','record_at'])     #첫 제목행 만들기 
f.close()    # movie.csv생성 

name_li = [] 
for i in range(10):
    today = lastday.strftime('%Y%m%d')

    rank_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={api_key}&targetDt={today}&weekGb=0'

    res = requests.get(rank_url)   
    ranking = res.json() # url들어가면 보이는 소스   
    rank_list = ranking.get('boxOfficeResult').get('weeklyBoxOfficeList')        

    for li in rank_list: # 소스에서 받은 자료들을 
        f = open('boxoffice.csv','a',encoding='utf-8', newline='') #만들어진 movie.csv에 추가할거다 
        movie_set = csv.writer(f)   
        list_set = [li.get('movieCd'),li.get('movieNm'),li.get('audiAcc'),today] 
        if li.get('movieNm') not in name_li:
            movie_set.writerow(list_set)
            name_li.append(li.get('movieNm'))
        f.close()
    lastday += timedelta(days= -7)
    
    


'''
위에서 수집한 영화 대표코드를 활용하여 상세 정보를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 영
화 정보로 활용될 것입니다.

##결과 
영화별로 다음과 같은 내용을 저장합니다.
영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 개봉연도 , 상영시간 , 장르 , 감독
명 , 관람등급 , 배우1 , 배우2 , 배우3
배우의 경우 최대 3명입니다. 영화에 따라 1~2명일 수도 있습니다.
해당 결과를 movie.csv에 저장합니다.
'''


#boxoffice에서 영화 끌어오기 
f = open('boxoffice.csv','r',encoding='utf-8')
r = csv.reader(f)
r_li = [li[0] for li in r]
r_li = r_li[1:]
f.close()

# 제목 줄 생성
f = open('movie.csv','w',encoding='utf-8',newline='')
mv= csv.writer(f) 
mv.writerow(["movie_code", "movie_name_ko", "movie_name_en", "movie_name_og", "prdt_year", "showTm", "genres", "directors", "watch_grade_nm", "actor1", "actor2", "actor3"])
f.close()


# 소스페이지에서 긁어오기 
# - 영화 code마다 정보 긁어오기 
for cd in r_li:
    detail_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={api_key}&movieCd={cd}'
        
    res = requests.get(detail_url)
    details = res.json()
    dtls = details.get("movieInfoResult").get('movieInfo')

    #내용 줄 채우기, 
    f = open('movie.csv','a',encoding='utf-8', newline='')
    movie_detail_set = csv.writer(f) 
    #info -{영화코드, 영화명(국문), 영화명(영문), 영화명(원문), 개봉연도, 상영시간} 
    detail_basic_set = [dtls.get('movieCd'),dtls.get('movieNm'),dtls.get("movieNmEn"),dtls.get("movieNmOg"),dtls.get("prdtYear"),dtls.get("showTm")]
    # 장르, 감독명, 관람등급, 배우1,2,3(영화에 따라 2명일 수 있음)
    #info={genres-genreNm(복수개), directors-peopleNm, audits-watchGradeNm, actors- peopleNm(3명까지)}
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
    #배우들 
    i = 0
    for a in dtls.get('actors'):
        detail_basic_set.append(a.get('peopleNm'))
        i+=1
        if i ==3:
            break
    
    movie_detail_set.writerow(detail_basic_set)
    f.close()
    

client_id = os.getenv('NAVER_ID')
client_secret = os.getenv('NAVER_SECRET')


'''
3. 네이버 영화검색 API
앞서 영진위에서 얻은 영화명(국문)을 바탕으로 네이버 영화 검색 API를 통해 추가적인 데이터를 수집합니다. 해
당 데이터는 향후 영화평점서비스에서 기준 평점 및 영화 포스터 썸네일로 활용될 것입니다.

API 정보 :  https://developers.naver.com/docs/search/movie/

##요청
영화명을 통해 요청합니다.

##응답
영화별로 다음과 같은 내용을 저장합니다. 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하
이퍼텍스트 link , 유저 평점
해당 결과를 movie_naver.csv에 저장합니다.


movie_code	thumb_url	link_url	user_rating
'''



# movie.csv 에서 li[0] 코드 , li[1] 영어제목 가져오기 
f = open('movie.csv','r',encoding='utf-8')
movies = csv.reader(f)
mv_nm = [(li[0],li[1]) for li in movies]
mv_nm = mv_nm[1:]
f.close()

f = open('movie_naver.csv','w', encoding='utf-8', newline='')
movies = csv.writer(f)
movies.writerow(['movie_code','thumb_url','link_url','user_rating'])
f.close()         # 제목 첫행 만들기 

for name in mv_nm:
    
    url =f"https://openapi.naver.com/v1/search/movie.json?query={name[1]}&yearfrom=2000&yearto=2019"

    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.get(url, headers=headers)
    doc = response.json()

    pp(doc)

    li = doc.get('items')[0]
    f = open('movie_naver.csv', 'a', encoding="utf-8", newline="")
    search_a = csv.writer(f)
    mo_se = [name[0], li.get('image'), li.get('link'), li.get('userRating')]
    search_a.writerow(mo_se)
    f.close()

    
'''
4. 영화 포스터 이미지 저장
앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장합니다. 
해당 데이터는 향후 영화 목록에서 포스터 이미지로 사용될 것입니다.

###요청
이미지 URL

###응답
응답받은 결과를 파일로 저장합니다. 저장시 반드시 wb 옵션으로 저장하시기 바랍니다.
저장되는 파일명은 images 폴더 내에 영진위 영화 대표코드.jpg 입니다.
'''

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
    f = open(f'{url[0]}.jpg','wb')
    f.write(ctt)
    f.close()