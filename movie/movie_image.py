import os
import csv
import requests
from pprint import pprint as pp


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

# os.mkdir('images')
os.chdir('C:\\Users\\SOOWON_J\\Project\\movie\\images')

for url in mv_li:
    res = requests.get(url[1])
    ctt = res.content
    f = open(f'{url[0]}.jpg','wb')
    f.write(ctt)
    f.close()
