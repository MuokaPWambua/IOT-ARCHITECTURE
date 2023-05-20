-- Create the database
CREATE DATABASE IF NOT EXISTS analysis;

GRANT ALL PRIVILEGES ON analysis.* TO 'app'@'%';

-- Switch to the database
USE analysis;

-- Create the table
CREATE TABLE IF NOT EXISTS readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    humidity FLOAT,
    temperature FLOAT,
    sensor_name VARCHAR(255),
    created_at TIMESTAMP
);

-- Insert initial data
INSERT INTO readings (humidity, temperature, sensor_name, created_at) VALUES
    (15, 5, 'Sensor 1', NOW()),
    (20, -5, 'Sensor 2', NOW()),
    (15, 10, 'Sensor 3', NOW());
