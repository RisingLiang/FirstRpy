# encoding:utf-8
import urllib.request
import base64
import json
import os
import cv2
from tkinter import *
from tkinter import filedialog
selectFileName = ""
def run1():
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/New1_Orange"
    selectFileName = filedialog.askopenfilename(title='选择文件')  # 选择文件
    print(selectFileName)
    selectFileName = selectFileName[-5:]
    print(selectFileName)
    with open(selectFileName, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode('UTF8')
    img = cv2.imread(selectFileName)
    params = {"image": s}
    ls = params;

    params = json.dumps(params)


    params = params.encode('utf-8')
    access_token = '24.f9e7fc4cb96f0c3bcd0dd774e6f9102e.2592000.1624546669.282335-24233511'
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read().decode()
    if content:
        print(content)
#转回来然后遍历
    s = json.loads(content)
    for i in s["results"]:
        xmin=i["location"].get("left")
        xmax=i["location"].get("left")+i["location"].get("width")
        ymin=i["location"].get("top")
        ymax=i["location"].get("top")+i["location"].get("height")
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0,0,255), 1)
        cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (255,0,0), 1)
    cv2.imshow('src',img)
'''
easydl物体检测
'''
root= Tk()
root.title('橘子检测系统')
root.geometry('500x500') # 这里的乘号不是 * ，而是小写英文字母 x
btn1 = Button(root, text='选择检测图片', command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)



root.mainloop()
