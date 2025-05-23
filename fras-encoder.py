import cv2
import os
import face_recognition
import pickle

#import student images
folderPath = 'FRAS_Image'
pathList = os.listdir(folderPath)
#print(pathList)
imgList = []
studentIDs = []


for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) # read the image and append it to imgList
    format_studentIDs = os.path.splitext(path)[0].split('_')[0]
    studentIDs.append(format_studentIDs)# extracts the student ID only
    #print(path)
    #print(os.path.splitext(path)[0])

print(imgList) # should be able to see different arrays
print(len(imgList)) # should  be able to see 18, which are the number of images in the FRAS-Image Folder

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]
print("Encoding Complete")
file = open("FinalEncodedFile.p",'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("File Saved")

