#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import socket
import subprocess


STANFORD_PARSER = os.path.abspath(os.environ['STANFORD_NER_JAR'])
STANFORD_MODEL = os.path.abspath(os.environ['STANFORD_NER_MODEL'])
JAVA_MEM = '-Xmx200m'
STANFORD_PORT = '9191'

def start_ner_server(parser=STANFORD_PARSER, model=STANFORD_MODEL,mem=JAVA_MEM,port=STANFORD_PORT):
  command = [
    'java',
    mem,
    '-cp',
    parser,
    'edu.stanford.nlp.ie.NERServer',
    '-port',
    port,
    '-loadClassifier',
    model,
    '-outputFormat',
    'inlineXML'
  ]
  print ' '.join(command)
  return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



"""
El código se ejecuta solo si el script es ejecutado como programa.
Si es importado se ignora.
"""
if __name__ == '__main__':
  print 'Iniciando Stanford NER server...'
  print 'Escuchando en ' +socket.gethostbyname(socket.gethostname())+':'+STANFORD_PORT+' ...'
  process = start_ner_server()
  try:
  	while True:
            out = process.stderr.readline()
            if out and out != "":
                print out
            out = process.stdout.readline()
            if out and out != "":
               print out
  except KeyboardInterrupt:
    print 'Deteniendo NER server..'
    process.kill()
