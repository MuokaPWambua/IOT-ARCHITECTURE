import datetime

def save_sensor_data(connection,data):
    try:
        humidity = data['humidity']
        temperature = data['temperature']
        sensor_name = data['sensor_name']
        created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur = connection.cursor()
        cur.execute(f"INSERT INTO readings\
            (humidity, temperature, sensor_name, created_at)\
            VALUES {(humidity, temperature, sensor_name, created_at)}")
        connection.commit()
        cur.close()
    except Exception as e:
        print(str(e))