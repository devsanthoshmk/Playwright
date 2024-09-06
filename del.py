from selenium import webdriver
from time import time
import threading
st=time()
def sele(link):
    driver=webdriver.Firefox()
    st=time()
    driver.get(link)
    print(driver.title)
    driver.close()
    print(time()-st)
t1=threading.Thread(target=sele,args=("https://playwright.dev/python/docs/library",))
t2=threading.Thread(target=sele,args=("http://playwright.dev",))
t1.start()
t2.start()
t1.join()
t2.join()
print(time()-st)