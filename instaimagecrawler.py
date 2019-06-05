import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

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

#realsource
driver=webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
account='bodyon_bikini'
instagram_addr='https://www.instagram.com/'
driver.get(instagram_addr+account)
time.sleep(3)

#dir이 없다면, DIR을 만들어줌
if not (os.path.isdir(account)):
    os.makedirs(os.path.join(account))#account 명으로 dir 생성


def nextPic(count):
    if count == 0:
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
    else:
        driver.find_element_by_xpath('/ html / body / div[4] / div[1] / div / div / a[2]').click()

    count += 1
    return count

urls=[]
checkend=0

for i in range(200):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    for alpha in soup.findAll('div',{'class':'v1Nh3 kIKUG _bz0w'}):
        url=alpha.find('a')['href']
        if url not in urls:
            print(url)
            urls.append(url)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)

for url in urls:
    print(instagram_addr+account+url)
    driver.get(instagram_addr+account+url)
    driver.implicitly_wait(3)
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    datetime=soup.find('time')['datetime']
    print(datetime)
    datetime = datetime.replace('T', 'T ')
    datetime=datetime.replace(':','_')
    datetime=datetime[:20]
    savename = datetime + ".png"
    fullfilename = os.path.join('C:\\Users\\elime\\PycharmProjects\\instarCrawler\\' + account + '\\', savename)

    if os.path.isfile(fullfilename):
        print(datetime+" is already Exist")
    else:
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            elapa = soup.find('div', {'class': 'KL4Bh'})
            imgurl=elapa.find('img')['src']
            print(imgurl)

        except Exception as inst:
            print("Not Found")
            #count=nextPic(count)
            continue

        #count=nextPic(count)

        #bs4를 활용하여 첫번째 태그 img,video 일 경우로 분리하여 계산.

        print(fullfilename)
        try:
            print(datetime)
            urllib.request.urlretrieve(imgurl, "./"+account+"/"+savename)
            print(savename+" is saved.")

        except Exception as inst:
            print(type(inst))
            print("Nope")
            driver.quit()

driver.quit()
    #count=nextPic(count)