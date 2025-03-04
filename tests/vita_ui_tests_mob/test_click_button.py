from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import ClientConfig


def test_click_button():
    # Настройки для Appium
    appium_url = "http://127.0.0.1:4723/wd/hub"

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel_4_API_33"
    options.app_package = "com.platfomni.vita.dev"
    options.app_activity = "com.platfomni.vita.ui.splash.SplashActivity"
    options.auto_grant_permissions = True
    options.no_reset = True
    options.full_reset = False

    # Добавляем ClientConfig для предотвращения предупреждений
    client_config = ClientConfig()

    driver = None  # Инициализируем driver заранее

    try:
        print("Подключение к Appium...")
        driver = webdriver.Remote(
            command_executor=appium_url,
            options=options,
            client_config=client_config  # Используем client_config
        )
        print("Приложение успешно запущено.")

        # Пример взаимодействия
        driver.find_element("id", "cityChoose").click()
        assert True  # Успешный тест, если нет ошибок

    except Exception as e:
        print(f"Ошибка при запуске теста: {e}")
        assert False  # Провалить тест, если ошибка

    finally:
        if driver:
            driver.quit()