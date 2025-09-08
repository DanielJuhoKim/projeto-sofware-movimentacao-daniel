FROM python

COPY * /

ENTRYPOINT ["python", "-py", "/app.py"]