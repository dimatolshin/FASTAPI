FROM python

COPY /MainApi /project

WORKDIR /project

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
