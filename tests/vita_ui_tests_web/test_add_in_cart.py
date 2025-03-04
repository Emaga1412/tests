import allure


@allure.step("Открываем главную страницу сайта")
def open_website(page):
    """Ожидаемый результат: Страница загружается успешно и отображается главная страница."""
    page.goto('https://vitaexpress.ru/')
    allure.attach('Ожидаемый результат: Страница загружается успешно и отображается главная страница',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("На предложенном городе нажимаем 'выбрать'")
def confirm_city_selection(page):
    """Ожидаемый результат: Модальное окно выбора города должно быть видно, и город должен быть выбран."""
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[1]').wait_for(state='visible')
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[1]').click()
    allure.attach('Ожидаемый результат: Модальное окно выбора города должно быть видно, и город должен быть выбран.',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажимаем кнопку 'Поиск' и вводим 'Цетрин'")
def search_button_click_and_enter_product_name(page):
    """Ожидаемый результат: Поле поиска становится активным, и в нем появляется название товара 'Цетрин'."""
    page.locator(
        'xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/input').wait_for(state='visible')
    search_locator = page.locator(
        'xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/input')
    search_locator.click()
    search_locator.fill('Цетрин')
    allure.attach('Ожидаемый результат: Поле поиска становится активным, и в нем появляется название товара "Цетрин".',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажимаем на лупу в левой части поисковой строки")
def search_product(page):
    """Ожидаемый результат: После клика на иконку лупы должен начаться поиск товара 'Цетрин'."""
    page.locator(
        'xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/button[1]').wait_for(state='visible')
    page.locator('xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/button[1]').click()
    allure.attach('Ожидаемый результат: После клика на иконку лупы должен начаться поиск товара "Цетрин".',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажать 'В корзину'")
def add_in_cart(page):
    """Ожидаемый результат: Продукт 'Цетрин' должен быть добавлен в корзину, и кнопка должна измениться."""
    page.wait_for_url('https://vitaexpress.ru/search/?q=%D0%A6%D0%B5%D1%82%D1%80%D0%B8%D0%BD')
    page.locator('xpath=//*[@id="catalogRoot"]/div[1]/div/div[2]/div[2]/div[2]/button/div[1]').click()
    allure.attach('Ожидаемый результат: Продукт "Цетрин" должен быть добавлен в корзину, и кнопка должна измениться.',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Нажать на корзину")
def go_to_cart(page):
    """Ожидаемый результат: Иконка корзины становится активной, и происходит переход в корзину."""
    search_count_product = page.locator(
        'xpath=/html/body/div[1]/div[3]/div[5]/div[2]/div[3]/div[1]/div/div[2]/div[2]/div[2]/button/div[2]/span[2]')
    search_count_product.wait_for(state='visible')
    page.locator('xpath=/html/body/div[1]/header/div[2]/nav/div/div/div[2]/div[2]/div[2]/div/a/img').click()
    allure.attach('Ожидаемый результат: Иконка корзины становится активной, и происходит переход в корзину.',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step("Ожидаем, что при переходе в корзину отображается выбранный товар с количеством, которое мы выбрали")
def visible_cart_with_added_product(page):
    """Ожидаемый результат: В корзине должен быть виден товар 'Цетрин' с правильным количеством (1)."""
    finish_element = page.locator(
        'xpath=/html/body/div[1]/form/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/h2')
    finish_element.wait_for(state='visible')
    assert finish_element.is_visible()
    allure.attach('Ожидаемый результат: В корзине должен быть виден товар "Цетрин" с правильным количеством (1).',
                  name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.title("Тест добавления товара в корзину на сайте VitaExpress")
@allure.description("Ожидаемый результат: В корзине отображается товар в количестве, которое мы добавили")
def test_add_in_cart(page):
        open_website(page)
        confirm_city_selection(page)
        search_button_click_and_enter_product_name(page)
        search_product(page)
        add_in_cart(page)
        go_to_cart(page)
        visible_cart_with_added_product(page)