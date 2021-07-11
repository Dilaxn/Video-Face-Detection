#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:21:27 2021

@author: dilaxn
"""


import cv2
import face_recognition

webcam_video_stream = cv2.VideoCapture(0)

while True:
    
    ret,current_frame = webcam_video_stream.read()

    current_frame_small= cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)

    all_faces = (face_recognition.face_locations(current_frame_small,model='hog'))

    for index,face in enumerate(all_faces):
        top_pos , right_pos,bottom_pos,left_pos = face
        top_pos =top_pos*4
        left_pos=left_pos*4
        bottom_pos=bottom_pos*4
        right_pos=right_pos*4
        print('found face {} at top:{},right :{},bottom :{},lef:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
        cv2.rectangle(current_frame, (left_pos,top_pos),(right_pos,bottom_pos) , (100,0,155),2)
        cv2.imshow("viudeo", current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam_video_stream.release()
cv2.destroyAllWindows()    