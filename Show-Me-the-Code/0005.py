import os
from PIL import Image

def resize_img(path):
    print(os.getcwd())
    imges=os.listdir(path)
    for i in imges:
        img=Image.open(i)
        print(img.size)
        w=min(img.size[0],1136)
        h=min(img.size[1],640)
        print(w,h)
        reimg=img.resize((w,h),Image.ANTIALIAS)
        reimg.save(os.path.dirname(path)+os.sep+"modify_"+i)
if __name__=="__main__":
    path="C:\\Users\\chauncey\\Desktop\\aa\\"
    os.chdir(path)
    resize_img(path)

