# Spanish Stanford NER Docker
Dockerfile with [Stanford Named Entity Recognizer](https://github.com/stanfordnlp/CoreNLP/tree/master/doc/ner).

## Base Docker Image
* [java](https://registry.hub.docker.com/_/java/)

## Installation

1. Install [Docker](https://docs.docker.com/installation/).

2. Build an image from Dockerfile:

```bash
git clone
docker-compose up
```

## Usage as a simple Server
When running as a simple server, both NER and POS Stanford servers will be started and will listen for querys.
Note you need to change docker-compose.yml to run stanford_server.py directly. In this mode models should be inside "stanford" folder and proper enviroment variables should be set in docker-compose.yml file.

Here is an invocation example:
```python
import ner
class Stanford():
    """
    Clase que se conecta al servidor NER Stanford y devuelve el texto anotado.
    """

    def __init__(self, ner_host='localhost', ner_port=9191, ner_output_format='inlineXML',pos_port=9190):
        if ner_output_format not in ('slashTags', 'xml', 'inlineXML'):
            raise ValueError('Formato de salida %s invalido.' % ner_output_format)
        self.ner_tagger = ner.SocketNER(host=ner_host,port=ner_port)
        self.pos_tagger = ner.SocketNER(host=ner_host,port=pos_port)
        
    def tag(self,text):
        """
        Retorna texto anotado
        """
        return self.ner_tagger.tag_text(text)
    
    def pos(self,text):
        """
        Retorna texto anotado
        """
        return self.pos_tagger.tag_text(text)
```
## Usage through a Restful API
By default docker will start a Restful API wich you can use to start and stop both NER and POS servers. This API also allows you to train new Stanford models transfering training data from a client. You can print each operation results using:
```python
print response.content
```
### Transfer .tsv file
```python
import requests
url = 'http://172.17.0.2:5000/ner/train'
files = {'file': open('prueba_train.tsv')}
response = requests.post(url, files=files)
```
### Train new model
```python
import requests
url = 'http://172.17.0.2:5000/ner/train'
response = requests.get(url)
```
### List available models
```python
import requests
url = 'http://172.17.0.2:5000/ner/models'
response = requests.get(url)
```
### Start NER server
```python
import requests
url = 'http://172.17.0.2:5000/ner/start'
response = requests.get(url)
```
### Stop NER server
```python
import requests
url = 'http://172.17.0.2:5000/ner/stop'
response = requests.get(url)
```
### Check NER server status
```python
import requests
url = 'http://172.17.0.2:5000/ner/status'
response = requests.get(url)
```
### Start POS server
```python
import requests
url = 'http://172.17.0.2:5000/pos/start'
response = requests.get(url)
```
### Stop POS server
```python
import requests
url = 'http://172.17.0.2:5000/pos/stop'
response = requests.get(url)
```
### Check POS server status
```python
import requests
url = 'http://172.17.0.2:5000/pos/status'
response = requests.get(url)
```
