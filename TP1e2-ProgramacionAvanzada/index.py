# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:13:48 2023

@author: pedro
"""
from flask import Flask, render_template, request

app=Flask(__name__)     
@app.route('/')
def principal():
    return render_template('index.html')

    
if __name__=="__main__":
    app.run(debug=False)
