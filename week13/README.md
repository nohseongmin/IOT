## 13주차 수업내용
1. cygwin 개요
2. TinyOS 기반 NesC 프로그래밍

## cygwin 개요
1. 윈도우 환경 안에서 Linux 실습가능
2. 윈도우와 리눅스간 파일 이동 자유로움

## TinyOS 기반 NesC 프로그래밍
1. TestC.nc
```C
module TestC
{
    uses {
        interface Boot;
        interface Leds;
        interface Timer<TMilli> as MilliTimer;

        interface SplitControl as RadioControl;
        interface AMSend as RadioSend;

        interface Read<uint16_t> as Temp;
        interface Read<uint16_t> as Humi;
        interface Read<uint16_t> as Illu;

        interface Battery;
    }
}

implementation
{
    message_t testMsgBffr;
    test_data_msg_t *testMsg;

    uint32_t seqNo;
    uint8_t step;

    
    task void startTimer();
    event void Boot.booted() { //부팅시 작동
        testMsg = (test_data_msg_t *)call RadioSend.getPayload(
            &testMsgBffr, sizeof(test_data_msg_t));
        testMsg->srcID = TOS_NODE_ID; // 포인터 역할

        seqNo = 0;

        post startTimer();
     }
    
    task void startTimer() {
        call MilliTimer.startPeriodic(TEST_PERIOD);
    }

    task void radioOn();
    event void MilliTimer.fired() {
        post radioOn();
    }

    void startDone();
    task void radioOn() {
        if (call RadioControl.start() != SUCCESS) startDone();
    } //RadioControl.start() 는 내장함수

    event void RadioControl.startDone(error_t error) {
        startDone();
    }
    
    task void readTask();
    void startDone() {
        step = 0;
        post readTask();
        call Leds.led0Toggle();
    }

    void sendDone();
    task void sendTask() {
        testMsg->seqNo = seqNo++;
        testMsg->type = 2;

        if (call RadioSend.send(AM_BROADCAST_ADDR, &testMsgBffr,
            sizeof(test_data_msg_t)) != SUCCESS) sendDone();
        call Leds.led2Toggle();
    }

    event void RadioSend.sendDone(message_t* msg, error_t error) {
        sendDone();
    }

    task void radioOff();
    void sendDone() {
        call Leds.led0Off();
        call Leds.led1Off();
        call Leds.led2Off();
        post radioOff();
    }

    void stopDone();
    task void radioOff() {
        if (call RadioControl.stop() != SUCCESS) stopDone();
    }

    event void RadioControl.stopDone(error_t error) {
        stopDone();
    }

    void stopDone() {
    }
    task void readTask() {
        switch(step) {
            case 0:
                call Temp.read(); break;
            case 1:
                call Humi.read(); break;
            case 2:
                call Illu.read(); break;
            default:
                testMsg->battery = call Battery.getVoltage();
                post sendTask();
                break;
        }
        step += 1; //event가 아니었다면 도달할 수 없었겠지만 비동기식 통신을 사용하므로 프로그램 완료를 기다리지 않음 -> 도달가능
    } 

    event void Temp.readDone(error_t error, uint16_t val) {
        //if ~
        testMsg->Temp = error == SUCCESS ? val : 0xFFFA;
        post readTask();
    }
    event void Humi.readDone(error_t error, uint16_t val) {
        //if ~
        testMsg->Humi = error == SUCCESS ? val : 0xFFFB;
        post readTask();
    }

    event void Illu.readDone(error_t error, uint16_t val) {
        //if ~
        testMsg->Illu = error == SUCCESS ? val : 0xFFFC;
        post readTask();
    }
}
```
2. TestAppC.nc
```C
includes Test;
configuration TestAppC
{
}
implementation
{
    components TestC, MainC;
    components LedsC, new TimerMilliC();

    components ActiveMessageC as AMC;
    components new AMSenderC(AM_TEST_DATA_MSG) as AMSC;

    TestC.Boot -> MainC;
    TestC.Leds -> LedsC;
    TestC.MilliTimer -> TimerMilliC;

    TestC.RadioControl -> AMC;
    TestC.RadioSend -> AMSC;

    components new SensirionSht11C() as Sht11ChOC;
    TestC.Temp -> Sht11ChOC.Temperature;
    TestC.Humi -> Sht11ChOC.Humidity;

    components new IlluAdcC() as Illu;
    TestC.Illu -> Illu;

    components BatteryC;
    TestC.Battery -> BatteryC;
}

```
3. Test.h
```C
#ifndef TEST_H
#define TEST_H
#include "message.h"
enum {
    TEST_PERIOD = 10240LU, //10초(long unsigned)
};
enum { //enum은 const와 비슷함. 기호상수 0x11
    DFLT_VAL = 0x11,
};
enum {
    TEST_DATA_LENGTH = TOSH_DATA_LENGTH - 6, // 6바이트는 헤더같이 전송에 필요한 부분
};
enum {
    AM_TEST_DATA_MSG = 0xA4,
};

typedef nx_struct test_data_msg { //struct와 비슷
    nx_am_addr_t srcID;
    nx_uint32_t seqNo;
    nx_uint16_t type;
    nx_uint16_t Temp;
    nx_uint16_t Humi;
    nx_uint16_t Illu;
    nx_uint16_t battery;
} test_data_msg_t;

#endif //두번 선언 방지 디테일
```

4. 이후 컴파일
```
make telosb
```
![image](https://github.com/user-attachments/assets/14f5998a-3b6a-4c60-be75-33e9f7ba36f0)

5. 모듈 설치
```
make telosb.(nodenum)
```
![image](https://github.com/user-attachments/assets/927dbbc3-f765-40c4-9e04-f89f966632df)

6. 원리
   - USB에 연결된 모듈에 프로그램 설치
   - 모듈을 센서에 부착
   - 센서로부터 무선통신(AM)으로 데이터를 전송받음
