FROM python:3.11.3
WORKDIR /usr/local/app
RUN apt-get update && apt-get install -y groff-base
ADD Pipfile /usr/local/app
RUN pip install pipenv==2023.5.19 && pipenv install --skip-lock -d
ENTRYPOINT ["pipenv", "run"]
