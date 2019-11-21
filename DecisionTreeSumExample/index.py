#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:27:50 2019

@author: krunal3kapadiya

Problem: Find profit for next data

"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  

input_df = pd.read_csv('decision_tree.csv')

X = input_df.iloc[:, 0:3].values
Y = input_df.iloc[:, 3].values

labelEncoder = LabelEncoder()
input_df = input_df.apply(labelEncoder.fit_transform)

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, Y)

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
# to convert dot to png
# dot -Tpng tre.dot -o tree_limited.png -Gdpi=600
y_pred = clf.predict([[0,1,0]])
