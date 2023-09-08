FROM python:3.10

WORKDIR /app

ADD . /app
COPY python_run.sh /app
RUN pip install -r requirement.txt
ENV FLASK_APP=main.py
RUN chmod +x /app/python_run.sh
ENTRYPOINT ["/bin/sh", "python_run.sh"]
