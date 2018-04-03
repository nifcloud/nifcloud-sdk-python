FROM python:3.6.3
WORKDIR /usr/local/app
RUN apt-get update && apt-get install -y groff-base
ADD Pipfile.lock /usr/local/app
RUN pip install pipenv==11.8.0 && pipenv install --ignore-pipfile -d
ENTRYPOINT ["pipenv", "run"]
