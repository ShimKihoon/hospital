## Python + MariaDB + HTML + CSS + JS + JQuery을 이용한 Hospital 관리 Web

### 개발 기한: 2021/01/21 ~ 02/16 멀티캠퍼스 IoT 프로젝트 A반
###### 최종수정: 2021-02-16 심기훈
------------------------------------------------------------------
#### 사용 IDE 및 언어
  1. Pycharm *(Anaconda interpreter)*: Python, HTML, JavaScript, JQuery, CSS
  2. HeidiSQL: MariaDB
  3. ERDCloud: Database table 시각화
        
        ![ERD](https://user-images.githubusercontent.com/37172546/107970973-32824180-6ff5-11eb-8905-f280935409ff.jpg)

  4. template 출처: Bootstrap (https://www.templateshub.net/demo/?theme=Preclinic-Hospital-Bootstrap4-Admin)
  ------------------------------------------------------------------
  
#### 기능 개요
  1. **관리자(의사) 로그인과 방문객 로그인 2가지 모드**
  2. **의사 로그인**
      1. 환자 추가
      2. 진료 추가
      3. 차트 추가
      4. 병실 현황 및 침상 별 환자 정보 조회
      5. 환자 리스트 조회
  
  3. **방문객(Guest) 로그인**
      1. 병실 점유 현황 조회
      2. 의사 목록 조회
      
  4. **로그인 페이지**      
      ![로그인](https://user-images.githubusercontent.com/37172546/107971118-6493a380-6ff5-11eb-8002-1c97426ce639.JPG)
      1. 로그인 container를 section화.
      2. Guest 로그인과 의사 로그인 두가지 중 하나 선택
      3. Kakao Map API를 이용해 지도 확대 축소, Marker 표시
  
  5. **Database 연결 및 제어: frame 폴더**
      1. db.py : DB 접속 제어 기능
      2. sql.py : Data manipulate를 위한 SQL문
      3. table.py : 각 table은 class로 만들어 Python App에서 각 attribute에 접근할 수 있게 한다
      4. util.py : DB에 연결하여 Data 편집 또는 App을 통해 Web page에 출력할 수 있다.
  
  6. **base.html:** 
      - Web page의 base, 기초 페이지 역할. 
      - 기능별 block과 views.py에서 section contents 호출, 출력
  
  7. **Dashboard (index.html)**
  
        ![dash](https://user-images.githubusercontent.com/37172546/107970937-2302f880-6ff5-11eb-922b-ef908c1bd556.JPG)      
      1. 침상 점유율 그래프
      2. 질병별 환자 통계
  
  8. **Rooms (hospitalstructure.html)**
  
      ![room](https://user-images.githubusercontent.com/37172546/107970852-06ff5700-6ff5-11eb-953a-72df1fdf4eb6.jpg)
      1. 층별 section화 및 병실 클릭 시 popup 형태로 출력
      2. 침상 사용 여부에 따라 색상 변화
          - 사용 중: 노랑
          - 빈 침상: 초록
      3. 병실 만석 여부 확인 가능
          - 병실 만석: 노랑
          - 빈 침상有: 초록
      4. 사용 중인 침상에 Tooltip 형태로 이용자 정보 출력

  9. **Doctors list**
  
        ![doc](https://user-images.githubusercontent.com/37172546/107971561-f9969c80-6ff5-11eb-83ea-4b9fe1a540d1.jpg)
      1. Grid / Widget 형태로 DB - DoctorDb에서 목록 출력
      2. selectbox로 분과별 의사 시각화
      3. treatment, chart 추가 가능(로그인 한 자신의 계정만 가능, 타 의사 정보 수정 불가)
      4. Doctor 추가 기능

  10. **treatment, chart**
  
        ![chart](https://user-images.githubusercontent.com/37172546/107971891-6316ab00-6ff6-11eb-8bbd-35afd435fa20.JPG)
      1. 담당 의사, 병명, 질병 등 정보 입력
      
  11. **Patients**
  
        ![pat](https://user-images.githubusercontent.com/37172546/107971712-2945a480-6ff6-11eb-82ec-5b9bd2bed358.jpg)
      1. DB와 연동해 patients list를 출력
      2. 의사로 로그인 한 경우 환자 추가 및 차트 조회 가능
  
