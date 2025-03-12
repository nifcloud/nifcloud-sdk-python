FROM python:3.13.2
WORKDIR /usr/local/app
RUN apt-get update && apt-get install -y groff-base
ADD Pipfile /usr/local/app
RUN pip install pipenv==2024.4.1 && pipenv install --skip-lock -d
ENTRYPOINT ["pipenv", "run"]
