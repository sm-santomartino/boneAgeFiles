import os
from PIL import Image
import requests
import time
import json
import xlwt
from xlwt import Workbook
import csv

file_dir = "boneAgeFiles/rsna_res1024"


headers = ['image_path','age_female','age_male', 'img_path','inference_time']

wb = Workbook()
sheet1 = wb.add_sheet('Sheet1')
sheet1.write(0, 0, headers[0])
sheet1.write(0, 1, headers[1])
sheet1.write(0, 2, headers[2])
sheet1.write(0, 3, headers[3])
sheet1.write(0, 4, headers[4])

url = "https://www.16bit.ai/predict-url"

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

#edit for correct transformation
all_files = getListOfFiles(file_dir)

count = 0
for file in all_files:
    try:
        count += 1
        split = file.split('/')
        #image_path = 'https://raw.githubusercontent.com/smsantom/boneAgeFiles/master/' + split[1] + '/' + split[2] + '/' + split[3] + '/' + split[4]
        image_path = 'https://raw.githubusercontent.com/smsantom/boneAgeFiles/master/' + split[1] + '/' + split[2] 
        payload={'url': image_path}
        files=[]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
        json_resp = json.loads(response.text)
        age_female = json_resp['age_female']
        age_male = json_resp['age_male']
        img_path = json_resp['img_path']
        inference_time = json_resp['inference_time']
        print(image_path)
        #write to excel
        sheet1.write(count, 0, image_path)
        sheet1.write(count, 1, age_female)
        sheet1.write(count, 2, age_male)
        sheet1.write(count, 3, img_path)
        sheet1.write(count, 4, inference_time)

        #edit for correct transformation
        wb.save('RSNAPrediction_res1024.xls')
        time.sleep(10)
        
##        if(count == 10):
##            wb.save('test.xls')
##            exit(0)
        
    except:
        print('error: ' + file)
        
#edit for correct transformation
wb.save('RSNAPrediction_res1024.xls')


