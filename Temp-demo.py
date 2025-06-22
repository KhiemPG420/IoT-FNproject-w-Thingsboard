import paho.mqtt.client as mqtt
import random
import time
import json

# Configuration
THINGSBOARD_HOST = "localhost"
ACCESS_TOKEN = "lhn3p1vmb7pd4an4zhty"
PORT = 1883  # Default MQTT port for ThingsBoard CE
TOPIC = "v1/devices/me/telemetry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to ThingsBoard MQTT broker")
    else:
        print(f"❌ Connection failed with code {rc}")

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.on_connect = on_connect

try:
    client.connect(THINGSBOARD_HOST, PORT, 60)
    client.loop_start()
    print(f"Starting to send telemetry data to ThingsBoard MQTT at {THINGSBOARD_HOST}:{PORT}")
    print("Press Ctrl+C to stop...")

    while True:
        telemetry = {
            "temperature": round(random.uniform(25.0, 38.0), 2),
            "humidity": round(random.uniform(30.0, 70.0), 2)
        }
        payload = json.dumps(telemetry)
        result = client.publish(TOPIC, payload)
        status = result[0]
        if status == 0:
            print(f"✅ Data sent successfully: {telemetry}")
        else:
            print(f"❌ Failed to send message: {telemetry}")
        time.sleep(5)

except KeyboardInterrupt:
    print("\nStopped by user")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
finally:
    client.loop_stop()
    client.disconnect()
    print("Telemetry sender stopped")
