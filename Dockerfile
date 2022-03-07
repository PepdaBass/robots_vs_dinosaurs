FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /usr/app

COPY requirements.txt/ ./
RUN pip3 install pipenv

COPY ./ ./

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
RUN pipenv shell

CMD ["python", "manage.py", "runserver"]