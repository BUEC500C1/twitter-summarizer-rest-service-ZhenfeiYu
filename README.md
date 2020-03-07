# video-ZhenfeiYu
video-ZhenfeiYu created by GitHub Classroom
## Requirements
* Convert text into an image in a frame
* Do a sequence of all texts and images in chronological order.
* Display each video frame for 3 seconds
## Presets
* Environment prepare
```
pip3 install tweepy
pip3 install os
```
```
pip3 install Pillows
```
```
pip3 install --upgrade pip
pip3 install opencv-python
```
## Use Twitter API Search for tweets
* Apply for twitter api keys
* Output ten tweets related to searchword
* Save tweets to a txt file
## Convert Tweets to Image
* Use python PIL package
* Set image parameters, like font and background color
* Save the pictures to a folder named "images"
## Generate Video of Images
* Import python cv2 package
```
video=cv2.VideoWriter('../'+foldername+'/'+foldername+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.5,(1280,720)) 
```
## Queue System
* Develop a queue system that can exercise your requirements with stub functions.
* Develop the twitter functionality with an API.
* Integrate them
```
foldername = ['blakelively','sehun','baekhyun','evanlin','chanyeol','EXO']
    keyword = ['blakelively','sehun','baekhyun','evanlin','chanyeol','EXO']
    source = (('blakelively','blakelively'),('sehun','sehun'),('baekhyun','baekhyun'),('evanlin','evanlin'),('chanyeol','chanyeol'),('EXO','EXO'))
```
<div align=center><img src="https://github.com/BUEC500C1/video-ZhenfeiYu/blob/master/images/1.png"/></div>
