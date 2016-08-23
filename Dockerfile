FROM java:8
MAINTAINER Raul Speroni (raulsperoni@gmail.com)

RUN mkdir stanford

ADD run.py run.py

WORKDIR /stanford


ENTRYPOINT ["python", "-u", "/run.py"]
EXPOSE 9191
