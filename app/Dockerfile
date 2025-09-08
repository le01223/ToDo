FROM python:3.12.3

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /app

COPY todo_result/todo_list.csv todo_result/todo_list.csv

COPY main.py main.py

ENTRYPOINT ["python", "main.py"]
