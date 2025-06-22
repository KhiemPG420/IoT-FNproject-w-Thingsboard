import paho.mqtt.client as mqtt
import time
import json
import random

# ---------- CẤU HÌNH ----------
THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "CK2vEutjSDuz0arKxkhI"  
PORT = 1883
GAS_THRESHOLD = 300  # ppm (ngưỡng cảnh báo)

# ---------- HÀM XỬ LÝ ----------
def on_connect(client, userdata, flags, rc):
    print("✅ Đã kết nối ThingsBoard (RC=" + str(rc) + ")")

# ---------- MQTT CLIENT ----------
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect

client.connect(THINGSBOARD_HOST, PORT, 60)
client.loop_start()

try:
    while True:
        gas_ppm = random.randint(150, 500)  # ppm
        gas_alert = gas_ppm > GAS_THRESHOLD

        data = {
            "gas_ppm": gas_ppm,
            "gas_alert": gas_alert
        }

        print("📡 Gửi:", data)
        client.publish("v1/devices/me/telemetry", json.dumps(data), qos=1)
        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 Dừng mô phỏng.")
    client.loop_stop()
    client.disconnect()
