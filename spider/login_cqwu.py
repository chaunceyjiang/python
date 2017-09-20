import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time
loginURL = 'http://218.194.177.14/jwmis/_data/login.aspx'
ocrURL='http://139.199.183.119/?img=true'
sourceURL='http://218.194.177.14/jwmis/'

phantomjsPATH=r'C:\Python\phantomjs\bin\phantomjs.exe'
chromePATH=r'C:\Python\phantomjs\bin\chromedriver.exe'
def ocr():
    with open('a.png','rb') as f:
        response=requests.post(url=ocrURL,data=f)
        return response.text
def phantomJS(url):
    try:
        driver=webdriver.Chrome(executable_path=chromePATH)
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        driver.switch_to.frame(0)
        driver.maximize_window()#窗口最大化
        driver.find_element_by_name('txt_asmcdefsddsd').clear()
        driver.find_element_by_name('txt_asmcdefsddsd').send_keys('201458254036')
        driver.find_element_by_id('txt_pewerwedsdfsdff').clear()
        driver.find_element_by_id('txt_pewerwedsdfsdff').send_keys('xxxx')
        driver.find_element_by_name('txt_sdertfgsadscxcadsads').clear()#网页默认需要点击验证码才会显示，所以这里单机验证码输入框，以显示验证码
        driver.save_screenshot('screenshot.png')#保存屏幕截图
        i = Image.open("screenshot.png")
        frame4 = i.crop((330,278,408,297))#定位验证码位置（这里是将验证码的位置写死了，因为还不知道怎么动态的获取验证码位置。。。。）
        frame4.save('a.png')#保存验证码
        code=ocr()#OCR识别，这里调用的是在线的验证码识别，也可以改用
        a=driver.find_element_by_name('txt_sdertfgsadscxcadsads')
        a.send_keys(code)
        x=a.submit()#提交数据
        print('--------------',x,'---------------')
        time.sleep(5)
        driver.switch_to.frame(2)
        driver.find_element_by_id('memuBarText7').click()
        driver.find_element_by_xpath('//*[@id="memuLinkDiv7"]/table/tbody/tr[11]/td[2]/span').click()
        driver.switch_to.frame(0)
        driver.find_element_by_xpath('//input[@id="SelXNXQ_0"]').click()
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/input[1]').click()
        time.sleep(20)
        print(driver.page_source)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        os.remove("screenshot.png")#移除临时文件
        os.remove('a.png')
phantomJS(sourceURL)
