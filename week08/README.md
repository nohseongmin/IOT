# 8주차 수업내용
## 시험 review
1. #define은 전처리 단계에서 실행 / const는 컴파일 시점
2. 협업 필터링 = 군집화를 배제

## 라즈베리파이 OS 설치
https://www.raspberrypi.com/software/
</br>
![image](https://github.com/user-attachments/assets/09629469-9f46-4420-9b6d-bf23b4f8fbe5)

## 라즈베리파이 세팅
1. 네트워크 설정
   - 현재 네트워크 환경에 맞게 IPV4 설정
   - 연결 방식을 수동으로 변경 후 적용
  
2. 한국어 패치
   - 최초 진입 시 영어 선택, 이후 키보드 설정 변경 ( 최초에 한글 선택 시 깨질 수 있음 )
   - 이후 터미널 진입, 명령어 입력
```
sudo apt-get install fonts-unfonts-core -y
sudo apt-get install ibus ibus-hangul -y
sudo reboot
```
 - 재시작 전 좌측 상단 라즈베리파이 설정에서 언어 및 시간 한국어, 서울로 변경
