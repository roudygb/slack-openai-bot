FROM python:3.12

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 3000

CMD ["python", "bot.py"]

