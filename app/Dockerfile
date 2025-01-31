FROM python:3.10-slim

WORKDIR /usr/src/app
COPY APIRest ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
