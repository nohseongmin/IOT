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
