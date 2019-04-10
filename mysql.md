*Using the terminal* 

sudo /usr/bin/mysql -u root -p 

mysql> CREATE DATABASE bachapp; 

mysql> USE bachapp; 

mysql> CREATE TABLE users(uid INT(11) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(50),
email, VARCHAR(50), settings VARCHAR(30000), tracking VARCHAR(30000), rank INT (3));

*To view the table* 
mysql> SHOW TABLES;

*To view the description of each role on the table* 
mysql> DESCRIBE users; 

mysql> QUIT 
Bye 

*To start the merge with python code* 
sudo apt-get install python-mysqldb

*WORK IN PROGRRESS*
