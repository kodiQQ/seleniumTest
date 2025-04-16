from django.http import JsonResponse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
# Wczytanie zmiennych z pliku .env
load_dotenv()
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ✅ bez GUI
    chrome_options.add_argument("--no-sandbox")  # ✅ dla środowisk chmurowych
    chrome_options.add_argument("--disable-dev-shm-usage")  # ✅ dla ograniczonych zasobów
    chrome_options.add_argument("--disable-gpu")  # opcjonalnie

    # Jeśli używasz niestandardowej ścieżki do Chrome (czasem wymagane na Render):
    # chrome_options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def loginToSteam(driver, login, password):
    print("loginToSteam")
    driver.get("https://steamcommunity.com/login/home/?goto=")
    sleep(5)
    try:
        accept_cookies = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div[1]/span")
        accept_cookies.click()
    except:
        1
    login1 = driver.find_element("xpath",
                                 '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
    password1 = driver.find_element("xpath",
                                    '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
    sleep(1)
    login1.send_keys(login)
    password1.send_keys(password)
    password1.send_keys(Keys.ENTER)
    sleep(7)

def runSelenium(request):
    driver = get_driver()
    loginToSteam(driver,os.getenv("LOGIN"),os.getenv("PASSWORD"))
    cookies=driver.get_cookies()
    driver.quit()
    return JsonResponse({"cookies": cookies})
