import requests
import wget
import csv
import os 
from pprint import pprint as pp






api_key = os.getenv('KOBIS_API_KEY')
rank_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={api_key}&targetDt=20190113&weekGb=0'

f = open('movie.csv','w',encoding='utf-8',newline='') #newline으로 결과.csv 줄띄움 없애기  
movie = csv.writer(f) 
movie.writerow(['code','name','record','at'])
f.close()

res = requests.get(rank_url)
ranking = res.json() # url들어가면 보이는 소스 
pp(ranking)
rank_list = ranking.get('boxOfficeResult').get('weeklyBoxOfficeList')


for li in rank_list:
    f = open('movie.csv','a',encoding='utf-8', newline='')
    movie_set = csv.writer(f) 
    list_set = [li.get('movieCd'),li.get('movieNm'),li.get('audiAcc')]
    movie_set.writerow(list_set)
    f.close()
    

# rank_list = [(g.get('movieCd'),g.get('movieNm'),g.get('audiAcc'),ranking.get('yearWeekTime')) for g in ranking.get("weeklyBoxOfficeList")]


# print(get_rank())
    # return [(g.get('movieCd'),get('movieNm'),get('audiAcc'),g.get('yearWeekTime')) for g in ranking]
    #해당일 관객수 = 'audiCnt'
    #조회주차에 해당하는 연도와 주차 : yearWeekTime