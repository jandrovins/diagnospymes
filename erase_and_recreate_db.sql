DROP DATABASE diagnospymes;
CREATE DATABASE diagnospymes CHARACTER SET utf8;
GRANT ALL PRIVILEGES ON diagnospymes.* TO 'diagnospymes_user'@'localhost' IDENTIFIED BY 'password';
flush privileges;
