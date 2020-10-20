import time
from selenium import webdriver
timer =5
link='https://www.youtube.com/watch?v=9-1RyGDKACs'
views=20
driver=webdriver.Chrome()
driver.get(link)
for i in range(views):
	time.sleep(timer)
	driver.refresh()
	print(str(i)+'th iteration completed')