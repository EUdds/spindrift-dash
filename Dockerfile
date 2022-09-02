FROM python:3.8-slim-buster

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY data.db data.db
COPY spindrift_dash .

CMD ["uvicorn", "spindrift_dash.main:app", "--host", "0.0.0.0", "--port", "8124", "&"]
CMD ["python3", "spindrift_dash/src/main.py", "&"]
