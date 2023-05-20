FROM mysql:8.0

# Set the environment variables for the MySQL server
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=analysis
ENV MYSQL_USER=app
ENV MYSQL_PASSWORD=userpassword

# custom configeration file
# COPY my.cnf /etc/mysql/my.cnf

# Copy the SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

# Start the MySQL server
CMD ["mysqld"]

