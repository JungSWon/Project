
import os 
import csv
import requests 

client_id = os.getnv('NAVER_ID')
client_secret = os.getnv('NAVER_SECRET')


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


4. 영화 포스터 이미지 저장 
앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장합니다. 해당 데이
터는 향후 영화 목록에서 포스터 이미지로 사용될 것입니다.

##요청
이미지URL

##응답
응답받은 결과를 파일로 저장합니다. 저장시 반드시 wb 옵션으로 저장하시기 바랍니다.
저장되는 파일명은 images 폴더 내에 영진위 영화 대표코드.jpg 입니다.


movie_code	thumb_url	link_url	user_rating
'''



# movie.csv 에서 li[0] 코드 , li[1] 영어제목 가져오기 
######### 왜????????????  mv_nm = mv_nm[1:] 의 의미가 뭐지 
f = open('movie.csv','r',encoding='utf-8')
movies = csv.reader(f)
mv_nm = [(li[0],li[1] for li in movies)]
mv_nm = mv_nm[1:]
f.close()

f = open('movie_naver.csv','w', encoding='utf-8', mewline='')
movies = csv.writer(f)
movies.writerow(['movie_code','thumb_url','link_url','user_rating'])
f.close()         # 제목 첫행 만들기 


for name in mv_nm:
    
    url =f''
