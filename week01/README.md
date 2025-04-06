# week 1
+ tinkercad
+ arduino install + practice

## tinkercad practice
![image](https://github.com/user-attachments/assets/d4b555c5-0abb-450e-9b19-2a0f02ec02c6)

## arduino practice
```c
//C언어처럼 활용가능
#define TRIG 13 
#define ECHO 12

//전역변수도 마찬가지
int led_R = 7; 
int led_G = 8;

//여기서 pinmode로 in/out 설정 먼저 해줘야함
void setup()
{
#시리얼 포트 연결 (9600 속도로)
  Serial.begin(9600);
//초음파 센서 관련 TRIG와 ECHO 설정
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(led_R, OUTPUT);
  pinMode(led_G, OUTPUT);
}

//반복실행부분
void loop()
{
//거리값 계산 전 선언
  long duration, distance;

//low로 시작하는 이유는 그렇게 설계되었기 떄문(datasheet 참고)
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

//datasheet에 있는대로 설정 (외울필요 없음)
  duration = pulseIn(ECHO, HIGH);
  distance = duration /58.2;

//거리가 100이상일때 led_R켜고 이외는 led_G 켜기
  if (distance>=100){
    digitalWrite(led_R, HIGH);
    digitalWrite(led_G, LOW);
    
  }
  else {
    digitalWrite(led_R, LOW);
    digitalWrite(led_G, HIGH);
  }
  delay(1000);

  /*
  거리값 출력 내용
  Serial.println(distance);
  Serial.println(" cm");
  delay(1000);
  */
  
  /* 
  led_R과 led_G 번갈아 켜는 내용
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  */
    
}
```
