FROM python:slim

ADD main.py /

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install -r requirements.txt


RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

COPY ./ ./

CMD ["python", "main.py"]