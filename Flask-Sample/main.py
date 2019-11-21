#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:51:47 2019

@author: krunal3kapadiya
PYLINT SCORE: 8.18
"""
import argparse
import re
import os
AP = argparse.ArgumentParser()
AP.add_argument("-i", "--command", required=True,
                help="Command wants to run API or execute WEBPAGE?")
ARGS = vars(AP.parse_args())
if(re.match(ARGS['command'], 'WEBPAGE')):
    os.system(str("python templete.py"))
elif(re.match(ARGS['command'], 'API')):
    os.system(str("python api.py"))
else:
    print("Please parse valid command either WEBPAGE or API")
