import requests
import csv
import os 

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


api_key = os.getenv('KOBIS_API_KEY')


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
    
