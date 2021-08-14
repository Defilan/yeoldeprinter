FROM arm64v8/python:3

COPY . .

CMD [ "python3", "./main.py" ]