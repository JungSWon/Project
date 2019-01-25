
import os 
import csv
import requests 
from pprint import pprint as pp

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
mv_nm = [(li[0],li[1]) for li in movies]
mv_nm = mv_nm[1:]
f.close()

f = open('movie_naver.csv','w', encoding='utf-8', newline='')
movies = csv.writer(f)
movies.writerow(['movie_code','thumb_url','link_url','user_rating'])
f.close()         # 제목 첫행 만들기 

'''
호출 
curl "https://openapi.naver.com/v1/search/movie.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&genre=1" \
    -H "X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}" \
    -H "X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}" -v

요청 
> GET /v1/search/movie.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&genre=1 HTTP/1.1
> Host: openapi.naver.com
> User-Agent: curl/7.49.1
> Accept: */*
> X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}
> X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}

응답
<rss version="2.0">
    <channel>
        <title>Naver Open API - movie ::'주식'</title>
        <link>http://search.naver.com</link>
        <description>Naver Search Result</description>
        <lastBuildDate>Wed, 28 Sep 2016 16:40:17 +0900</lastBuildDate>
        <total>2</total>
        <start>1</start>
        <display>2</display>
        <item>
            <title>주마등&lt;b&gt;주식&lt;/b&gt;회사</title>
            <link>http://openapi.naver.com/l?AAADWLQQvCIBzFP83f48h0zh08uK1B0S2IOm7mUEIts0F9+vQQPN77vQfv+dbxI2DXgyTQ9QV4B+2ATNSLMCk9gEjYjlkurFZXflp1rFRw/yXnbEspNk8vqypvPJBRhZsGMrSMY4ySwLSpN5RT3NSYIScO5nxhdzc18cjq0958w8LneKUy8fz6AdRxjD6YAAAA</link><image>http://imgmovie.naver.com/mdi/mit110/0968/96811_P01_142155.jpg</image>
            <subtitle>走馬&amp;amp;#28783;株式&amp;amp;#20250;社</subtitle>
            <pubDate>2012</pubDate>
            <director>미키 코이치로|</director>
            <actor>카시이 유우|쿠보타 마사타카|카지와라 히카리|치요 쇼타|요코야마 메구미|카시와바라 슈지|</actor>
            <userRating>4.50</userRating>
        </item>
        ...
    </channel>
</rss>
'''
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
