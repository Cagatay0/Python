import os
from PIL import Image

def renameFunc():
    path = "/Users/cagatay/Desktop/renameBeforeTheme/" #folder path
    dir_list=os.listdir(path)
    i=10
    for fileName in dir_list:
        splitText=fileName.split('.')
        f1= splitText[0]
        f2=splitText[1]
        oldName="/Users/cagatay/Desktop/renameBeforeTheme/"+f1+"."+f2
        newName="/Users/cagatay/Desktop/renameBeforeTheme/"+str(i)+".jpg"
        os.rename(oldName,newName)
        i+=10
 
def imgCompressWorkedFunc():
    folder_path= "/Users/cagatay/Desktop/beforeUploadStorage/" #folder path
    dir_list=os.listdir(folder_path)
    for fileName in dir_list:
        if(fileName !='.DS_Store'):
            splitText=fileName.split('.')
            fileNameFirst=splitText[0]
            fileNameLast=splitText[1]
            img_comp_path=folder_path+fileNameFirst+'.'+fileNameLast
            size_mb = os.path.getsize(img_comp_path)/(1024*1024) #get file size
            if(size_mb>1):
                print('------:'+img_comp_path+':::::  '+str(size_mb))
                with Image.open(img_comp_path) as img:
                    width,height=img.size
                    new_width= width/2
                    new_height=height/2
                    resized_img = img.resize((int(new_width),int(new_height)))
                    rgb_image=resized_img.convert('RGB')  
                    rgb_image.save('/Users/cagatay/Desktop/beforeUploadStorage/'+fileNameFirst+'.jpg')  