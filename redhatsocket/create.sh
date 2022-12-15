docker build -t my-apache2 .
docker run -dit --name my-running-app -p  0.0.0.0:8000:8000 my-apache2
