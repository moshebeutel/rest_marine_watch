# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:47:20 2021

@author: mbeutel
"""

from flask import json
import requests
import cv2 as cv
def draw_bounding_box(img, obj):
    
    print(obj['category'], obj['x'], obj['y'], obj['h'], obj['w'])

    img_h, img_w, _ = img.shape


    half_bb_h = int( (float(img_h) * float(obj['h']))/ 2.0)
    half_bb_w = int( (float(img_w) * float(obj['w'])) / 2.0)

    bb_x = int(float(img_w) * float(obj['x']))
    bb_y = int(float(img_h) * float(obj['y']))

    cv.rectangle(img,(bb_x - half_bb_w, bb_y- half_bb_h) ,(bb_x+  half_bb_w, bb_y+ half_bb_h),(0,255,0),3)

    
    return img    
    
    
 
def draw_objects_bounding_boxes(filename, obj_list, bb_filename):
    if len(obj_list) > 0:
        img = cv.imread(filename)
        for obj in obj_list:
            img = draw_bounding_box(img, obj)
        cv.imwrite(bb_filename, img)
    else:
        print(f'No Objects detected in {filename}')

filename = 'MVI_1646_VIS_frame360.jpg'

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open(filename,'rb')})

json_response = resp.json()

print('respose:', json_response)

assert 'objects' in json_response.keys()

obj_list = json_response['objects']

bb_filename = 'bboxes.jpg'

draw_objects_bounding_boxes(filename, obj_list, bb_filename)

