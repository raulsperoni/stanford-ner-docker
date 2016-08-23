#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import socket
import subprocess


STANFORD_NER_PARSER = os.path.abspath(os.environ['STANFORD_NER_JAR'])
STANFORD_NER_MODEL = os.path.abspath(os.environ['STANFORD_NER_MODEL'])
STANFORD_NER_LIB = os.path.abspath(os.environ.get('STANFORD_NER_LIB') if os.environ.get('STANFORD_NER_LIB') else '')
STANFORD_POS_PARSER = os.path.abspath(os.environ['STANFORD_POS_JAR'])
STANFORD_POS_MODEL = os.path.abspath(os.environ['STANFORD_POS_MODEL'])
STANFORD_POS_LIB = os.path.abspath(os.environ.get('STANFORD_POS_LIB') if os.environ.get('STANFORD_POS_LIB') else '')
JAVA_MEM = '-Xmx200m'
STANFORD_NER_PORT = '9191'
STANFORD_POS_PORT = '9190'

def start_ner_server(parser=STANFORD_NER_PARSER, model=STANFORD_NER_MODEL,mem=JAVA_MEM,port=STANFORD_NER_PORT,lib=STANFORD_NER_LIB):
  if lib:
     parser = parser + ':' + lib
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

def start_pos_server(parser=STANFORD_POS_PARSER, model=STANFORD_POS_MODEL,mem=JAVA_MEM,port=STANFORD_POS_PORT,lib=STANFORD_POS_LIB):
  if lib:
     parser = parser + ':' + lib
  command = [
    'java',
    mem,
    '-cp',
    parser,
    'edu.stanford.nlp.tagger.maxent.MaxentTaggerServer',
    '-model',
    model,
    '-port',
    port

  ]
  print ' '.join(command)
  return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



"""
El código se ejecuta solo si el script es ejecutado como programa.
Si es importado se ignora.
"""
if __name__ == '__main__':
  print 'Iniciando Stanford NER server...'
  print 'Escuchando en ' +socket.gethostbyname(socket.gethostname())+':'+STANFORD_NER_PORT+' ...'
  process = start_ner_server()
  
  print 'Iniciando Stanford POS server...'
  print 'Escuchando en ' +socket.gethostbyname(socket.gethostname())+':'+STANFORD_POS_PORT+' ...'
  process_pos = start_pos_server()

  try:
  	while True:
            out = process.stderr.readline()
            if out and out != "":
            	print out
            out = process.stdout.readline()
            if out and out != "":
                print out
            out = process_pos.stderr.readline()
            if out and out != "":
                print out
            out = process_pos.stdout.readline()
            if out and out != "":
                print out

  except KeyboardInterrupt:
    print 'Deteniendo NER server..'
    process.kill()
    print 'Deteniendo POS server..'
    process_pos.kill()

