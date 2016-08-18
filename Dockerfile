FROM java:8
MAINTAINER Raul Speroni (raulsperoni@gmail.com)

RUN apt-get install -y \
      unzip \
    && apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

ADD http://nlp.stanford.edu/software/stanford-spanish-corenlp-2015-10-14-models.jar stanford-spanish.zip
ADD http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip ner.zip 
RUN mkdir stanford
RUN unzip stanford-spanish.zip -d stanford
RUN unzip ner.zip -d stanford
ENV STANFORD_NER_JAR stanford-ner-2015-04-20/stanford-ner.jar 
ENV STANFORD_NER_MODEL stanford-ner-2015-04-20/classifiers/english.all.3class.distsim.crf.ser.gz

WORKDIR /stanford

ADD run.py run.py

ENTRYPOINT ["python", "-u", "/stanford/run.py"]
EXPOSE 80
