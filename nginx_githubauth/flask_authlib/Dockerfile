FROM python:3
ADD hello.py /
ADD app.py /
ADD .env /
RUN pip install python-dotenv
RUN pip install flask
RUN pip install Authlib
RUN pip install requests

##EXPOSE 5000
#CMD [ "python", "./hello.py"]
CMD [ "python", "./app.py"]
