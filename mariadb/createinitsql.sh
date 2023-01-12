##echo 'This is a test' > init_new.sql
##echo ${FIRST_NAME} > init_new.sql

echo "CREATE USER '${PYTHONUSER}'@'localhost' IDENTIFIED BY '${PYTHONUSERPASSWORD}';" > init.sql

echo "CREATE DATABASE data;" >> init.sql

echo "GRANT ALL PRIVILEGES ON *.* TO '${PYTHONUSER}'@'localhost' WITH GRANT OPTION;" >> init.sql

echo "ALTER USER '${PYTHONUSER}'@'%' IDENTIFIED BY '${PYTHONUSERPASSWORD}';" >> init.sql

echo "GRANT ALL PRIVILEGES ON *.* TO '${PYTHONUSER}'@'%' WITH GRANT OPTION;" >> init.sql

## This is required when using Dockerfile
