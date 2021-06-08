FROM python:3.8

ENV PORT 8080
ENV HOST 0.0.0.0

RUN apt update
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "cronrunner.py"]