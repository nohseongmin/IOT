# IOT week3 practice
+ I2C protocol 
  - Inter-Integrated Circuit
  - 단 이중통신 사용
  - SDA(data), SCL(clock) 각각 1개의 선만 있으면 통신가능
  - 하나의 master에 112개(2^7-15(예약))의 slave(센서) 가능
  - 풀업 저항 필요(신호선을 항상 high(1)로 유지하는 역할) = LOW를 제어 가능하기 때문


# LCD.C
+ LCD ~ arduino connect ( LiquidCrystal_I2C )
```c++
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

//similar with java(lang)'s class
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup(){
  lcd.init();
  lcd.backlight();
  lcd.print("LCD init");
  delay(2000);
  lcd.clear();
}

void loop() { 
  lcd.setCursor(0,0);
  lcd.print("Hello, World!!");
  
  for (int position =0; position < 16; position++){
    lcd.scrollDisplayLeft();
    delay(150);
  }
}
```

# LCD_practice.c
 + 1주차 초음파 센서 내용을 더해 응용
```c++
//초음파 센서로 거리값을 받아 LCD로 출력
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define TRIG 13 
#define ECHO 12

float Vo_value = 0;
float Voltage = 0;  
float dustDensity = 0;
long duration, distance;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.print("LCD init");
  delay(2000);
  lcd.clear();

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn(ECHO, HIGH);
  distance = duration /58.2;

  lcd.setCursor(0,0);
  lcd.println(distance);
  Serial.println(distance);
  delay(1000);
  lcd.clear();
  
}
```
