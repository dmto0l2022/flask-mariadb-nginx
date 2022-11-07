FROM python:3
ADD myapp.py /
ADD /app/*.* /app/
RUN pip install flask
RUN pip install flask_restful
EXPOSE 5000
CMD [ "python", "./myapp.py"]
