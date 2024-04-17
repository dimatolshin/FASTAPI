FROM python

COPY . .

WORKDIR .

EXPOSE 8000

RUN pip install -r requirements.txt  && python3 ./SQLAlchemi/database.py

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
