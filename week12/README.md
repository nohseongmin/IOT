# 12주차 실습
1. InFluxDB 설치
2. grafana 설치
3. 데이터 시각화 실습
4. 텔레그램 봇 실습

## InfluxDB 설치
1. 설치
```
 sudo apt-get update && sudo apt-get install influxdb -y
```
2. 서비스 스타트
```
sudo service influxdb status
```
3. 데이터베이스 생성
```
>create database <데이터베이스이름>
확인 : show databases 
```

## grafana 설치
1. 설치
```
sudo apt-get install -y apt-transport-https software-properties-common wget
```
2. 서버 스타트
```
sudo systemctl start grafana-server
```
3. 라이브러리 설치
```
pip install influxdb
```
4. 접속
  - 크롬미니 >> localhost:3000
  - 로그인

## 데이터 시각화 실습
1. arduino의 미세먼지 센서 통해 데이터를 받아옴
![KakaoTalk_20250523_193516824](https://github.com/user-attachments/assets/1d4ce16f-7ee2-4e3c-b0fa-170b43aa919b)
2. 데이터를 grafana에서 InfluxDB(Data source)로 받음
![KakaoTalk_20250523_193517276](https://github.com/user-attachments/assets/7d055004-eae8-4a9a-82da-4ca372b77188)
3. grafana의 DashBoard로 시각화
![image](https://github.com/user-attachments/assets/884abe12-c8e7-4abf-bee3-04b10145d8fc)


## 텔레그램 봇 실습
1. telegrambot/example/timer.py 에 api키 삽입
2. /dust 핸들러 추가
![image](https://github.com/user-attachments/assets/c2b902c8-0f4e-49c5-9a37-706db0480baa)
3. 함수 구현
![image](https://github.com/user-attachments/assets/6da4b0bb-c206-4014-8e05-fc04d8e49375)
4. 테스트<br/>
![KakaoTalk_20250523_194904131](https://github.com/user-attachments/assets/24971153-67a4-4d27-917a-810b1d6f5ff5)
