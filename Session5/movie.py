from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/yschae/Desktop/NEXT_HW/Session5/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기
driver.get("https://movie.naver.com/")

# 1위부터 20위까지 가져오기
chartbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
chartbtn.click()

for i in range(2,11):
    rank = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
 
    print(i-1, rank)


for k in range(13,23):
    rank2 = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{k}]/td[2]/div/a').text
    print(k-2, rank2)

#감독 개요 평점
detail = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/div/a')
detail.click()

rate= driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em").text
genre= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a[1]").text
genre2= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a[2]").text
director= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a").text
print(rate, genre, genre2, director)

#좋아하는 영화 검색
time.sleep(1)
search=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/fieldset/div/span/input")
search.click()
time.sleep(1)
name="그 시절, 우리가 좋아했던 소녀"
search.send_keys(name)
searchbtn= driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/fieldset/div/button")
searchbtn.click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[2]/dl/dt/a/strong").click()
favname= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/h3/a").text
favdir= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a").text
print(favname , "\n", favdir)

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

rating= driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]").text
print("\n")
print(rating)

file = open("movie.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["댓글", "좋아요 수", "닉네임"])

for j in range(1, 6):
 comment = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[4]/ul/li[{j}]/div[2]/p").text
 like = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[4]/ul/li[{j}]/div[3]/a[1]/strong").text
 user = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[4]/ul/li[{j}]/div[2]/dl/dt/em[1]/a/span").text
 writer.writerow([comment, like, user])
 print(comment, like, user)
file.close()