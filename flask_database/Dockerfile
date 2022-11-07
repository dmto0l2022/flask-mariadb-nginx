FROM python:3
ADD app_simple.py /
ADD myapp.py /
ADD /app/*.* /app/
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./myapp.py"]
