-- A script that prepares a MySQL server.
-- Create a project developement database with the name hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user named : hbnb_dev with all privileges.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
