##echo 'This is a test' > init_new.sql
##echo ${FIRST_NAME} > init_new.sql

echo "CREATE USER '${PYTHONUSER}'@'localhost' IDENTIFIED BY '${PYTHONUSERPASSWORD}';" > init_new.sql

echo "CREATE DATABASE data;" >> init_new.sql

echo "GRANT ALL PRIVILEGES ON *.* TO '${PYTHONUSER}'@'localhost' WITH GRANT OPTION;" >> init_new.sql

echo "ALTER USER '${PYTHONUSER}'@'%' IDENTIFIED BY '${PYTHONUSERPASSWORD}';" >> init_new.sql

echo "GRANT ALL PRIVILEGES ON *.* TO '${PYTHONUSER}'@'%' WITH GRANT OPTION;" >> init_new.sql

## This is required when using Dockerfile
