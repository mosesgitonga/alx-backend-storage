-- create table with enumeration

CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    COUNTRY ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
