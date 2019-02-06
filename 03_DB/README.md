#  Project 03 - DB 

목표 

- 영진위 API를 활용하여 수집한 데이터를 데이터베이스에 반영하기
- SQL을 통한 데이터베이스 조작
- 단일 테이블에서의 데이터 조작
- 영화추천서비스와 관련된 다양한 검색 쿼리 작성하기 

준비사항

- SQL 활용 환경 설정
- 영화 데이터 베이스
  -  `boxoffice.csv`로 제공된 100주간 박스오피스 TOP10에 들어간 적이 있었던 영화 총 360개의 정보를 활용합니다. 

공통사항 

- 순서에 맞게 쿼리문을 작성합니다. 





##  1. 테이블 구성하기 

- 파일명 : 01_create_table.sql

### 1) 테이블을 만듭니다.

####  	(1-1) 테이블 이름:  movies

####  	(1-2) 스키마는 아래 표와 같습니다.

| Column     | Type    |
| ---------- | ------- |
| 영화코드   | 정수,PK |
| 영화이름   | 문자열  |
| 관람등급   | 문자열  |
| 감독       | 문자열  |
| 개봉연도   | 숫자    |
| 누적관객수 | 정수    |
| 상영시간   | 정수    |
| 제작국가   | 문자열  |
| 장르       | 문자열  |

###  2) 설정

#### 	(1-1) header 설정

``` sql
CREATE TABLE movies (
    영화코드 INTEGER PRIMARY KEY,
    영화이름 TEXT NOT NULL,
    관람등급 TEXT NOT NULL,
    감독 TEXT NOT NULL,
    개봉연도 INTEGER NOT NULL,
    누적관객수 INTEGER NOT NULL,
    상영시간 INTEGER NOT NULL,
    제작국가 TEXT NOT NULL,
    장르 TEXT NOT NULL
);
```

#### 	(1-2) mode 설정

```sql
.mode csv
.import boxoffice.csv movies
.mode column
.headers on 
```

#### 	(1-3) 추가 설정 확인

​		- `.help` 명령어를 통해 가능한 mode를 확인 해봅니다.	

### 3) 전체 데이터 출력

```sql
SELECT * FROM movies;
```



## 2. CRUD 조작하기 

- 파일명 : 02_crud.sql

### 1) 누락 정보 추가 

- 아래 레코드를 테이블에 추가 합니다.

| Column     | Type           |
| ---------- | -------------- |
| 영화코드   | 20182530       |
| 영화이름   | 극한직업       |
| 관람등급   | 15세이상관람가 |
| 감독       | 이병헌         |
| 개봉연도   | 20190123       |
| 누적관객수 | 3138467        |
| 상영시간   | 111            |
| 제작국가   | 한국           |
| 장르       | 코미디         |

``` sql
INSERT INTO movies VALUES (20182530,'극한직업','15세이상관람가','이병헌',20190123,3138467,111,'한국','코미디');
```



###  2) 과거 데이터 삭제

- 영화코드가 20040521인 데이터를 출력합니다.

  ```sql
  SELECT * FROM movies WHERE 영화코드 IS 20040521;
  ```

- 해당 데이터를 삭제합니다. 

  ```sql
  DELETE FROM movies WHERE 영화코드 IS 20040521;
  ```

###  3) 변경 확인

- 영화코드가 20185124인 데이터를 출력합니다. 

  ``` sql
  SELECT * FROM movies WHERE 영화코드 IS 20185124;
  ```

- 공란으로 되어 있는 컬럼에 값을 '없음'으로 수정합니다. 

  - `.nullvalue STRING      Use STRING in place of NULL values`

    위 문법을 사용 하여 아래와 같이 수정을 시도해보았습니다. 

    ```sql
    .nullvalue '없음'
    ```

    그러나 대체되지 않으므로 아래와 같이 수정합니다.

  - ```sql
    UPDATE movies SET 감독 = '없음' WHERE 영화코드 = 20185124;
    ```

