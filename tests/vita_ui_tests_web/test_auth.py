import allure


@allure.step("Открываем главную страницу сайта")
def open_website(page):
    """Ожидаемый результат: Страница загружается успешно и отображается главная страница"""
    page.goto('https://vitaexpress.ru/')
    allure.attach('Ожидаемый результат: Страница загружается успешно и отображается главная страница',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("На предложенном городе нажимаем 'выбрать'")
def confirm_city_selection(page):
    """Открыт главный экран, выбран предложенный город"""
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[1]').wait_for(state='visible')
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[1]').click()
    allure.attach('Ожидаемый результат: Открыт главный экран, выбран предложенный город',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажимаем на 'Войти' в верхнем правом углу")
def click_auth_button(page):
    """Открывается форма авторизации"""
    page.locator('//*[@id="main-navbar"]/div[2]/div[2]/div[3]/div/span').wait_for(state='visible')
    page.locator('//*[@id="main-navbar"]/div[2]/div[2]/div[3]/div/span').click()
    allure.attach('Ожидаемый результат: Открывается форма авторизации',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Вводим номер телефона")
def enter_number(page):
    """Ожидаемый результат: В поле телефон отображается введенный номер"""
    page.locator('//*[@id="user-form"]/div[1]/input').wait_for(state='visible')
    page.locator('//*[@id="user-form"]/div[1]/input').fill('79333333344')
    allure.attach('Ожидаемый результат: В поле телефон отображается введенный номер', name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажимаем 'Отправить")
def send_button_click(page):
    """Ожидаемый результат: Отображается форма авторизации, шаг2 ввод кода авторизации"""
    page.locator('//*[@id="user-form"]/div[5]/button').wait_for(state='visible')
    page.locator('//*[@id="user-form"]/div[5]/button').click()
    allure.attach('Ожидаемый результат: Отображается форма авторизации, шаг2 ввод кода авторизации',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Ожидаем увидеть кнопку подтвердить для кода авторизации")
def confirm_button_visible(page):
    locator = page.locator('//*[@id="modal-enter-register"]/div/div/div/div/div/div[2]/div[2]/form/div[2]/input')
    locator.wait_for()
    assert locator.is_visible()
    # поправить тут, туповато все выглядит, надо чтоб ор был один


@allure.title('Авторизация пользователя. Получение кода авторизации')
@allure.description("Ожидаем увидеть кнопку подтвердить для кода авторизации")
def test_auth(page):
        open_website(page)
        confirm_city_selection(page)
        click_auth_button(page)
        enter_number(page)
        send_button_click(page)
        confirm_button_visible(page)

        browser.close()
