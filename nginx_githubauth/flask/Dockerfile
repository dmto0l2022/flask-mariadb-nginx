FROM python:3
ADD hello.py /
ADD app.py /
ADD .env /
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask_dance
RUN pip install python-dotenv

##EXPOSE 5000
CMD [ "python", "./hello.py"]
#CMD [ "python", "./app.py"]
