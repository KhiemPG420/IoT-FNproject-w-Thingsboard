import paho.mqtt.client as mqtt
import time
import json
import random

# Thông tin kết nối
THINGSBOARD_HOST = 'localhost' 
ACCESS_TOKEN = 'MixmYF6lliUkGi1mqPMa'  # <-- Dán Access Token từ ThingsBoard

# Hàm khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Tạo client MQTT
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect

# Kết nối tới ThingsBoard Cloud qua MQTT (port 1883)
client.connect(THINGSBOARD_HOST, 1883, 60)

# Bắt đầu vòng lặp
client.loop_start()
status_data = [
    {"status": "Nothing", "color": "green"},
    {"status": "Mother", "color": "red"},
    {"status": "Tranger", "color": "yellow"}
]

try:
    while True:
        # Tạo dữ liệu ngẫu nhiên
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        motion = random.choice([True, False])
        tranger = random.choice(["My son", "Nothing", "Tranger", "My mom"])
        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "motion": motion,
            "lam": tranger
        }

        # In và gửi dữ liệu
        print("Gửi:", payload)
        client.publish("v1/devices/me/telemetry", json.dumps(payload), 1)

        time.sleep(5)  # gửi mỗi 5 giây

except KeyboardInterrupt:
    print("Stopped by user")
    client.loop_stop()
    client.disconnect()
# --------- HÀM XỬ LÝ KẾT NỐI ---------
def on_connect(client, userdata, flags, rc):
    print("✅ Kết nối thành công với ThingsBoard (RC=" + str(rc) + ")")


#----------------------------------GIẢ LÂP CẢM BIEN CHUYEN DỘNG------------------------------


