import time
import socketio
from utils import humidity, temperature
import os

sensor_id = os.environ.get('SENSOR', 'SENSOR ID')
host = os.environ.get('HOST', 'http://webapp:5000') # analysis node vm ip

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')


if __name__ == '__main__':
    while True:
        try:
            sio.connect(host, transports='websocket')
            break
        except socketio.exceptions.ConnectionError as e:
            print(f'Error connecting to server: {e}')
            time.sleep(5)

    while True:
        data = {
            'sensor_name': sensor_id,
            'temperature': temperature(),
            'humidity': humidity()
        }
        
        sio.emit('sensor_data', data)
        time.sleep(5)

    sio.wait()
