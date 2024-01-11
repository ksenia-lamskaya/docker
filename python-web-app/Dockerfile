FROM python:3.10-slim 

RUN mkdir /usr/src/app
COPY ./my-app /usr/src/app
COPY ./requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URL=postgress://user:password@localhost:5432/DATABASE_URL

EXPOSE 5000

CMD [ "python", "app.py" ]