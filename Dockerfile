FROM python

COPY . .

ENTRYPOINT ["python", "/app.py"]