DROP DATABASE diagnospymes;
CREATE DATABASE diagnospymes;
GRANT ALL PRIVILEGES ON diagnospymes.* TO 'diagnospymes_user'@'localhost' IDENTIFIED BY 'password';
flush privileges;
