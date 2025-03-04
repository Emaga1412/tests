import allure
import time



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
    allure.attach(
        'Ожидаемый результат: Модальное окно выбора города должно быть видно, и город должен быть выбран.',
        name='Ожидаемый результат', attachment_type=allure.attachment_type.TEXT)


@allure.step('Ожидаемый результат: В поисковой строке отображается "Кагоцел"')
def input_to_search(page):
    """Ожидаемый результат: Отображается результат поиска с товарами"""
    page.locator('xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/input').wait_for(state='visible')
    page.locator('xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/input').fill('Кагоцел')
    allure.attach(
        'Ожидаемый результат: В поисковой строке отображается "Кагоцел".', name="Ожидаемый результат", attachment_type=
        allure.attachment_type.TEXT
    )


@allure.step('Нажать на лупу')
def enter_of_search(page):
    """Ожидаемый результат: Отображается результат поиска с товарами"""
    page.locator('xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/button[1]').wait_for(state='visible')
    page.locator('xpath=/html/body/div[1]/header/div[4]/div[1]/div[2]/div/form/div/button[1]').click()
    allure.attach(
        'Ожидаемый результат: Отображается результат поиска с товарами',
        name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)


@allure.step('Проверить, что у товара есть активное вещество "Кагоцел" и кликнуть по нему')
def visible_active_substance(page):
    """Ожидаемый результат: У товара отображается активное вещество"""
    page.locator('xpath=/html/body/div[1]/div[3]/div[5]/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[3]').wait_for(
        state='visible')
    page.locator('xpath=/html/body/div[1]/div[3]/div[5]/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[3]').click()
    time.sleep(10)
    allure.attach('Ожидаемый результат: У товара отображается активное вещество', name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


@allure.title('Поиск по активному веществу')
@allure.description("Ожидаем увидеть список товаров по активному веществу")
def assert_goods_with_active_substance_is_visible(page):
    element = page.locator('h1[data-qa="515052643"]')
    element.wait_for(state='visible')
    actual_text = element.text_content()
    expected_text = 'Препараты с действующим веществом Кагоцел'

    assert actual_text == expected_text
    time.sleep(10)
    allure.attach(f"Ожидаемый текст: '{expected_text}', Фактический текст: '{actual_text}'",
                  name="Сравнение текста", attachment_type=allure.attachment_type.TEXT)


def test_search_by_active_substance(page):
        open_website(page)
        confirm_city_selection(page)
        input_to_search(page)
        enter_of_search(page)
        visible_active_substance(page)
        assert_goods_with_active_substance_is_visible(page)