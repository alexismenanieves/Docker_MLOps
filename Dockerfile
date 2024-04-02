FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9696

CMD ["python","catgif.py"]
