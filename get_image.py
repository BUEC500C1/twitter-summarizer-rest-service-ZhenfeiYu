from PIL import Image  
from PIL import ImageDraw  
import twitter
from PIL import ImageFont  

def tweet2image(username,searchword):  
    list_word = twitter.get_tweets(username,searchword)
    address = username+'/'+username+'_images/'
    #build a white background 
    for i in range(0,len(list_word)):
        font = ImageFont.truetype('./DejaVuSerif-Italic.ttf', 15)
        word = list_word[i].encode('ascii', 'ignore').decode('ascii')
        image = Image.new('RGB', (500, 312), color = (190, 226, 231))  
        draw = ImageDraw.Draw(image)  
        draw.text((5, 200), word, fill = (0,0,0), font=font)  
        j = str(i+1)
        image.save(username+'/'+username+'_images/'+j+'.jpg',dpi=(300.0,300.0))
        # image.show()
    return  address

# if __name__ == '__main__':
   
#     foldername = input('Enter your foldername: ')
#     searchword = input('Enter the searchword you would like to search: ')
#     tweet2image(foldername, searchword)
