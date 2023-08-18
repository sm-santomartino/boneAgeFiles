import os
from PIL import Image, ImageEnhance, ImageOps

#file_dir = "DigitalHandAtlas/JPEGimages/"
file_dir = "boneAgeFiles/RSNA_validation2/"


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

all_files = getListOfFiles(file_dir)

for file in all_files:
    try:
        im = Image.open(file)
        im = ImageOps.invert(im)

        split = file.split('/')

        #new_path = 'DHA_invert/'+split[2]+'/'+split[3]+'/'
        new_path = 'rsna_invert/'

        isExist = os.path.exists(new_path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(new_path)
            #print("The new directory is created!")

        #im.save(new_path+split[4])
        im.save(new_path+split[2])
    except:
        print('error: ' + file)

