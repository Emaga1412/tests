import allure
from playwright.sync_api import sync_playwright

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


