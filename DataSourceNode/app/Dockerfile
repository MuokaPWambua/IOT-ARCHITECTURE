FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install python-socketio requests websocket-client

EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD ["app.py"]