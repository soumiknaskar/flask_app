FROM python:3.9-alpine

RUN mkdir -p home/app
WORKDIR home/app

COPY . home/app

RUN pip3 install -r home/app/requirement.txt

CMD ["python","home/app/server.py"]