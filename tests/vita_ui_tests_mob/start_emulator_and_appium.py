import subprocess
import time

# Запуск эмулятора через Git Bash
print("Запуск эмулятора...")
subprocess.Popen(["bash", "-c", "emulator -avd Pixel_4_API_33"])

# Ожидание, чтобы эмулятор успел загрузиться
time.sleep(30)  # Можно увеличить, если эмулятор долго запускается

# Запуск Appium через Git Bash
print("Запуск Appium ...")
appium_process = subprocess.Popen(["bash", "-c", "appium --address 127.0.0.1"])

# Ожидание, чтобы Appium успел запуститься
time.sleep(20)  # Можно увеличить, если Appium долго стартует

# Запуск автотестов
print("Запуск автотестов...")
subprocess.run(["pytest", "C:/Users/poego/PycharmProjects/PythonProjectUITests2025feb/tests/vita_ui_tests_mob"], check=True)

# Остановка Appium после завершения тестов
appium_process.terminate()
print("Appium остановлен.")


