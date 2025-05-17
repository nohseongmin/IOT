# 9주차 실습
1. OPENCV2 설치
2. Telegram Bot API KEY로 연동
3. Bot Sample - Timerbot 사용 실습

## OPENCV2 설치
1. openCV2 Doc >> https://github.com/opencv/opencv
2. 전체를 설치하기에는 용량이 너무 큼. 파이썬 라이브러리로 파이썬에서만 동작할 수 있도록 설치.<br/>
```pip3 install opencv-python```

## Telegram Bot API KEY로 연동
1. Telegram botfather 로 봇 생성, API KEY 복사
2. samples - timerbot.py 의 API KEY를 복사한 API KEY로 대체

## Bot Sample - Timerbot 사용 실습
1. Timerbot.py 실행. ( 봇 구동 ) 
2. Telegram bot과 채팅 -> /start로 구동 확인
![KakaoTalk_20250518_004431105](https://github.com/user-attachments/assets/726b0e25-bd34-4205-92a4-40bf5fdd7f54)
3. 정상 작동 확인, timerbot.py 파일 내의 핸들러 수정 및 적용 확인
4. /set <time> 에 사진 찍어서 보내는 기능 추가 ( alarm 기능에 사진 찍는 기능을 추가해 설정한 시간이 다 되면 사진을 찍어 Telegram bot으로 전송하는 방식 )
5. 채팅을 통한 기능 확인<br/>
![KakaoTalk_20250518_004431538](https://github.com/user-attachments/assets/a80a1208-7d28-456a-aa63-58ebec9435ba)
![KakaoTalk_20250518_010806732](https://github.com/user-attachments/assets/b4235255-5df1-4ac9-8ef9-1847a714a4a9)
