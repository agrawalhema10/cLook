import cv2
import os
import numpy as np
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade=cv2.CascadeClassifier("C:\\Users\\Hp\\PycharmProjects\\cLook\\cLook\\haarcascade_frontalface_default.xml")
    faces= face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)
    return faces,gray_img
def labels_for_training_data(directory):
    faces=[]
    faceID=[]
    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):                                                                                                             #Skipping system file
                continue
            id=os.path.basename(path)
            img_path=os.path.join(path,filename)
            test_img=cv2.imread(img_path)
            if test_img is None:
                                                                                                                                                    #Image not loaded properly
                continue
            faces_rect,gray_img=faceDetection(test_img)
            if len(faces_rect)!=1:
                continue
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID
def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=1)
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,5,(255,0,0),6)
def init(name):
    flag=0
    test_img=cv2.imread(name)
    face_detected,gray_img=faceDetection(test_img)
    #print(face_detected)
    faces,faceID=labels_for_training_data("C:\\Users\\Hp\\PycharmProjects\\cLook\\cLook\\train")
    face_recognizer=train_classifier(faces,faceID)
    face_recognizer.save("C:\\Users\\Hp\\PycharmProjects\\cLook\\cLook\\trainingData.yml")
    name={101:"Avinash",102:"Modi",103:"RamRaheem",104:"Asharam"}
    for faces in face_detected:
        (x,y,w,h)=faces
        roi_gray=gray_img[y:y+h,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        if confidence>50:
            draw_rect(test_img,faces)
            predicted_name=name[label]
            put_text(test_img,predicted_name,x,y)
            return label,predicted_name
        else:
            return "Not Found",""


def resize(name):
    img = cv2.imread(f'{name}', cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    width = 190
    height = 190
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f'{name}',resized)
    return init(name)