from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен драйвер для Chrome
    driver.get("https://ru.wikipedia.org")

    while True:
        query = input("Введите запрос для поиска в Википедии: ")
        search_box = driver.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Ждем загрузки страницы
        try:
            # Проверяем, является ли это страницей результатов поиска
            if "Результаты поиска" in driver.title:
                print("Страница результатов поиска:")
                search_results = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text .searchresults li")

                for i, result in enumerate(search_results):
                    link = result.find_element(By.CSS_SELECTOR, "a")
                    link_text = link.text
                    link_href = link.get_attribute('href')
                    link_title = link.get_attribute('title')
                    print(f"{i + 1}. {link_text} (ссылка: {link_href}, title: {link_title})")

                continue

            page_title = driver.find_element(By.ID, "firstHeading").text
            print(f"\nСтатья: {page_title}")
            paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")

            # Показать все параграфы
            if paragraphs:
                for i, paragraph in enumerate(paragraphs):
                    print(f"{i + 1}. {paragraph.text}")
            else:
                print("Параграфы не найдены.")

        except Exception as e:
            print("Ошибка при загрузке статьи:", e)
            continue

        while True:
            action = input(
                "\nВыберите действие:\n1. Листать параграфы\n2. Перейти на связанную страницу\n3. Создать страницу\n4. Искать в других поисковых системах\n5. Выйти\nВведите номер: ")
            if action == '1':
                for i, paragraph in enumerate(paragraphs):
                    print(f"\n{i + 1}. {paragraph.text}")
                break
            elif action == '2':
                links = driver.find_elements(By.CSS_SELECTOR, "a[href^='/wiki/']")
                print("Связанные страницы:")
                for i, link in enumerate(links[:5]):  # Показать первые 5 связанных страниц
                    link_text = link.text
                    link_href = link.get_attribute('href')  # Извлечение href
                    link_title = link.get_attribute('title')  # Извлечение title
                    print(f"{i + 1}. {link_text} (ссылка: {link_href}, title: {link_title})")
                link_choice = int(input("\nВыберите номер страницы для перехода: ")) - 1
                if 0 <= link_choice < len(links):
                    driver.execute_script("arguments[0].scrollIntoView();", links[link_choice])
                    time.sleep(0.5)
                    links[link_choice].click()
                    time.sleep(2)  # Ждем загрузки страницы
                    break
            elif action == '3':
                title = input("Введите название страницы для создания: ")
                driver.get(f"https://ru.wikipedia.org/wiki/{title}")
                print(f"Создание страницы: {title} (проверьте, существует ли она уже).")
            elif action == '4':
                search_engine = input("Выберите поисковую систему (Google, Яндекс, Bing): ").lower()
                if search_engine == 'google':driver.get(f"https://www.google.com/search?q={query}")
                elif search_engine == 'яндекс':
                    driver.get(f"https://yandex.ru/search/?text={query}")
                elif search_engine == 'bing':
                    driver.get(f"https://www.bing.com/search?q={query}")
                else:
                    print("Неверный выбор. Попробуйте снова.")
                time.sleep(2)  # Ждем загрузки страницы
                break
            elif action == '5':
                print("Выход из программы.")
                driver.quit()
                return
            else:
                print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()