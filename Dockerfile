FROM python:3.6.4-slim-jessie

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY api.py api.py
ENTRYPOINT ["python3", "api.py"]