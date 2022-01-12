import cv2
import numpy as np

cap = cv2.VideoCapture('test1.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
model = cv2.createBackgroundSubtractorMOG2()
fps = cap.get(cv2.CAP_PROP_FPS)
video_rect = []
success,frame = cap.read()
size = (frame.shape[1],frame.shape[0])
while(True):
	success, frame = cap.read()
	if not success:
		break
	fgmk = model.apply(frame)
	fgmk = cv2.morphologyEx(fgmk,cv2.MORPH_OPEN,kernel)
	contours,_ = cv2.findContours(fgmk,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contours = contours
	cv2.waitKey(1000//int(fps))
	
	for c in contours:
		length = cv2.arcLength(c,True)
		if length>200:
			(x,y,w,h) = cv2.boundingRect(c)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow('fgmk',fgmk)
	cv2.imshow('frame',frame)
	video_rect.append(frame)
	cv2.waitKey(100//int(fps))
cap.release()
cv2.destroyAllWindows()

out_rect = cv2.VideoWriter('output_rect.mp4',cv2.VideoWriter_fourcc(*'DIVX'),fps,size)
for i in range(len(video_rect)):
	out_rect.write(video_rect[i])
out_rect.release()

