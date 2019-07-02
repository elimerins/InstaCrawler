import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys


#realsource
driver=webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
account='cooicu'
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

#게시물 갯수 확인하는 코드, 다만 bs를 쓰기때문에 조금 느려짐.
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
contentNum=soup.find('span',{'class':'g47SY'}).text
contentNum=contentNum.replace(',',"")
count=0
for i in range(2000):
    if len(urls)==int(contentNum)-3:
        break
    html = driver.page_source
    time.sleep(1)
    soup = BeautifulSoup(html, "html.parser")
    for alpha in soup.findAll('div',{'class':'v1Nh3 kIKUG _bz0w'}):
        url=alpha.find('a')['href']
        if url not in urls:
            urls.append(url)
            count+=1
            print(url+' '+str(count)+' '+contentNum)
            if len(urls) == int(contentNum)-3:
                break
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)

print('Crawling Start\n')
for idx,url in enumerate(urls):
    print('\n'+str(idx+1)+'/'+str(len(urls)))
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

    savename_img = datetime + ".png"
    savename_video=datetime + ".mp4"
    fullfilename_img = os.path.join('C:\\Users\\elime\\PycharmProjects\\instarCrawler\\' + account + '\\', savename_img)
    fullfilename_video = os.path.join('C:\\Users\\elime\\PycharmProjects\\instarCrawler\\' + account + '\\', savename_video)

    if os.path.isfile(fullfilename_img) or os.path.isfile(fullfilename_video):
        print(datetime+" is already Exist")
        print('Program will be terminated')
        break

    else:
        try:

            elapa = soup.find('div', {'class': '_5wCQW'})
            mediaurl = elapa.find('video')['src']
            print(mediaurl)
            print("Video Found")
            # count=nextPic(count)

            print(fullfilename_video)
            try:
                print(datetime)
                urllib.request.urlretrieve(mediaurl, "./" + account + "/" + savename_video)
                print(savename_video + " is saved.")

            except Exception as inst:
                print(type(inst))
                print("Nope")
                driver.quit()


        except Exception as inst:

            elapa = soup.find('div', {'class': 'KL4Bh'})
            mediaurl = elapa.find('img')['src']
            print(mediaurl)
            print("Image Found")

            print(fullfilename_img)
            try:
                print(datetime)
                urllib.request.urlretrieve(mediaurl, "./" + account + "/" + savename_img)
                print(savename_img + " is saved.")

            except Exception as inst:
                print(type(inst))
                print("Nope")
                driver.quit()

            continue
driver.quit()