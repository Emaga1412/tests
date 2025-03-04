from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    version = browser.version  # Замените 'version()' на 'version' (без скобок)
    print(f"Chromium version: {version}")
    browser.close()


# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch()  # Для Chromium
#     # Или для других браузеров
#     # browser = p.firefox.launch()
#     # browser = p.webkit.launch()
#
#     page = browser.new_page()
#     page.goto("https://example.com")
#     print(page.title())
#     browser.close()