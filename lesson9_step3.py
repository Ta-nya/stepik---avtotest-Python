from selenium import webdriver

'''
Поиск товара по ключивому слову "Python"

1. Открываем сайт магазина http://selenium1py.pythonanywhere.com/ru/
2. В окно "Найти" вводим ключевое слово "Python"
3. Нажимаем на кнопку "Найти"

Ожидаемый результат: В списке отображаются товары в названии которых фигурируем введенное на шаге 2 ключевое слово "Python".
'''
link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    search = browser.find_element_by_id("id_q")
    search.send_keys("Python")
    button = browser.find_element_by_css_selector("input.btn")
    button.click()
    result = browser.find_element_by_partial_link_text('Python')
    assert "Python" in result.text

finally:

    browser.quit()

'''
Вход зарегистрированного пользователя
Предварительные условия: email используемый для тестирования имеет зарегистрированную учетную запись
1. Открываем старницу "Войти или зарегистрироватся" http://selenium1py.pythonanywhere.com/ru/accounts/login/
2. Заполняем поле "Адрес электронной почты", вводим логин зарегистрированной учетной записи test@gmail.com
3. Заполняем поле "Пароль", вводим пароль зарегистрированной учетной записи R0ZPg2A6c
4. Нажимаем на кнопку "Войти"

Ожидаемый результат: Пользователь авторизован, на странице отопражается приветствие "Рады видеть вас снова".
'''
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    username = browser.find_element_by_id("id_login-username")
    username.send_keys("test1@gmail.com")
    password = browser.find_element_by_id("id_login-password")
    password.send_keys("R0ZPg2A6c")
    button = browser.find_element_by_name("login_submit")
    button.click()
    message = browser.find_element_by_class_name('alertinner')

    assert "Рады видеть вас снова" in message.text

finally:

    browser.quit()
