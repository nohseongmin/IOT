import serial
from influxdb_client import InfluxDBClient
import time

serial_port = 'COM15'
baud_rate = 9600
timeout = 2

#influxDB v2 설정
influxdb_url = "http://localhost:8086"
influxdb_token = "yourToken" #input yourToken here.
influxdb_org = "test"
influxdb_bucket = "dust"

#influxDB 클라이언트 초기화
client = InfluxDBClient(url=influxdb_url, token=influxdb_token, org=influxdb_org)
write_api = client.write_api()

#시리얼포트 오픈
try:
    ser = serial.Serial(serial_port, baud_rate, timeout = timeout)
    print(f"Connect to {serial_port} at {baud_rate} baud")
except Exception as e:
    print(f"{e}")
    exit()

try:
    while True:
        if ser.in_waiting > 0:
            #아두이노로부터 시리얼 데이터 읽음
            line = ser.readline().decode('utf-8').strip()
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

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    ser.close()
