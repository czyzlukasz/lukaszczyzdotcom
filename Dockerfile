FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /webapp
COPY landing_page ./landing_page
COPY logbook ./logbook
COPY lukaszczyzdotcom ./lukaszczyzdotcom
COPY scripts ./scripts
COPY requirements.txt .
COPY manage.py .
COPY gunicorn_config.py .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD "/webapp/scripts/start_server.sh"
