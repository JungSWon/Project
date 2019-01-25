import requests
import csv
import os 
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
<<<<<<< HEAD
        list_set = [li.get('movieCd'),li.get('movieNm'),li.get('audiAcc'),today]
        if li.get('movieNm') not in name_list:
            movie_set.writerow(list_set)
            name_list.append(li.get('movieNm'))
=======
        list_set = [li.get('movieCd'),li.get('movieNm'),li.get('audiAcc'),today] 
        if li.get('movieNm') not in name_li:
            movie_set.writerow(list_set)
            name_li.append(li.get('movieNm'))
>>>>>>> 92264ec4a198f6d670101cde9d450fd95eff3f2f
        f.close()
    lastday += timedelta(days= -7)
    
    

# rank_list = [(g.get('movieCd'),g.get('movieNm'),g.get('audiAcc'),ranking.get('yearWeekTime')) for g in ranking.get("weeklyBoxOfficeList")]


# print(get_rank())
    # return [(g.get('movieCd'),get('movieNm'),get('audiAcc'),g.get('yearWeekTime')) for g in ranking]
    #해당일 관객수 = 'audiCnt'
    #조회주차에 해당하는 연도와 주차 : yearWeekTime