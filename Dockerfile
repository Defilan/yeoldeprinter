FROM python:bullseye

COPY . .

CMD [ "python3", "./main.py" ]