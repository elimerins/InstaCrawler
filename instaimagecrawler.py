import urllib.request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import os
'''
#url은 직접 지정하면 당연히 편하지만, 이걸 변수화할 수 있는가?

#각 이미지별 xpath
# /html/body/div[3]/div[2]/div/article/div[1]/div/div/div[1]/img
# value가 src의 URL
url='https://scontent-icn1-1.cdninstagram.com/vp/3679a2aab2d4139c96fca74a6bf6ab21/5D7A439D/t51.2885-15/e35/p1080x1080/59437726_147637629620230_8042594664446725464_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com'

savename="test.png"

urllib.request.urlretrieve(url,savename)

print(savename+" saved")
'''
'''

셀레니움 단일 사진 긁어오는 소스
driver=webdriver.Chrome('C:\\Users\\elime\\PycharmProjects\\instarCrawler\\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('https://www.instagram.com/p/Bxj2yyFnlVx/')

url=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[1]/img').get_attribute('src')

savename="test.png"

urllib.request.urlretrieve(url,savename)

print(savename+" saved")
driver.quit()
'''

driver=webdriver.Chrome('C:\\Users\\elime\\PycharmProjects\\instarCrawler\\chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/chuu__chloe')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()

time.sleep(2)

print(driver.current_url)

html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

elapa=soup.find('div',{'class':'KL4Bh'})


elapa=elapa.find('img')
print(elapa.name)#string type
print(type(elapa.name))

'''
while True:
    datetime=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time').get_attribute('datetime')
    datetime=datetime.replace(':','-')
    datetime=datetime[:19]
    if os.path.isfile(datetime+".png"):
        print(datetime+" is already Exist")
    else:
        if count==0:
            url = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
        else:
            try:
                url = driver.find_element_by_xpath(
                '/ html / body / div[4] / div[2] / div / article / div[1] / div / div / div[1] / img').get_attribute('src')
            except Exception as inst:
                try:
                    url = driver.find_element_by_xpath(
                    '/ html / body / div[4] / div[2] / div / article / div[1] / div / div / div[1] / div[1] / img').get_attribute(
                    'src')
                except Exception as inst:
                    print("Not Found")
                    continue

        bs4를 활용하여 첫번째 태그 img,video 일 경우로 분리하여 계산.
        savename = datetime+".png"
        try:
            print(datetime)
            urllib.request.urlretrieve(url, savename)
            print(savename+" is saved.")

        except Exception as inst:
            print(type(inst))
            print("Nope")
            driver.quit()

    if count==0:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
    else:
        driver.find_element_by_xpath('/ html / body / div[4] / div[1] / div / div / a[2]').click()
    count+=1
    time.sleep(2)

'''