# Stanford NER Docker
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

## Usage
```python
import ner
tagger = ner.SocketNER(host=localhost,port=9191)
        entities = []
        for t in texts:
            sentence_entities = tagger.get_entities(t)
            entities.append(sentence_entities)
        return entities
```
