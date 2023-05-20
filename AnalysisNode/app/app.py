from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pymysql
from utils import *
from flask_cors import CORS
import eventlet
from eventlet import wsgi

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your-secret-key'

application = app

socketio = SocketIO(
    app, 
    cors_allowed_origins='*',
    logger=True,
    engineio_logger=True,
    async_mode='eventlet'
)

connection = pymysql.connect(
    host='mysql',
    user='app',
    password='userpassword',
    db='analysis',
)

# Route for the main page
@app.route('/')
def index():

    try:
        
        with connection.cursor() as cursor:
            # Execute the SQL query to fetch data
            sql = "SELECT * FROM readings"
            cursor.execute(sql)
            result = cursor.fetchall()    
            temp = [x[2] for x in result] 
            humid = [x[1] for x in result]
            avg_humid = sum(humid)/len(humid)
            avg_temp = sum(temp)/len(temp) 
            return render_template(
                'index.html', 
                data=result,
                humidity_average=avg_humid,
                temperature_average=avg_temp)
    except Exception as e: 
        return render_template('index.html', data=[], humidity_average=25, temperature_average=15)

@socketio.on('connect')
def handle_connect():
    emit('sensor connected')

@socketio.on('disconnect')
def handle_disconnect():
    emit('sensor disconnected')

@socketio.on('sensor_data')
def handle_sensor_data(data):
    try:
        save_sensor_data(connection, data)
        emit('data_saved', {'message': 'Sensor data saved successfully'})
    except Exception as e:
        print(str(e))
        
        
if __name__ == '__main__':
    wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)
