CREATE DATABASE IF NOT EXISTS microbits;

USE microbits;

GRANT ALL PRIVILEGES
	ON microbits.*
    TO 'user'@'%'
;

SET GLOBAL local_infile = 1;

DROP TABLE sensors;
CREATE TABLE sensors
(
	sensor_id CHAR,
    temp int,
    light int,
    currentTime VARCHAR(10)
);

LOAD DATA LOCAL INFILE 'data.txt'
INTO TABLE sensors COLUMNS TERMINATED BY '\t'
IGNORE 1 LINES;