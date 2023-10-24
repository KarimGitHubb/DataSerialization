#! /usr/bin/env python3
import os
import requests

path = "/data/feedback"
dic = {}
txtlist = os.listdir(path)
for file in txtlist:
    with open('/data/feedback/'+file, 'r') as txtfile:
        lines = txtfile.readlines()
        # get data individually
        dic['title'] = lines[0].strip()
        dic['name'] = lines[1].strip()
        dic['date'] = lines[2].strip()
        dic['feedback'] = lines[3].strip()
    response = requests.post("http://<corpweb-external-IP>/feedback/", data=dic)
   # with open(file, 'r') as f:
  #      for i in range(3):
 #           next(f)
#        feedback = ' '.join(line.rstrip() for line in f)


