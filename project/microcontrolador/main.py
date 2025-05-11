import network
import time
from machine import Pin
import dht
import ujson
import urequests

WIFI_SSID = 'Wokwi-GUEST'
WIFI_PASSWORD = ''
API_URL = "http://localhost:8000/api/sensor-data/" 

sensor = dht.DHT22(Pin(15))

def connect_wifi():
    print("Conectando ao WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    
    if not sta_if.isconnected():
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)
    print(" Conectado!")
    print("IP:", sta_if.ifconfig()[0])

def read_sensor():
    try:
        sensor.measure()
        return {
            "temperature": sensor.temperature(),
            "humidity": sensor.humidity()
        }
    except Exception as e:
        print("\nErro ao ler sensor:", str(e))
        return None

def send_data(data):
    try:
        headers = {"Content-Type": "application/json"}
        print("Enviando para API...")
        print("A...")
        response = urequests.post(API_URL, data=ujson.dumps(data), headers=headers)
        print(response)
        if response.status_code == 200:
            print("Dados enviados com sucesso!")
        else:
            print(f"Erro na API (Status {response.status_code}): {response.text}")
        
        response.close()
        return True
    except OSError as e:
        print("\nErro de conexão:", str(e))
        if isinstance(e, OSError) and e.args[0] == -2:  
            print("Verifique o endereço da API:", API_URL)
        return False
    except Exception as e:
        print("\nErro inesperado:", str(e))
        return False

connect_wifi()

last_data = None

while True:
    if not network.WLAN(network.STA_IF).isconnected():
        print("WiFi desconectado. Reconectando...")
        connect_wifi()
    
    sensor_data = read_sensor()
    
    if sensor_data:
        print(f"Temperatura: {sensor_data['temperature']}°C, Umidade: {sensor_data['humidity']}%")
        
        if ujson.dumps(sensor_data) != last_data:
            if not send_data(sensor_data):
                print("Falha ao enviar dados. Tentando novamente...")
                time.sleep(2)
                if not send_data(sensor_data):  
                    print("Falha persistente. Verifique conexão e API.")
            else:
                last_data = ujson.dumps(sensor_data)
        else:
            print("Dados inalterados. Não enviando.")
    
    time.sleep(5) 