# week 06
## 실습 
### 실습 사진
![image](https://github.com/user-attachments/assets/d278c1ef-2010-4ee4-8183-7655c4a7d40c)
![image](https://github.com/user-attachments/assets/dd1dc850-ec18-4c60-8f94-aa09fb2b983e)
![image](https://github.com/user-attachments/assets/bde3ef0a-f2ce-4e7f-b730-24bb827d7442)
### LedToggle library
#### LedToggle.cpp
```cpp
#include "LedToggle.h"

LedToggle::LedToggle(int pin){
	_pin = pin;
	_state = false;
	pinMode(_pin, OUTPUT);
	digitalWrite(_pin, LOW);
}

LedToggle::LedToggle(int pin, unsigned long delayTime){
	_pin = pin;
	_state = false;
	_delayTime = delayTime;
	pinMode(_pin, OUTPUT);
	digitalWrite(_pin, LOW); 
}
//delayTime이 초기화가 안되는 문제 

void LedToggle::toggle(int pin, unsigned long delayTime){
	_state = !_state;
	digitalWrite(_pin, _state ? HIGH : LOW);
	delay(delayTime);
}
```
#### LedToggle.h
```cpp
#ifndef LedToggle_h
#define LedToggle_h

#include "Arduino.h"

class LedToggle{
	public:
		LedToggle(int pin);
		void toggle(int pin, unsigned long delayTime);
		
	private:
		int _pin;
		bool _state;
		unsigned long _delayTime;
};

#endif
```

# 이론 ( 통신의 이해 )
## 통신 시스템
### 구성 요소
1. 송+수신기 : 데이터 처리부+데이터 전송부
2. 메시지(패킷) : 인터넷의 탄생~현재까지 대부분 통신에서 사용
3. 비트레이트(bps) : 초당 전송 가능한 비트 수
4. 보 레이트(baud) : 초당 전송 가능한 펄스/심볼 수
5. 대역폭(Hz) : 대역폭 넓음=빠름=벽 통과 못함=단거리
 
### 종류
1. 유선 통신
    - 동축 케이블, 이중와선(UTP, STP) 등
    - 광케이블(싱글모드(단거리), 멀티모드(장거리))
2. 무선 통신
    - 3000Hz~3000GHz 사이의 전자기파를 이용한 통신
    - 파동의 마루 사이(미터), 마루~마루까지 초당 몇번 전파가 반복되는지 나타내는 주파수(Hz)
    - 주파수가 높을수록 빠르지만 단거리임(벽 통과 잘 못함)
3. 직렬통신
    - 순차적 데이터 전송
4. 병렬통신
    - 병렬로 데이터 전송->선이 여러개 필요
    - 비효율적이고 비싸서 병렬통신은 퇴조중
       
### 통신방식
1. 단방향 통신
2. 양방향 통신
3. 전이중 통신 (무전기)
4. 동기식 통신: 송/수신기가 하나의 신호에 맞춰 동작, TCP(=신뢰성)이랑 비슷함
5. 비동기식 통신: 미리 전송방식을 협의하여 별도의 신호 없이 동작, UDP(=비신뢰성)이랑 비슷함

### 다중화
- 여러 신호를 합쳐 하나의 신호로 묶어 하나의 통신매체로 전송
    1. 주파수 분할 다중화 (주파수 여러개로 신호 보냄)
    2. 시분할 다중화 (시간을 나눔)
       
### 네트워크
- 데이터통신 방식
    1. 유니캐스트 : 송신 1, 수신 1
    2. 멀티캐스트 : 송신 1, 수신 n(미리 정해진 값)
    3. 브로드캐스트 : 송신 1, 수신 n(불특정 다수)
 
- 영역별 네트워크
    1. 개인 통신망(PAN)
    2. 홈 네트워크
    3. 근거리 통신망(LAN)
    4. 도시권 통신망(MAN)
    5. 광역 통신망(WAN)
    6. ![image](https://github.com/user-attachments/assets/bdf9e746-904b-4f66-83a7-9fa0108a513d)
       
- 네트워크 개녕
  - 패킷교환망 : 인터넷망
  - 회선교환망 : 전화기
    
- 네트워크 구성방식
![image](https://github.com/user-attachments/assets/249276c7-70a5-40ee-b628-f8b183c168dd)
1. 스타 토폴로지 
2. 트리 토폴로지 
3. 버스 토폴로지 : 추가/삭제가 쉬움
4. 링   토폴로지 : 추가/삭제 어려움
5. 메시 토폴로지 : 제일 많이 쓰는거(하나가 끊겨도 다른게 연결가능)

#### 인터넷
- 정의
  - 패킷 네트워크와 TCP/IP라는 두 요소로 정의됨
  - 패킷 네트워크:전송할 메시지를 나눠 조각마다 송/수신지 주소 기입, 각각의 조각이 패킷. 패킷들이 독립적으로 네트워크를 이동
  - TCP/IP : 하드웨어나 운영체제 상관없이 통신가능
    
- 서버와 클라이언트
  - P2P : 연결된 모든 컴퓨터가 서버이자 클라이언트 역할 수행
    
- 인터넷 연결장비
  - 허브 : 연결된 포트들에 모두 같은 패킷 전송(이후 처리 하긴하지만 좀 멍청함)
  - 스위치 : 허브의 단점을 보완(패킷을 필요로 하는곳에 효율적으로 전송)
  - 라우터 : 최적 경로를 찾아주는 장비
