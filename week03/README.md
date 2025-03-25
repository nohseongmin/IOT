# IOT week3 practice
+ I2C protocol 
  - Inter-Integrated Circuit
  - 단 이중통신 사용
  - SDA(data), SCL(clock) 각각 1개의 선만 있으면 통신가능
  - 하나의 master에 112개(2^7-15(예약))의 slave(센서) 가능
  - 풀업 저항 필요(신호선을 항상 high(1)로 유지하는 역할) = LOW를 제어 가능하기 때문
+ LCD ~ arduino connect ( LiquidCrystal_I2C )
+ combine with week1 practice

# LCD.C
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
