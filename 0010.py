import string
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
img=Image.new('RGBA',(240,60),(160,160,160,100))
count=0

#颜色点
while count <2000:
    randX=random.randint(0,240-1)
    randY=random.randint(0,60-1)
    img.putpixel((randX,randY),(random.randint(10,255),random.randint(10,255),random.randint(10,255)))
    count+=1

#字体
myfont=ImageFont.truetype(r"C:\Windows\Fonts\Verdana.ttf",39)

nimg=ImageDraw.Draw(img)

#文字
nimg.text((random.randint(0,70-random.randint(0,20)),random.randint(3,17)),random.choice(string.ascii_letters),fill=(random.randint(100,255),random.randint(100,255),random.randint(100,255)),font=myfont)
nimg.text((random.randint(60,130-random.randint(0,20)),random.randint(6,20)),random.choice(string.ascii_letters),fill=(random.randint(100,255),random.randint(100,255),random.randint(100,255)),font=myfont)
nimg.text((random.randint(120,190-random.randint(0,20)),random.randint(2,8)),random.choice(string.ascii_letters),fill=(random.randint(100,255),random.randint(100,255),random.randint(100,255)),font=myfont)
nimg.text((random.randint(180,230-random.randint(0,20)),random.randint(4,15)),random.choice(string.ascii_letters),fill=(random.randint(100,255),random.randint(100,255),random.randint(100,255)),font=myfont)

#高斯模糊 参考：http://www.daima234.com/9/686287.html
img=img.filter(ImageFilter.GaussianBlur(1))

img.show()
