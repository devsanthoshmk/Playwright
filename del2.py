from playwright.sync_api import sync_playwright
from time import time
import threading
def sele(link):
    with sync_playwright() as p:
        st=time()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(link)
        print(page.title())
        print(time()-st)
        browser.close()
st=time()
t1=threading.Thread(target=sele,args=("https://playwright.dev/python/docs/library",))
t2=threading.Thread(target=sele,args=("http://playwright.dev",))
t1.start()
t2.start()
t1.join()
t2.join()
print(time()-st)