from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pip._vendor import requests

import time

link = 'https://piter-online.net/'
browser = webdriver.Chrome()
browser.get(link)


def scrolling_page():
    """Выполнение скроллинга страницы"""
    browser.execute_script('window.scrollTo(0, 200);')
    time.sleep(1)


STREET_NAME = '/html/body/div[1]/div/div[1]/div[3]/div[1]/div/div/div/' \
              'div[2]/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/input'
NUMBER_HOUSE = '/html/body/div[1]/div/div[1]/div[3]/div[1]/div/div/div/' \
               'div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/input'
TYPE_CONNECTION = '/html/body/div[1]/div/div[8]/div[1]/div/div/div/ul/li[1]'
CHOICE_TARIFF = '/html/body/div[1]/div/div[1]/div[3]/div[1]/div/div/div/' \
                'div[2]/div/div[1]/div/div[3]/div/div'
CLOSE_WINDOW = '/html/body/div[1]/div/div[4]/div/div/div/div/div/span'

# ШАГ 1
# Вводим наименование улицы
search_string_street = browser.find_element(By.XPATH, STREET_NAME)
search_string_street.send_keys('Тестовая линия')
time.sleep(1)
search_string_street.send_keys(Keys.ENTER)

# Вводим номер дома
search_string_house = browser.find_element(By.XPATH, NUMBER_HOUSE)
search_string_house.send_keys('1')
time.sleep(1)
search_string_house.send_keys(Keys.ENTER)

# Скроллинг страницы
scrolling_page()

# Выбрать подключение
search_string_flat = browser.find_element(By.XPATH, TYPE_CONNECTION)
search_string_flat.click()

# Показать тарифы
search_tariff = browser.find_element(By.XPATH, CHOICE_TARIFF)
search_tariff.click()

# Прогрузить страницу
time.sleep(2)

# Закрыть окно про доступные тарифы
close_window = browser.find_element(By.XPATH, CLOSE_WINDOW)
close_window.click()

# ШАГ 2
for i in range(5):
    # Скроллинг страницы
    scrolling_page()

    # Кликаем на подключить
    choice_tariff = browser.find_element(By.XPATH, '/html/body/div[1]/div/'
                                                   'div[1]/div[4]/div[4]/'
                                                   'div[1]/div/div/div[2]/'
                                                   'div[1]/div[7]/div/div/'
                                                   'div[2]/div[2]/a')
    choice_tariff.click()
    # Прогрузить страницу
    time.sleep(5)

    # Заполнить имя
    name = browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[4]/'
                                          'div/div[2]/div[1]/form/div/div[2]/'
                                          'div/div[2]/input')
    name.send_keys('Автотест')
    time.sleep(1)

    # Заполнить номер телефона
    phone = browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div[4]/'
                                           'div/div[2]/div[1]/form/div/div[3]/'
                                           'div/div[2]/input')
    phone.send_keys('1111111111')
    time.sleep(1)

    # Нажать на кнопку отправить заявку
    send_button = browser.find_element(By.XPATH, '/html/body/div[1]/div/'
                                                 'div[1]/div[4]/div/div[2]/'
                                                 'div[1]/form/div/div[6]/div')
    send_button.click()
    time.sleep(10)

    # Узнать статус код
    r = requests.get('https://piter-online.net/leningradskaya-oblast/orders/'
                     'home?tariff_id=102134021')
    print(r.status_code)

    if r.status_code == 201:
        print(f'Тест {i} пройден успешно')
    else:
        print(f'Тест {i} упал')

    # Прогружаем страничку на которой выбираем тариф
    link = 'https://piter-online.net/leningradskaya-oblast/' \
           'rates?house_id=4270758'
    browser = webdriver.Chrome()
    browser.get(link)
