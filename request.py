# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:47:20 2021

@author: mbeutel
"""

import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('MVI_1646_VIS_frame360.jpg','rb')})


print(resp.json())