FROM python:3.9

# ENV PATH="$PATH:/home/app/.local/bin"

# Install system dependencies
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential libmariadb3

WORKDIR /app

# copy all files from current directory to containers app directory
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# path to executable
ENTRYPOINT [ "uwsgi" ]

CMD [ "--ini", "uwsgi.ini"]