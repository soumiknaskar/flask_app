FROM python:3.9-alpine

RUN mkdir -p home/app
WORKDIR home/app
RUN pip install flask
COPY . home/app

CMD ["python","home/app/main.py"]