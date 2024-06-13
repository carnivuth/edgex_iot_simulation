FROM python:3.11
WORKDIR /usr/local/monitor
ADD monitor.py .
ADD settings.py .
RUN pip install requests python-telegram-bot
CMD ["python", "./monitor.py"] 
