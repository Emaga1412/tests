import subprocess

print("Запуск тестов...")
subprocess.run(["cmd", "/c", "pytest", "--alluredir=allure-results"])

print("Генерация Allure отчета...")
subprocess.run(["cmd", "/c", "allure generate allure-results -o allure-report --clean"])

print("Открытие Allure отчета...")
subprocess.run(["cmd", "/c", "allure open allure-report"])

