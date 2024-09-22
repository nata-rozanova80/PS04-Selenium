# PS04-Selenium

1. **Не отображается текст параграфов**: Это может происходить из-за того, что при первом запросе вы получаете страницу результатов поиска, а не саму статью. Поэтому, когда вы пытаетесь вывести текст параграфов, он отсутствует. Вам нужно обрабатывать случай, когда на странице результатов поиска нет параграфов.

2. **Ошибка `ElementNotInteractableException`**: Эта ошибка возникает, когда вы пытаетесь кликнуть на элемент, который не может быть взаимодействован (например, он скрыт или недоступен). В вашем случае это может быть связано с тем, что вы пытаетесь кликнуть на ссылку, которая не является интерактивной. Вам нужно убедиться, что перед кликом элемент доступен для взаимодействия.


Строка `self.log(f'Name: {name}')` используется в контексте программирования на Python, и в частности, это может быть частью кода, связанного с фреймворком Scrapy. Давайте разберем ее по частям:

1. **`self`**: Это ссылка на текущий экземпляр класса. В контексте объекта, `self` позволяет вам получить доступ к его атрибутам и методам.

2. **`log`**: Это, вероятно, метод, определенный в классе, который позволяет записывать сообщения в журнал (лог). В Scrapy это может быть метод, который используется для логирования информации, предупреждений или ошибок, чтобы разработчики могли отслеживать поведение программы.

3. **`f'Name: {name}'`**: Это строка формата (f-string), которая была введена в Python 3.6. Она позволяет встраивать выражения внутри строк. В данном случае, переменная `name` будет подставлена в строку. Если, например, `name` равно `"John"`, то строка будет выглядеть как `"Name: John"`.

Таким образом, `self.log(f'Name: {name}')` записывает в журнал сообщение, которое содержит имя, переданное в переменной `name`. Это может быть полезно для отладки или мониторинга работы вашего кода, чтобы понять, какие значения передаются в ваш код или как работает логика программы.
