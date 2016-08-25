#!/usr/bin/env python
# -*- coding: utf-8 -*-

from standford_server import *
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
