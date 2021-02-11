import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import getpass


option = Options()

option.add_argument("start-maximized")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
option.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

#login

def login(email , password , driver):

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "email")) 
    )
    element.send_keys(email)

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "pass")) 
    )
    element.send_keys(password)

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.NAME, "login")) 
    )
    element.click()


# add friend with same location

def add_friend(friend_name,driver):

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[1]/a')))
    element.click()


    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')) 
    )
    element.click()


    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.pxsmfnpt.pedkr2u6.n1dktuyu.dvqrsczn.l23jz15m.d4752i1f > div > div > div > div > div > div > a:nth-child(3) > div.bp9cbjyn.rq0escxv.j83agx80.pfnyh3mw.frgo5egb.l9j0dhe7.cb02d2ww.hv4rvrfc.dati1w0a > span')) )

    element.click()

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.LINK_TEXT, "Places lived")) 
    )
    element.click()


    city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.c9zspvje:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
    city = city.text

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.XPATH, "//input[@class ='oajrlxb2 rq0escxv f1sip0of hidtqoto lzcic4wl hzawbc8m ijkhr0an nlq1og4t sgqwj88q b3i9ofy5 oo9gr5id b1f16np4 hdh3q7d8 dwo3fsh8 qu0x051f esr5mh6w e9989ue4 r7d6kgcz br7hx15l h2jyy9rg n3ddgdk9 owxd89k7 ihxqhq3m jq4qci2q k4urcfbm iu8raji3 qypqp5cg l60d2q6s hv4rvrfc hwnh5xvq dati1w0a o1lsuvei nhd2j8a9 aj8hi1zk r4fl40cc kd8v7px7 m07ooulj mzan44vs']")) 
    )
    element.send_keys(friend_name)
    element.send_keys(Keys.RETURN)

    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.LINK_TEXT, "People")) 
    )
    element.click()


    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.l8hfysis:nth-child(2)")))
    element.click()



    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH , "//div[@class = 'l9j0dhe7']/div/input")))
    element.send_keys(city)

    i = random.randint(1,10)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , f'//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[{i}]/div/div/div/div/div/div/div[3]/span/div/i')))
    element.click()


# update status

def status_update(status,driver):

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[1]/a')))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@class = "oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 ni8dbmo4 stjgntxs kbf60n1y"]')))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')))
    element.send_keys(status)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div')))
    element.click()

    driver.implicitly_wait(5)


# comment

def comment_on_friend_post(comment,driver):

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[1]/a')))
    element.click()

    element = WebDriverWait(driver, 15).until( 
        EC.visibility_of_element_located((By.XPATH , '//*[@class="buofh1pr"]/ul/li/div/a')) 
    )
    element.click()


    element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.rq0escxv.lpgh02oy.du4w35lb.rek2kq2y > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.i1fnvgqd.gs1a9yip.owycx6da.btwxx1t3.pxsmfnpt.pedkr2u6.n1dktuyu.dvqrsczn.l23jz15m.d4752i1f > div > div > div > div > div > div > a:nth-child(4)')))

    element.click()

    i = random.randint(1,5)

    driver.execute_script("window.scrollBy(0, 250)")

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , f'#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div > div > div > div:nth-child(1) > div > div > div > div > div.j83agx80.btwxx1t3.lhclo0ds.i1fnvgqd > div:nth-child({i}) > div:nth-child(1) > a')))
    element.click()

    driver.execute_script("window.scrollBy(0, 500)")

    element = WebDriverWait(driver , 20).until(EC.presence_of_element_located((By.CSS_SELECTOR , '#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.hpfvmrgz.gile2uim.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div:nth-child(3) > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.cwj9ozl2.tvmbv18p > div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a.j83agx80.btwxx1t3.lzcic4wl > div.g3eujd1d.ni8dbmo4.stjgntxs.rz4wbd8a > div._25-w > div > div > div > form > div > div > div._5rpb > div > div > div > div')))
    element.click()

    element = WebDriverWait(driver , 20).until(EC.presence_of_element_located((By.XPATH , '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div/div/div/div')))
    element.send_keys(comment)
    element.send_keys(Keys.RETURN)


if __name__ == "__main__":
    
    email = input("Enter your email : \n")
    password = getpass.getpass("Enter password : \n")
    driver = webdriver.Chrome(chrome_options=option, executable_path="chromedriver.exe")
    driver.get("https://www.facebook.com/")
    login(email , password, driver)

    while True:

        ans = input("\n\n Press (A) to add friend from same location \nPress (S) to update status \nPress (C) to comment on random friend's first post \nPress (Q) to exit \n\n  Enter :- ").lower()

        if ans == "a":
            name = input("\n Enter name : ")
            add_friend(name , driver)

        elif ans == "s":
            status = input("\n Enter status : ")
            status_update(status, driver)

        elif ans == "c":
            comment = input("\n Enter comment : ")
            comment_on_friend_post(comment, driver)

        elif ans == "q":
            driver.close()
            break
