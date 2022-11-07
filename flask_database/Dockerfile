FROM python:3
ADD app_simple.py /
ADD myapp.py /
ADD /app/*.* /app/
RUN pip install flask
RUN pip install flask_restful
EXPOSE 5000
##CMD [ "python", "./app_simple.py"]
CMD [ "python", "./myapp.py"]
