# 12주차 실습
1. InFluxDB 설치
2. grafana 설치
3. 데이터 시각화 실습
4. 텔레그램 봇 실습

## InfluxDB 설치
1. 라즈베리파이 eth0 down/up
```
  sudo ip link set down && sudo ip link set up
```

2. 라즈베이파이 업데이트
```
  sudo apt update
  sudo apt upgrade
```
3. Repository의 GPG key를 더하기

```
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -

```

4. Repository를 더하기

```
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

5. 프로그램 설치
```
sudo apt update
sudo apt install influxdb
```
6. 프로그램 실행 전 설정
```
sudo systemctl unmask influxdb
sudo systemctl enable influxdb
sudo systemctl start influxdb
```

7. 데이터베이스 만들기
```
$ influx

>create database <데이터베이스이름>
```
```
확인 : show databases 
```


## grafana 설치
1. Add GPG key (of repository)
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
2. Add repository
```
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
3. program install
```
sudo apt update
sudo apt install grafana
```
4. program start
```
sudo service grafana-server start
```
5. influxDB import
```
sudo pip3 install influxdb
```
6. gpio pin map
```
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
```


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
