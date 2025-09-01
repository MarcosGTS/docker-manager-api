FROM python:3.12.5-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip  

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

EXPOSE 8000

RUN apt-get update && apt-get install -y netcat-traditional

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "api_root.asgi:application"]
