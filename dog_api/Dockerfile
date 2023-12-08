FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=9000" ]
