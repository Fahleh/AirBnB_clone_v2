-- This script prepares a MySQL server.
-- Create project testing database with the name hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user named hbnb_test with all privileges on the db.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
