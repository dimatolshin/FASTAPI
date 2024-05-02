FROM python:3.9

COPY . .

WORKDIR .

EXPOSE 8000

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
