import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent

"""
В проекте этот файл не используется, но пусть лежит пока что



"""
def webdriver_options(proxy, path, headless):
    
    #Настраиваем вебдрайвер прописываем прокси, путь к драйверу и режим хеадлесс
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent={useragent.random}")
    options.add_argument(proxy)
    
    #тихий режим работы
    if headless == 1:
        options.add_argument('headless')

    return  webdriver.Chrome(executable_path=path, options=options)

def send_addres(driver, adres, xpath_textarea, xpath_clean, xpath_select):

    otkuda = driver.find_element(By.XPATH, xpath_textarea)
    otkuda.send_keys(adres)
    if xpath_clean != 0:
        driver.find_element(By.XPATH, xpath_clean).click()
        otkuda.send_keys(adres)
    time.sleep(2)
    if xpath_select != 0:
        driver.find_element(By.XPATH, xpath_select).click()

def button_fix(driver):
    button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/button')
    if button is not None:
        button.click()

def yandex_taxi(from_where, where):
    url = "https://taxi.yandex.ru/"

    driver = webdriver_options('http://85.26.146.169', r"D:\\projects\\chromedriver\\chromedriver.exe", 0)

    try:
        #Переход по ссылке
        driver.get(url=url)
        time.sleep(2)
        try:
            #Нажимаем кнопку с местоположением если есть
            button_fix(driver)
        except:
            k = 0

        #заполняем поле откуда
        oxp_tx = '//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span[1]/span[2]/textarea'
        oxp_cl = '//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span[1]/span[1]'
        oxp_sl = '//*[@id="xuniq-0-1"]'
        send_addres(driver, from_where, oxp_tx, oxp_cl, oxp_sl)
        
        #заполняем поле куда
        kxp_tx = '//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/span[1]/span[2]/textarea'


        kxp_sl = "/html/body/div[3]/div/div[1]"
        send_addres(driver, from_where, kxp_tx, 0, kxp_sl)

        time.sleep(111)
        


        time.sleep(999)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
    driver.quit()

def main():
    yandex_taxi("Мира 112 Тольятти", "Аэрохлл Тольятти")

main()

