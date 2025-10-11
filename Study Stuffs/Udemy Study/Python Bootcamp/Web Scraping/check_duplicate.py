from tkinter import *
from tkinter import messagebox
import click
from pandas import options

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# DRIVER

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--windows-size=1200x638")
driver = webdriver.Chrome(
        executable_path=r"/Users/clcx/Documents/Calvin/Random/chromedriver",options=chrome_options)
driver.set_window_size(1200,638)

shop_name = ''

# buka web crm
driver.get("https://crm.xcyunxt.com/xccrm/#/clue/index")

# set id pass
usn = '15006106002'
pwd = 'A@1234xc'

def clickable(element: str) -> None:  # clickable
    try:
        element = WDW(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, element)))
        element.click()
    except:
        pass

def start():
    username = driver.find_element(By.NAME, 'username')
    username.clear()
    username.send_keys(usn)
    password = driver.find_element(By.NAME, 'password')
    password.clear()
    password.send_keys(pwd)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/button').click()

    driver.get('https://crm.xcyunxt.com/xccrm/#/clue/index')
    driver.get_screenshot_as_file('clue.png')
    
    '''# pilih CRM
    clickable('//*[@id="app"]/div/div[1]/div[4]/div[1]/div[1]/img')
    # buka bagian input data
    # ganti focus ke tab baru
    driver.switch_to.window(driver.window_handles[1])
    driver.set_window_size(1200,638)

    # panah bawah
    clickable('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
    driver.implicitly_wait(3)

    # pilih isi data
    #clickable('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul/div[2]/li/ul/div[7]/a/li/span')
    clickable('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[7]/a/li')
    #clickable('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul/div[2]/li/ul/div[7]/a/li/span')'''
    time.sleep(3)
    messagebox.showinfo(message='Program is ready!')

def clear():
    try:
        WDW(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]')))
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[1]/input').clear()
    except:
        pass

def input():
    clear()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    clickable('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[1]/button[1]')
    driver.get_screenshot_as_file('afterclick.png')
    try:
        WDW(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]')))
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[1]/input').send_keys(shop_name_box.get())
        # asal isi aja biar cursor pindah
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(' ')
    except:
        print('LOL STILL NOT WORKING BUDDY, TRY AGAIN🌚')

def check():
    for i in range(2,6):
        try:
            WDW(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div['+str(i)+']/div/div[2]/div/div/div[2]/div/div[3]/span[2]')))
            if ((driver.find_element(By.XPATH,'/html/body/div['+str(i)+']/div/div[2]/div/div/div[2]/div/div[3]/span[2]').text) == ''):
                messagebox.showinfo(message='OK')
                driver.get_screenshot_as_file('result.png')
                print('OK')
                break
            else:
                messagebox.showinfo(message='Already exists!')
                print(driver.find_element(By.XPATH,'/html/body/div['+str(i)+']/div/div[2]/div/div/div[2]/div/div[3]/span[2]').text)
                driver.get_screenshot_as_file('result.png')
                break
        except:
            continue
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def input_check() -> None:
    input()
    check()

# MAIN
gui = Tk()
gui.title('🟥🟧🟨🟩🟦🟪')
gui.geometry('275x70')

start_button = Button(gui, command=start, text='START', font=(14), bg='red')
start_button.grid(row=1, column=1, sticky=W)

shop_name_box = Entry(gui, textvariable=shop_name, font=(14))
shop_name_box.grid(row=2, column=1)

inputcheck_button = Button(gui, command=input_check, text='CHECK', font=(14), bg='red')
inputcheck_button.grid(row=2, column=2)

'''
input_button = Button(gui, command=input, text='INPUT', font=(14), bg='red')
input_button.grid(row=2, column=2)

check_button = Button(gui, command=check, text='CHECK', font=(14), bg='red')
check_button.grid(row=2, column=3)
'''

gui.mainloop()