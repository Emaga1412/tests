import time
import allure



# Шаг 1: Открываем главную страницу сайта
@allure.step("Открываем главную страницу сайта")
def open_website(page):
    """Ожидаемый результат: Отображается главный экран сайта"""
    page.goto('https://vitaexpress.ru/')
    allure.attach('Отображается главный экран сайта', name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


# Шаг 2: Нажимаем на кнопку смены города
@allure.step("Нажимаем на кнопку смены города")
def click_city_change_button(page):
    """Ожидаемый результат: Отображается форма поиска города"""
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[2]').wait_for(state="visible")
    page.locator('//*[@id="modal-help-city"]/div/div/div/div/div/div/div[3]/a[2]').click()
    allure.attach('Ожидаемый результат: Отображается форма поиска города', name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


# Шаг 3: Заполняем поле для ввода города
@allure.step("Заполняем поле для ввода города. Ввести 'Сочи'")
def fill_city_field(page):
    """Ожидаемый результат: В результатах поиска отображается город 'Сочи'"""
    page.locator('//*[@id="changeCityModalWrap"]/div/div/div/div/div/div[2]/div/form/input').wait_for(state="visible")
    page.locator('//*[@id="changeCityModalWrap"]/div/div/div/div/div/div[2]/div/form/input').fill('Сочи')
    allure.attach('Ожидаемый результат: В результатах поиска отображается город "Сочи"', name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


# Шаг 4: Выбираем город из предложенного списка
@allure.step("Выбираем город из выпадающего списка")
def select_city_from_suggestions(page):
    page.locator('//*[@id="changeCityModalWrap"]/div/div/div/div/div/div[2]/div/form/div[2]/div/div/div[1]').wait_for(
        state="visible")
    page.locator('//*[@id="changeCityModalWrap"]/div/div/div/div/div/div[2]/div/form/div[2]/div/div/div[1]').click()
    allure.attach("Ожидаемый результат: Окно с выбором города закрывается, отображается главный экран")


# Шаг 5: Ожидаем, что город отобразится в шапке сайта

@allure.step("Проверяем выбранный город в шапке сайта")
def wait_for_city_in_header(page):
    """Ожидаемый результат: Город Сочи отображается в шапке сайта"""
    city_locator = page.locator('xpath=//*[@id="selectCity"]/span')
    city_locator.wait_for(state='visible')
    time.sleep(2)
    city_element = page.locator('xpath=//*[@id="selectCity"]/span')
    selected_city = city_element.text_content().strip()

    assert selected_city == 'Сочи', f"Ожидался город 'Сочи', но найден '{selected_city}'"
    allure.attach("Ожидаемый результат: Город Сочи отображается в шапке сайта", name='Ожидаемый результат',
                  attachment_type=allure.attachment_type.TEXT)


# Основной тест
@allure.title("Смена города пользователя  на главном экране")
@allure.description("Ожидаемый результат: Выбранный город отображается в шапке сайта")
def test_select_city_and_search(page):
        open_website(page)
        click_city_change_button(page)
        fill_city_field(page)
        select_city_from_suggestions(page)
        wait_for_city_in_header(page)