# week 2
+ InfluxDB ~ arduino CONNECT
+ localhost DB 
+ using pip3, module install ( pip3 install ~~~~ )


## arduino program
```c
//미세먼지 농도 측정 프로그램
int Vo = A0;
int V_led = 12;

float Vo_value = 0;
float Voltage = 0;  
float dustDensity = 0;

void setup() {
  Serial.begin(9600);
  pinMode(V_led, OUTPUT);
  pinMode(Vo, INPUT);
}

void loop() {
  //모든 정치가 high=on은 아님
  digitalWrite(V_led, LOW);
  delayMicroseconds(280);
  Vo_value = analogRead(Vo);
  delayMicroseconds(40);
  digitalWrite(V_led, HIGH);
  delayMicroseconds(9680);

  //해당 PCB는 미세먼지값을 전압으로 출력하므로 다음과 같은 식 삽입
  //세부값은 DATASHEET 참고
  Voltage = Vo_value*5.0 / 1023.0;
  dustDensity = (Voltage - 0.5)/0.005;

  Serial.print("dust=" );
  Serial.println(dustDensity);

  delay(1000);
}
```


## Influx DB connect ( pycharm )
```
