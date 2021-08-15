# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from flask import Flask, jsonify, request
import io
from PIL import Image
#import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    print("predict called")
    
    if request.method == 'POST':
        print("POST called")
        file = request.files['file']
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        print('image size', image.size)
    else:
        print('error')
    
    print('parsing annotations')
    obj_list = []
    with open('MVI_1646_VIS_frame360.txt', 'r') as f:
        for line in f: 
            fields =line.split()
            obj = {'category': fields[0], 'x': fields[1], 'y': fields[2], 'w': fields[3], 'h': fields[4]}
            obj_list.append(obj)
           
    
    return jsonify({'objects': obj_list})



