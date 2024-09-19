from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def initialize_driver():
    options = Options()
    options.add_argument("--headless")  # Запуск в фоновом режиме
    #service = Service('C:\Users\Иван\Downloads\Исходники программ\chrome-win64')  # Укажите путь к chromedriver
    browser = webdriver.Chrome()
    #driver = webdriver.Chrome(service=service, options=options)
    #return driver
    return browser
browser = webdriver.Chrome()

print("Здравствуйте!")

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(3)
print("Открыта главная страница Википедии.")

# Запрашиваем у пользователя ввод текста
user_input = input("Что будем искать?...")

# Находим элемент search_box.
search_box = browser.find_element(By.ID, "searchInput") # searchInput = ID

# Вводим текст в элемент search_box
search_box.send_keys(user_input)

# (Необязательно) Отправляем форму, если это необходимо
search_box.send_keys(Keys.RETURN)
time.sleep(5)


def search_wikipedia(driver, query):
    driver.get("https://ru.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query + Keys.RETURN)


def get_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    return [para.text for para in paragraphs]


def get_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    return [link.get_attribute("href") for link in links]


def main():
    driver = initialize_driver()
    try:
        while True:
            query = input("Введите запрос для поиска в Википедии (или 'в' для завершения): ")
            if query.lower() == 'в':
                break

            search_wikipedia(driver, query)
            time.sleep(2)  # Ждем загрузки страницы

            paragraphs = get_paragraphs(driver)
            links = get_links(driver)

            for i, para in enumerate(paragraphs):
                print(f"{i + 1}: {para}\n")
                if i >= 2:  # Показать только первые три параграфа
                    break

            while True:
                action = input(
                    "Выберите действие: 1 - Листать параграфы, 2 - Перейти на связанную страницу, 3 - Выйти: ")
                if action == '1':
                    for i, para in enumerate(paragraphs):
                        print(f"{i + 1}: {para}\n")
                        if i >= 2:
                            break
                elif action == '2':
                    if links:
                        print("Связанные страницы:")
                        for idx, link in enumerate(links[:5]):  # Показать первые 5 связанных ссылок
                            print(f"{idx + 1}: {link}")
                        choice = int(input("Выберите номер страницы для перехода: ")) - 1
                        if 0 <= choice < len(links):
                            driver.get(links[choice])
                            time.sleep(2)  # Ждем загрузки страницы
                            paragraphs = get_paragraphs(driver)
                            links = get_links(driver)
                            break
                        else:
                            print("Некорректный выбор.")
                    else:
                        print("Нет связанных страниц.")
                elif action == '3':
                    break
                else:
                    print("Некорректный выбор.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
