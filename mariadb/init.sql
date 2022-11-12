CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonuser';

CREATE DATABASE dmtools;

CREATE DATABASE world;

GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'localhost' WITH GRANT OPTION;

##ALTER USER 'pythonuser'@'%' IDENTIFIED BY 'pythonuser';

##ALTER USER 'pythonuser'@'%' IDENTIFIED WITH mysql_native_password BY 'pythonuser';

##ALTER USER root@localhost IDENTIFIED BY PASSWORD '************';

##ALTER USER 'pythonuser'@'%' IDENTIFIED BY PASSWORD 'pythonuser';

create user pythonuser@'%' identified by 'pythonuser';

GRANT ALL PRIVILEGES ON *.* TO pythonuser@'%' WITH GRANT OPTION;

