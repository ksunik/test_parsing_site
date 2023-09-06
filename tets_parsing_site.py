import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def get_currency_rate():
    URL_TEMPLATE = "https://66.ru/bank/currency/"
    r = requests.get(URL_TEMPLATE)
    print(r.status_code)
    # print(r.text)
    soup = bs(r.text, "html.parser")
    # print(soup.prettify())
    best_current_course = soup.find("span", class_="currency-rate-span").get_text()
    name_bank = soup.find("a", class_="best-bank-name").get_text()
    for link in soup.find_all('a', rel="177", class_="best-bank-name"):
        print(link.get('href'))
    # name_bank = str(name_bank)
    return float(best_current_course.replace(",", ".")), str(name_bank)
# Основной код программы
if __name__ == "__main__":
    # Получаем текущий курс валюты
    current_rate, name_bank = get_currency_rate()
    print(f"Текущий лучший курс продажи валюты: {current_rate}")
 
    
    # Запускаем бесконечный цикл
    while True:
        # Ждем 5 секунд
        time.sleep(30)
        
        # Получаем новый курс валюты
        new_rate, name_bank  = get_currency_rate()
        
        # Если произошло сильное изменение курса валюты, отправляем уведомление
        if abs(new_rate - current_rate) > 0:
            print(f"Сильное изменение курса валюты! Старое значение: {current_rate}, новое значение: {new_rate}")
            current_rate = new_rate

