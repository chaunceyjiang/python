from PIL import Image
import pytesseract
import time,os

def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img
def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)
i=1

while i<=306:
    try:
        
        img=Image.open(r"C:\Users\chauncey\Desktop\image"+"\\"+str(i)+".jpg").convert('L')
    except:
        continue
    
    img=binarizing(img,180)

    img=depoint(img)
    time.sleep(1)
    img.show()
    img=depoint(img)
    code=pytesseract.image_to_string(img)
    time.sleep(1)
    img.show()
    
    print(i,":",code)
    i+=1

    kill_by_process_name_shell("Microsoft.Photos.exe")
    img.close()
    time.sleep(1)
    img=None
input()
