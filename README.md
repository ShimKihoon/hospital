## Python + MariaDB + HTML + CSS + JS + JQuery을 이용한 Hospital 관리 Web

### 개발 기한: # 2021/01/21 ~ 02/16 멀티캠퍼스 IoT 프로젝트 반
------------------------------------------------------------------
#### 사용 IDE 및 언어
  1. Pycharm *(Anaconda interpreter)*: Python, HTML, JavaScript, JQuery, CSS
  2. HeidiSQL: MariaDB
  3. ERDCloud: Database table 시각화
  ![ERD](https://user-images.githubusercontent.com/37172546/107967359-5abb7180-6ff0-11eb-8825-2e08ac78a28c.jpg)


  5. template 출처: Bootstrap (https://www.templateshub.net/demo/?theme=Preclinic-Hospital-Bootstrap4-Admin)
  ------------------------------------------------------------------
  
##### 기능 개요
  1. 관리자(의사) 로그인과 방문객 로그인 2가지 모드
  2. 의사 로그인
      1. 환자 추가
      2. 진료 추가
      3. 차트 추가
      4. 병실 현황 및 침상 별 환자 정보 조회
      5. 환자 리스트 조회
  
  3. 방문객(Guest) 로그인
      1. 병실 점유 현황 조회
      2. 의사 목록 조회
      
  4. 로그인 페이지
      
      ![로그인](https://user-images.githubusercontent.com/37172546/107968128-52176b00-6ff1-11eb-9f1a-476d6d920acb.JPG)
      1. 로그인 container를 section화.
      2. Guest 로그인과 의사 로그인 두가지 중 하나 선택
      3. Kakao Map API를 이용해 지도 확대 축소, Marker 표시
  
  5. Database 연결 및 제어: frame 폴더
      1. db.py : DB 접속 제어 기능
      2. sql.py : Data manipulate를 위한 SQL문
      3. table.py : 각 table은 class로 만들어 Python App에서 각 attribute에 접근할 수 있게 한다
      4. util.py : DB에 연결하여 Data 편집 또는 App을 통해 Web page에 출력할 수 있다.
  
  6. base.html: 
      - Web page의 base, 기초 페이지 역할. 
      - 기능별 block과 views.py에서 section contents 호출, 출력
  
  7. Dashboard (index.html)
      1. 침상 점유율 그래프
      2. 질병별 환자 통계
  
  8. Rooms
      1. 층별 section화
      2. 침상 사용 여부에 따라 색상 변화
          - 사용 중: 노랑
          - 빈 침상: 초록
