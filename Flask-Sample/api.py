#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:58:10 2019

@author: krunal3kapadiya
PYLINT SCORE: 8.57
"""
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def run_api():
    '''
    running API
    '''
    requested_json = request.get_json()
    return 'API Successfully called your response is {}'.format(requested_json)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
