FROM python:3.11-buster

WORKDIR /var/www/server

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . ./

LABEL maintainer="Jakub Was"

EXPOSE 8000

CMD [ "gunicorn", "--bind", ":8000", "--workers", "3", "myproject.wsgi:application" ]
