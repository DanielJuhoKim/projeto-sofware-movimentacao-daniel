FROM python

COPY . .

run ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python", "/app.py"]