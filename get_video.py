import os
import cv2
import get_image

def get_video(foldername,searchword):
    file_dir=get_image.draw_test(foldername,searchword)
    list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
           list.append(file)
    video=cv2.VideoWriter('../'+foldername+'/'+foldername+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.5,(1280,720)) 
    for i in range(1,len(list)+1):
        img=cv2.imread(file_dir+list[i-1]) 
        img=cv2.resize(img,(1280,720))
        video.write(img)
    video.release()
    print("Video generated!")

if __name__ == '__main__':
   
    foldername = input('Enter your foldername: ')
    searchword = input('Enter the searchword you would like to search: ')
    get_video(foldername,searchword)