
FROM python:3.12-slim

WORKDIR /main_bot

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "bot.py"]
