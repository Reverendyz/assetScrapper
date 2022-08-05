FROM python:3.8

ADD main.py .

ADD objscrapper.py .

RUN python -m pip install --upgrade pip

RUN pip install requests beautifulsoup4

CMD ["python", "./main.py"]