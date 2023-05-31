-- Create the database
CREATE DATABASE IF NOT EXISTS analysis;

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

