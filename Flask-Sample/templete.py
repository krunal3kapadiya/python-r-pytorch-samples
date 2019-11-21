#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:58:10 2019

@author: krunal3kapadiya
PYLINT SCORE: 10/10
"""
from flask import Flask, render_template
from flask_dropzone import Dropzone

APP = Flask(__name__)
DROPZONE = Dropzone(APP)

@APP.route("/")
def index():
    '''
    running index.html file.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    APP.run(port=9000, debug=True)
