import os
import cv2
import get_image
import sys

def tweet2video(username,searchword):
    file_dir=get_image.tweet2image(username,searchword)
    list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
           list.append(file)
    video=cv2.VideoWriter(username+'/'+username+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.5,(1280,720))   
    for i in range(1,len(list)+1):
        img=cv2.imread(file_dir+list[i-1])  #read the images
        img=cv2.resize(img,(1280,720)) #transfer images to 1280*720
        video.write(img)   #write the video
    video.release()

if __name__ == '__main__':
    tweet2video(sys.argv[1],sys.argv[2])
#    foldername = input('Enter your foldername: ')
#    searchword = input('Enter the searchword you would like to search: ')
#    tweet2video(foldername,searchword)
