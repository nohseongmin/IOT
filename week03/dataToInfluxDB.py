import serial
#influxDB 사용해 데이터를 저장할 것이므로 import
from influxdb_client import InfluxDBClient
#time.sleep 사용을 위한 time
import time

serial_port = 'COM15'
baud_rate = 9600
timeout = 2

#influxDB v2 설정
influxdb_url = "http://localhost:8086"
influxdb_token = "yourToken" #토큰은 항상 숨길것
influxdb_org = "test" 
influxdb_bucket = "dust" #데이터 저장할 bucket 이름(influxDB에 저장될 이름)

#influxDB 클라이언트 초기화
client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = client.write_api()

#시리얼포트 오픈
try:
    ser = serial.Serial(serial_port, baud_rate, timeout = timeout)
    print(f"Connect to {serial_port} at {baud_rate} baud")
#예외처리시 예외 이름을 출력하게 함으로서 예외를 정확히 파악
#except: ~ 로 하게 되면 이유를 알 수 없음
except Exception as e:
    print(f"{e}")
    exit()

try:
    while True:
        if ser.in_waiting > 0:
            #아두이노로부터 시리얼 데이터 읽음
            line = ser.readline().decode('utf-8').strip()
            #데이터가 유효한 경우 influxDB에 기록 (arduino.c에서 보면 알겠지만 =값을 기준으로 나누기때문에 공백에 주의)
            if "=" in line:
                key, value = line.split("=")
                try:
                    value = float(value)
                    data = f"sensor_data,device=arduino {key}={value}"
                    write_api.write(bucket=influxdb_bucket, record=data)
                    print(f"Data written to influxDB: {key}={value}")
                except ValueError:
                    print("Invalid data format")

        time.sleep(1)

#무한루프에 빠질 수 있으므로 KeyboardInterrupt 오류를 이용해 탈출가능하게 구성
except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    ser.close()