- 해당 데이터의 감독이 변경되었는지 확인합니다.

  ```sql
  SELECT 감독 FROM movies WHERE 영화코드 IS 20185124;
  ```

  



##  3. 원하는 데이터 찾기 

- 파일명 : 03_select.sql

####  1) 조건에 맞게 출력합니다. 

- 상영시간이 150분 이상인 영화이름

  ```sql
  SELECT 영화이름 FROM movies WHERE 상영시간 >= 150;
  ```

- 장르가 애니메이션인 영화코드와 영화이름

  ```sql
  SELECT 영화이름 FROM movies WHERE 장르 = '애니메이션';
  ```

- 제작국가가 덴마크이고 장르가 애니메이션인 영화이름

  ```sql
  SELECT 영화이름 FROM movies WHERE 제작국가 = '덴마크' and 장르 = '애니메이션';
  ```

- 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수

  ```sql
  SELECT 영화이름 , 누적관객수 FROM movies WHERE 누적관객수 >= 1000000 and 관람등급 = '청소년관람불가';
  ```

- 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화의 모든 정보\

  ```sql
  SELECT * FROM movies WHERE 개봉연도 >= 20000101 and 개봉연도 <= 20091231 ;
  ```

- 장르를 중복 없이 출력

  ```sql
  SELECT 장르 FROM movies GROUP BY 장르 HAVING COUNT (장르) > 1;
  ```

  

##  4. Expression 활용

- 파일명: 04_expression.sql

#### 1) 조건에 맞게 출력합니다.

- 모든 영화의 총 누적관객수

  ```sql
  SELECT SUM(누적관객수) FROM movies;
  ```

- 가장 많은 누적관객수인 영화이름과 누적관객수

  아래 두가지 방법으로 출력할 수 있다.

  ```sql
  SELECT 영화이름, 누적관객수 FROM movies ORDER BY 누적관객수 DESC LIMIT 1;
  ```

  ```sql
  SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수=(SELECT MAX(누적관객수) FROM movies);
  ```

- 가장 상영시간이 짧은 영화의 장르와 상영시간

  - 최소값을 가진 열이 다수라면 모두 출력한다.

    ``` sql
    SELECT 장르, 상영시간 FROM movies WHERE 상영시간=(SELECT MIN(상영시간) FROM movies);
    ```

    ``` terminal
    장르           상영시간
    ---------------  ------------
    애니메이션  57          
    액션           57  
    ```

  - 가장 작은 수를 가진 열중 하나만 출력한다. 

    ```sql
    SELECT 장르, 상영시간 FROM movies ORDER BY 상영시간 ASC LIMIT 1;
    ```

    ```terminal
    장르           상영시간
    ---------------  ------------
    애니메이션  57 
    ```

- 제작국가가 한국인 영화의 평균 누적관객수

  ```sql
  SELECT AVG(누적관객수) FROM movies WHERE 제작국가 = '한국';
  ```

- 관람등급이 청소년관람불가인 영화의 개수

  ```sql
  SELECT COUNT(영화코드) FROM movies WHERE 관람등급 = '청소년관람불가';
  ```

- 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수

  ```sql
  SELECT COUNT(영화이름) FROM movies WHERE 장르 = '애니메이션' and 상영시간>= 100 ;
  ```

  


##  5. 정렬

- 파일명 05_order.sql

####  1) 조건에 맞게 출력과 정렬합니다.

- 누적관객수 상위 5개 영화의 모든 데이터

  ```sql
  SELECT *FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
  ```

- 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개만 출력

  ```sql
  SELECT * FROM movies WHERE 장르 = '애니메이션' ORDER BY 제작국가 ASC , 누적관객수 DESC LIMIT 10;
  ```

- 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력

  ```sql
  SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;
  ```

  









**아래와 같이 결과물을 제출합니다.** 

> 03_db/
> ​	README.md
> ​	01_create_table.sql
> ​	02_crud.sql
> ​	03_select.sql
> ​	04_expression.sql
> ​	05_order.sql
> ​	pjt.sqlite3