from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent


def yandex_taxi(from_where, where):

    url = "https://taxi.yandex.ru/"

    #Настраиваем вебдрайвер
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent={useragent.random}")
    options.add_argument('http://' + '85.26.146.169')

    #тихий режим работы
    #options.add_argument('headless')

    #Указываем путь к chromedriver
    driver = webdriver.Chrome(executable_path=r"D:\\projects\\chromedriver\\chromedriver.exe", options=options)

    try:
        #Переход по ссылке
        driver.get(url=url)
        time.sleep(2)
        try:
            #Нажимаем кнопку с местоположением если есть
            button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/button')
            if button is not None:
                button.click()
        except:
            k = 0

        #Находим поле ввода откуда, очищаем его и отправляем туда наше местоположение
        otkuda = driver.find_element(By.XPATH,'//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span[1]/span[2]/textarea')
        
        otkuda.send_keys(from_where)
        driver.find_element(By.XPATH, '//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/span[1]/span[1]').click()
       
        otkuda.send_keys(from_where)
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="xuniq-0-1"]').click()
        

        #Находим поле ввода куда, очищаем его и отправляем туда наше местоположение
        kuda = driver.find_element(By.XPATH,'//*[@id="application"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/span[1]/span[2]/textarea')
                                            
        kuda.send_keys(from_where)
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="xuniq-0-27"]').click()

        time.sleep(999)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
    driver.quit()

def main():
    yandex_taxi("Мира 112 Тольятти", "Аэрохлл Тольятти")

main()