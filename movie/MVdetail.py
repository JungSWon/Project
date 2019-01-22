import requests
import wget
import csv
import os 
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=5b51146d5016cacd454419a8e831511c&movieCd=20184105
#api_key = '5b51146d5016cacd454419a8e831511c'
# mv_code = # boxoffice.py에서 가져오기 
api_key = os.getenv('KOBIS_API_KEY')


#code로 boxoffice에서 영화 끌어오기 
f = open('movie.csv','r',encoding='utf-8')
r = csv.reader(f)
r_li = [li[0] for li in r]
r_li = r_li[1:]
f.close()

# 제목 줄 생성
f = open('MVdetail.csv','w',encoding='utf-8',newline='')
mv= csv.writer(f) 
mv.writerow(['code','name_ko','name_en','name_ori','open_on','run_time','janre','director','age_over','actor1','actor2','actor3'])
f.close()


# 소스페이지에서 긁어오기 
# - 영화 code마다 정보 긁어오기 
for cd in r_li:
    detail_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'.format(api_key,cd)
        
    res = requests.get(detail_url)
    details = res.json()
    detail_list = details.get("movieInfoResult").get('movieInfo')

    #내용 줄 채우기, 
    f = open('detail.csv','a',encoding='utf-8', newline='')
    movie_detail_set = csv.writer(f) 
    #info -{영화코드, 영화명(국문), 영화명(영문), 영화명(원문), 개봉연도, 상영시간} 
    detail_basic_set = [cd.get('movieCd'),cd.get('movieNm'),cd.get("movieNmEn"),cd.get("movieNmOg"),cd.get("prdtYear"),cd.get("showTm")]
    # 장르, 감독명, 관람등급, 배우1,2,3(영화에 따라 2명일 수 있음)
    #info={genres-genreNm(복수개), directors-peopleNm, audits-watchGradeNm, actors- peopleNm(3명까지)}
    #장르
    genr_str = ''   
    for g in cd.get('genres'):
        genr_str += g.get('genreNm') + '/'
    detail_basic_set.append(genr_str[:-1]) #마지막'/'빼기
    #감독
    direc_str = ''   
    for d in cd.get('directors'):
        direc_str += d.get('peopleNm') +'/'
    detail_basic_set.append(direc_str[:-1])
    #관람등급
    detail_basic_set.append(cd.get('audits')[0].get('watchGradeNm')[0])
    #배우들 
    i = 0
    for a in cd.get('actors'):
        detail_basic_set.append('peopleNm')
        i+=1
        if i ==3:
            break
    
    movie_detail_set.writerow(detail_basic_set)
    f.close()
    
