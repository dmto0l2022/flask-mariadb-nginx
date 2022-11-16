FROM python:3
ADD hello.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask_dance
RUN pip install dotenv

##EXPOSE 5000
#CMD [ "python", "./hello.py"]
CMD [ "python", "./app.py"]
