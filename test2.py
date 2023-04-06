
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# Инициализируем веб-драйвер
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

# Переход на URL https://yandex.ru/images/
# driver.get("https://yandex.ru/images/")
# element = driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div/div/div[1]/a/div[1]""")
# element.click()
# time.sleep(2)
# /html/body/div[3]/div[2]/div/div[1]/div/div[2]
# driver.get("https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda")
# time.sleep(2)

# element = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/a/img""")
# # actions = ActionChains(driver)
# # actions.move_to_element(element)
# element.click()
# Проверка картинки 8) Проверить, что картинка открылась
# current_url = """https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda&pos=0&rpt=simage&img_url=http%3A%2F%2Ftraveltimes.ru%2Fwp-content%2Fuploads%2F2021%2F11%2F1920x1200-px-cliff-clouds-fall-field-Iceland-lake-landscape-lava-mountain-nature-river-turquoise-water-waterfall-1103888.jpg&lr=55"""
# driver.get(current_url)
# time.sleep(2)

# element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/img""")
# if element.get_attribute("src"):
#     print("yes")

# # вывод адреса на экран
# print(current_url)
# time.sleep(2)
# 9) Нажать кнопку вперед
# открытие галере с картинко
current_url = """https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda&pos=0&rpt=simage&img_url=http%3A%2F%2Ftraveltimes.ru%2Fwp-content%2Fuploads%2F2021%2F11%2F1920x1200-px-cliff-clouds-fall-field-Iceland-lake-landscape-lava-mountain-nature-river-turquoise-water-waterfall-1103888.jpg&lr=55"""
driver.get(current_url)
time.sleep(1)
# получение картинки
element = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/a/img""")
element.click()
time.sleep(2)
# получение первой картинки
element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
src1 = element.get_attribute("src")
print(src1)
# нажатие кнопки
element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[4]/i""")
element.click()
time.sleep(2)

# получение первой картинки

element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
src2 = element.get_attribute("src")
# 10) проверка что картинка сменилась

print(src2!=src1)
# 11) Нажать назад
element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/i""")
element.click()
time.sleep(1)
# 12) Проверить, что картинка осталась из шага 8
element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
src3 = element.get_attribute("src")
print(src1 == src3)


 






