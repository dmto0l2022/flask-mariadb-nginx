##echo 'This is a test' > init_new.sql
##echo ${FIRST_NAME} > init_new.sql

echo "CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonuser';" > init_new.sql

echo "CREATE DATABASE data;" >> init_new.sql

echo "GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'localhost' WITH GRANT OPTION;" >> init_new.sql

echo "ALTER USER 'pythonuser'@'%' IDENTIFIED BY 'pythonuser';" >> init_new.sql

echo "GRANT ALL PRIVILEGES ON *.* TO 'pythonuser'@'%' WITH GRANT OPTION;" >> init_new.sql

## This is required when using Dockerfile
