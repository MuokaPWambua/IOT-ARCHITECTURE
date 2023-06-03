![Alt Text](IOT.png)
# How To:
You will first need to build each image and create a network to connect each image

### Generate self signed certificate
this command will generate a self signed certificate inside the `AnalysisNode/app` directory the `key.pem` and `cert.pem`

- `openssl req -newkey rsa:2048 -nodes -keyout ./AnalysisNode/app/key.pem -x509 -days 365 -out ./AnalysisNode/app/cert.pem`

### Build Image

- mysql database `docker build -t mysql AnalysisNode/mysql`

- webapp `docker build -t webapp AnalysisNode/app`

- sensor `docker build -t sensor DataSourceNode/app`

### Create Network
- `docker network create analysis_net`

### Run and Connect Network

- mysql image: 
    `docker run -dp 3306:3306 --network analysis_net --network-alias mysql -v mysql-data:/var/lib/mysqld mysql`
- webapp image:
    `docker run -itp 5000:5000 --network analysis_net --network-alias webapp webapp`
- sensor:
    `docker run -itp 5001:5001 --network analysis_net -e SENSOR='Sensor Name' sensor`


*Note:
    to achieve this architecture you will need to duplicate the DataSourceNode sensor image on a different vm and give its own environment name which the app will use as the name of the sensor. ie `docker run -dp 5002:5001 -e SENSOR='Sensor Name' sensor2`

![Alt Text](iot.png)

