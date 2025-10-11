import click
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from openpyxl import load_workbook
import time

driver = webdriver.Chrome(
    executable_path=r"/Users/clcx/Documents/Calvin/Random/chromedriver")

# buka web crm
driver.get("https://crm.xcyunxt.com/xccrm/#/clue/index")

# set id pass
usn = '15006106002'
pwd = 'A@1234xc'

# excel workbook
filepath = '/Users/clcx/Documents/Calvin/Clients Data/Winna/9.xlsx'
wb = load_workbook(filepath)

sheetRange = wb['Sheet1']


def clear():  # clear form
    try:
        WDW(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]')))

        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[1]/input').clear()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[6]/div[1]/div/div/div[1]/input').clear()
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[6]/div[2]/div[1]/div/div/div/input').clear()
    except:
        print('NOT SHOWING')


def clickable(element: str) -> None:  # clickable
    try:
        element = WDW(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, element)))
        element.click()
    except:
        print(element + ' IS NOT SHOWING')

def close_repetition():
    try:
        for i in range(3):
            clickable('/html/body/div[2]/div/div[1]/button')
            clickable('/html/body/div[3]/div/div[1]/button/i')
            print('warning alert closed')
            time.sleep(.5)
    except:
        print('NOT SHOWING')

def close_duplicate():
    try:
        WDW(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]')))
        driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/button/i').click()
        print('duplicate alert closed')
    except:
        print('NOT SHOWING DUPLICATE ALERT')
    time.sleep(2)

def close_existing():
    try:
        WDW(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[3]/div/div[1]')))
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/button/i').click()
        print('existing alert closed')
    except:
        print('NOT SHOWING EXISTING ALERT')
    time.sleep(2)

# login crm
username = driver.find_element(By.NAME, 'username')
username.clear()
username.send_keys(usn)
password = driver.find_element(By.NAME, 'password')
password.clear()
password.send_keys(pwd)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/button').click()


# pilih CRM
clickable('//*[@id="app"]/div/div[1]/div[4]/div[1]/div[1]/img')

# buka bagian input data
# ganti focus ke tab baru
driver.switch_to.window(driver.window_handles[1])

# panah bawah
clickable('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
driver.implicitly_wait(3)

# pilih isi data
clickable('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[6]/a/li')
time.sleep(5)


def input_data(i: int) -> None: # input data
    # tambah data baru
    clickable('//*[@id="app"]/div/div[2]/section/div/div/div[1]/div[1]/button[1]')

    olshop_name = sheetRange['D'+str(i)].value
    firm_name = sheetRange['C'+str(i)].value
    boss_name = sheetRange['B'+str(i)].value
    phone_number = sheetRange['A'+str(i)].value

    # masukin data
    try:
        WDW(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]')))
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[1]/input').send_keys(olshop_name)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys(firm_name)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[6]/div[1]/div/div/div[1]/input').send_keys(boss_name)
        driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[6]/div[2]/div[1]/div/div/div/input').send_keys(phone_number)
    except:
        print('NOT SHOWING')
    
    time.sleep(3)

    # kalo muncul alert catet ke excel + clear form
    try:
        WDW(driver, 2).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]')))
        sheetRange['E'+str(i)].value = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/span[2]').text
        sheetRange['F'+str(i)].value = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[5]/span[2]').text
        wb.save(filepath)
        clear()
        print('NOTED on '+str(i))
    except:
        print('DID NOT NOTE')
        print(driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/span[2]').text)
        print(driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[5]/span[2]').text)

    close_existing()
    # matiin alert
    close_repetition()
    close_duplicate()
    close_existing()

    # save changes
    clickable('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/form/div[7]/div/button[1]')
    sheetRange['G'+str(i)].value = 'OK'
    close_repetition()

    # click close form
    clickable('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/button/i')
    
    time.sleep(2)

for i in range (2,32):
    input_data(i)
