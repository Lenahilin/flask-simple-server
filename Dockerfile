FROM python:latest
COPY . /flaskapp
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt

EXPOSE 5000

CMD ["python", "/flaskapp/main.py"]