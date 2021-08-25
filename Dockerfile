FROM python:bullseye

RUN adduser --system --group --no-create-home printy

COPY . .

USER printy
CMD [ "python3", "./main.py" ]