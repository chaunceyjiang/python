from PIL import Image,ImageFont,ImageDraw
import os
def Modify_Image(Image_Path,num=1):
    img=Image.open(Image_Path)
    mod_img=ImageDraw.Draw(img)
    myfont=ImageFont.truetype(r"C:\Windows\Fonts\Verdana.ttf",36)
    mod_img.text((img.size[1]*3/4,0),str(num),fill=(255,0,0),font=myfont)
    save_path=os.path.dirname(Image_Path)+os.sep+"modify"+os.path.splitext(Image_Path)[1]
    img.save(save_path)

if __name__=="__main__":
    path=r"C:\Users\chauncey\Desktop\c.jpg"
    Modify_Image(path,4)
