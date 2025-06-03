# 14주차 수업내용 ( 이론 )
1. Wi-Fi
2. ZigBee

## Wi-Fi
1. IEEE 표준에 따른 비교<br/>
   ![image](https://github.com/user-attachments/assets/a976a7cf-3e02-4434-b56f-ebb974b9a099)
   - 국제표준 = 802.11
   - 주파수 2.4 GHz ~ 5 GHz
   - 환경에 따라 전송/변조 방식, 도달거리가 다름
   - IEEE는 전자공학 등 여러 분야의 전문가들의 위원회(여러가지 함)
     
2. Wi-FI 구성
   - AP(Access Point) + STA(station)
   - AP : 유무선 공유기
   - STA : 노트북, 스마트폰 ( 단말기 )
     
3. Wi-Fi 서비스 셋
   - BSS(basic service set)
     - AP 없음 : ad hoc ( IOT device 등 )
       + device 최초 연결 시 ad hoc 사용, 설정. 이후 infrastruture로 사용
     - AP 있음 : infrastructure ( 일반적 사용)
   - ESS(extended service set)
     - 약간 고급형, AP 간 로밍
     - 학교 / 기업 등 BSS 여러개 쓰는데서 사용
       
4. MAC
   - MAC : 제조사에서 부여한 unique 식별번호
   - MAC 방식
     - DCF(distrivuted coordination function)
       - 분산식, CSMA/CA, STA에서 사용
     - PCF(point coordination function)
       - 중앙집중식, polling
       - 하나의 point에서 STA마다 물어봄(coordination)
   - MAC data frame
     ![image](https://github.com/user-attachments/assets/b1af3260-fd9f-4271-9ec3-317aa5c1ae88)<br/>
     1. 4종류의 주소
     2. Frame body에 데이터가 들어감
        
5. 주소 체계<br/>
   ![image](https://github.com/user-attachments/assets/4d593860-ea76-4996-81fc-ae1bc8aa762b)<br/>
   1. case 1 : BSS-ID가 3번째에 들어감 (SSID)
   2. case 2 : 유선 to 무선(인터넷)
   3. case 3 : 무선 to 유선
   4. case 4 : 무선 to 무선
      
6. CSMA-CA
   1. CS(carrier sence) : 네트워크를 누가 사용중인지 알아냄
   2. MA(multiple access) : 네트워크가 비어있으면 누구든 사용가능
   3. CA(collision avoidance : 충돌 회피
   - 무선통신은 구조적으로 충돌을 감지 못함(hidden terminal problem), 따라서 이걸 써서 충돌을 회피(CA)
   - 충돌(collision)
     - 여러 노드가 같은 시간대에 같은 노드에 패킷 전송
     - Hidden terminal problem<br/>
       ![image](https://github.com/user-attachments/assets/89a30d8c-d4d3-4493-b1f5-215bc4d680bc)<br/>
       - 신호 전송 범위 다름 >> B와 C는 서로 알 수 없음 >> RTS,CTS 사용(CA)
   - 일반적 동작 방식
     - 경합 방식 : 기기들끼리 경쟁<br/>
       ![image](https://github.com/user-attachments/assets/a4b4fffb-b060-4aea-9792-c7f66a2be8a1)<br/>
       1. 기기가 데이터 송신중인지 감지
       2. 송신중이면 대기(BACK-OFF)
       3. 랜덤한 시간 기다렸다가 반송파(RTS) 감지 >> 충돌 감지 못하니까 실험하는거
   - 다른 방식
     - CSMA-CD : 이더넷(유선)에서 사용, 충돌 감지
       - CA는 비용이 적으나 데이터 전송 지연 발생가능


## ZigBee
1. 구조
   - 스택 : 프로토콜, 소프트웨어의 집합체<br/>
![image](https://github.com/user-attachments/assets/9edff8c6-9c67-49a9-9fa0-b4f6cac7e5ec)<br/>
   - zigbee stack : 직비에서 정의한 프로토콜의 구현
     
2. 물리 계층<br/>
   ![image](https://github.com/user-attachments/assets/546988f6-d154-47bb-a44a-75d025103d0a)<br/>
   - IEEE 802.15.4 사용
   - 3개의 밴드, 27개의 채널(8-900 대)
   - 2.4GHz 대역에서 무선 랜과 겹치는 채널 있음 (25~26번은 겹치지 않음)
   - DSSS(직접 시퀀스 확산 스펙트럼 변조 방식)
     - 슈도 랜덤(스프레드 코드)을 사용, 반송파에 변형을 주어 사용
       
3. MAC 계층
   - 세 종류의 기기
     - NC(network coordinator) : 네트워크 관리
     - FFD(full function device)
     - RFD(reduced function device) : 축소된 기능
   - MAC 선택 샤양
     - 비콘 없음(non-slotted)
     - 비콘 있음(slotted)
   + zigbee의 CSMA-CA
     - RTS,CTS 사용안함 ( 비용 싼거 추구 )
     - 비콘
       - 슈퍼프레임(비콘 + CAP + CFP)
         - 항상 비콘으로 시작, 비콘은 NC 가 송신
         - CAP(경쟁구간) : 시간에 맞춰 송수신
         - CFP(경쟁없는구간) : NC가 슬롯 예약해 기기들이 송수신
         - 비콘에 따라 시간동기화 해서 slot단위 송수신 가능
         - GTS 가 어느 기기에 할당됐는지 알수있
         - 비활성구간 : 전력 사용 적게(zigbee는 저전력 추구)하기위해 송수신기 끔
    - MAC 프레임 종류
      - 데이터 프레임<br/>
      ![image](https://github.com/user-attachments/assets/79c7b8fb-e0b2-448d-ba1d-3d8bf1edd03b)<br/>
        1. 시퀀스 넘버 필드 : 전송 확인하기 위해 사용
        2. Payload : 실 데이터 실리는곳
    - 주소
      - PanID : 0-2바이트(같은 기기에서는 0바이트)
      - 목적지/근원지 주소 : 직비끼리는 2, 외부에선 8바이트
      - 주소 할당 기법<br/>
          ![image](https://github.com/user-attachments/assets/9a8be959-78ab-4e49-9f46-7b7db0343b2a)<br/>
        - 분산 주소 할당 기법 : 16비트 주소 할당 >> tree구조로 부모가 자식에게 할당<br/>
          ![image](https://github.com/user-attachments/assets/794d42d5-bf0f-4b6f-9b91-93356e8f245b)<br/>
          - 최대 자식의 수 = Cm(3)
          - 트리의 길이 = Lm(3)
          - 라우터(공유기라고 생각) 최대 길이 = Rm(3)
          - 부모->첫째 자식은 무조건 1
          - 이후에는 Cskip(d)를 더해서 할당 ex) 1(1번), 14(1번+13), 27(1번+13+13)
