from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def menu():
    while True:  # Бесконечный цикл для повторного отображения меню
        print('\nЧто делаем дальше?')
        print('1. Листаем параграфы текущей страницы...')
        print('2. Перейти на внутреннюю статью...')
        print('3. Выйти из программы')

        m = input('Выберите опцию (1, 2 или 3): ')

        if m == '1':
            print("Листаем параграфы текущей страницы...")
            # Код для листания параграфов
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            # Цикл для перебора параграфов
            for paragraph in paragraphs:
                print(paragraph.text)
                input()
                # Как остановить листание?

        elif m == '2':
            print("Перейдем на внутреннюю статью...")
            #код для перехода на внутреннюю статью
            # Поиск всех ссылок на странице
            links = browser.find_elements(By.TAG_NAME, 'a')

            # Переход по каждой ссылке
            for link in links:
                href = link.get_attribute('href')
                if href:  # Проверка, что ссылка не пустая
                    browser.get(href)
                    print(href)
                    time.sleep(2)  # Задержка для загрузки страницы
                    browser.back()  # Возврат на предыдущую страницу





        elif m == '3':
            print("Выход из программы...")
            break  # Выход из цикла и завершение программы
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

def get_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
    return [link.get_attribute("href") for link in links]

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

# Вызов процедуры меню
menu()


print("Работа завершена.")
print("До свидания.")
# Закрываем драйвер после выполнения
browser.quit()
