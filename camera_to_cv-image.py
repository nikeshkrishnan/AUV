
import cv2 
import imutils
import numpy as np
cX=0
Extreme=0
critcal_area_to_keep_min_dist=0
def nothing(y):
  pass
cv2.namedWindow('image')

cv2.createTrackbar('low_L','image',0,255,nothing)
cv2.createTrackbar('low_A','image',0,255,nothing)
cv2.createTrackbar('low_B','image',0,255,nothing)

cv2.createTrackbar('low1_L','image',0,255,nothing)
cv2.createTrackbar('low1_A','image',0,255,nothing)
cv2.createTrackbar('low1_B','image',0,255,nothing)

#cap = cv2.VideoCapture(0)

while True:
    #img_resp=requests.get(url2)
    
    #img_arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    
    img=cv2.imread('2.jpg')
    
   
        
    
    blur = cv2.GaussianBlur(img, (21, 21), 0)
    lab = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)
    lab_1 = cv2.cvtColor(blur, cv2.COLOR_BGR2YCR_CB)
    lower_lab = [cv2.getTrackbarPos('low_L', 'image'), cv2.getTrackbarPos('low_A', 'image'), cv2.getTrackbarPos('low_B', 'image')]

    lower_lab_1 = [cv2.getTrackbarPos('low1_L', 'image'), cv2.getTrackbarPos('low1_A', 'image'), cv2.getTrackbarPos('low1_B', 'image')]
    upper_lab =[255,255,255]
    lower = np.array(lower_lab, dtype="uint8")
    upper = np.array(upper_lab, dtype="uint8")
    lower_1 = np.array(lower_lab_1, dtype="uint8")
    upper_1 = np.array(upper_lab, dtype="uint8")
    mask_lab = cv2.inRange(lab, lower, upper)
    
    output = cv2.bitwise_and(img, img, mask=mask_lab) #note
    #thresh = cv2.threshold(output, 0, 255, cv2.THRESH_BINARY)[1]  #note
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print(cnts)
    cnts = imutils.grab_contours(cnts)  #note
    
    



    mask_lab_1 = cv2.inRange(lab_1, lower_1, upper_1)

    output_1 = cv2.bitwise_and(img, lab, mask=mask_lab_1) #note
    thresh_1 = cv2.threshold(output_1, 0,255, cv2.THRESH_BINARY)[1]  #note
    
    gray_1 = cv2.cvtColor(output_1, cv2.COLOR_BGR2GRAY)
    
    cnts_1 = cv2.findContours(gray_1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts_1= imutils.grab_contours(cnts_1)  #note
    dst = cv2.addWeighted(gray,0.5,gray_1,0.5,0)

    for c_1 in cnts_1:

     M = cv2.moments(c_1)
     cv2.drawContours(img, [c_1], -1, (0, 255, 0), 2)

     if(M["m00"]!=0):
      cX = int(M["m10"] / M["m00"])
     
    for c in cnts:

     M = cv2.moments(c)
     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)

     if(M["m00"]!=0):
      cX = int(M["m10"] / M["m00"])
     


      
    cv2.imshow("Image", img)

       
    cv2.imshow("Androidcam",dst)

    #put your image processing code here...........................
    if cv2.waitKey(1)==13:
     break