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

## 이론
