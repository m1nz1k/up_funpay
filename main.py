from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import math
import time


# Функция, выполняющая основную работу.
def up_funpay(url, login, password):
    # options
    chrome_options = webdriver.ChromeOptions()
    # Юзер-Агент
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
    # Запуск в фоновом режиме. Пока не включаем.
    # chrome_options.add_argument('--headless')

    # Передаем параметры в driver
    driver = webdriver.Chrome(options=chrome_options)
    # Открываем на весь экран
    driver.maximize_window()
    # Переходим по ссылке
    driver.get(url)
    # Авторизация
    try:
        login_input = driver.find_element(By.NAME, "login")
        password_input = driver.find_element(By.NAME, "password")

        login_input.send_keys(f'{login}')
        password_input.send_keys(f'{password}')
    except Exception:
        print('Ошибка в авторизации. Пройдите сами.')
    print("Для продолжения нажмите Shift+H")
    # Жмем сочетание клавиш Shift+h только после того, как авторизируемся на всех аккаунтах.
    while True:
        if keyboard.is_pressed('shift+h'):
            print("Вы нажали Shift+H! Продолжаем выполнение кода.")
            break
        time.sleep(0.1)
    time.sleep(2)
    while True:
        driver.get('https://funpay.com/users/3137802/')
        time.sleep(5)
        try:
            # Найдите все элементы с классом "offer-list-title"
            offer_list_titles = driver.find_elements(By.CLASS_NAME, "offer-list-title")

            # Создайте пустой список для хранения ссылок
            links = []
        except Exception:
            print('Ошибка в поиске элементов для хранения ссылок.')
        try:
            # Проход по каждому элементу "offer-list-title" и извлечение ссылки из элемента "a"
            for offer_title in offer_list_titles:
                link_element = offer_title.find_element(By.TAG_NAME, "a")
                link = link_element.get_attribute("href")
                links.append(link)
        except Exception:
            print('Ошибка в добавлении сылок.')
        try:
            for el in links:
                driver.get(f"{el}trade")
                time.sleep(5)
                # Находим элемент и жмем.
                raise_button = driver.find_element(By.CLASS_NAME, "js-lot-raise")
                raise_button.click()
                time.sleep(1)
        except Exception as ex:
            print(f'Ошибка при нажатии на кнопку: {ex}')
        time.sleep(1800)



# Функция для парсинга данных из файла
def parse_config_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split('|') for line in lines]

def main():
    # Парсим данные из файла
    config_data = parse_config_file('config.txt')
    up_funpay(config_data[0][0], config_data[0][1], config_data[0][2])


# Точка входа.
if __name__ == '__main__':
    main()

