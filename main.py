from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = Service("/Applications/chromedriver")
driver = webdriver.Chrome(service=chrome_driver)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def check_availability():
    global available_items
    grayed_items = driver.find_elements(By.CLASS_NAME, "grayed")
    grayed_items_list = [x.get_attribute("id") for x in grayed_items[:-1]]
    available_items = [x for x in items_list if x not in grayed_items_list]
    return available_items


def upgrade_items(store_items):
    available_prices = []

    for x in store_items:
        item = driver.find_element(By.ID, x)
        price = int(item.text.split("\n")[0].split(" - ")[1].replace(",", ""))
        available_prices.append(price)

    if len(available_prices) > 0:
        max_price_index = available_prices.index(max(available_prices))
        buy_item = driver.find_element(By.ID, store_items[max_price_index])
        buy_item.click()
        # print(buy_item.text.split("\n")[0])


def check_speed():
    speed = driver.find_element(By.ID, "cps").text
    print(speed)


five_sec = time.time() + 5
five_min = time.time() + 60*5

all_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_list = [x.get_attribute("id") for x in all_items[:-1]]
# print(all_items_list)

available_items = []
while True:
    cookie.click()

    if time.time() > five_sec:
        # grayed_items = driver.find_elements(By.CLASS_NAME, "grayed")
        # grayed_items_list = [x.get_attribute("id") for x in grayed_items[:-1]]
        # available_items = [x for x in items_list if x not in grayed_items_list]
        # # print(available_items)
        #
        # check_availability()
        #
        # available_prices = []
        # for x in available_items:
        #     item = driver.find_element(By.ID, x)
        #     price = int(item.text.split("\n")[0].split(" - ")[1].replace(",", ""))
        #     available_prices.append(price)
        # # print(available_prices)
        #
        # if len(available_prices) > 0:
        #     max_price_index = available_prices.index(max(available_prices))
        #     buy_item = driver.find_element(By.ID, available_items[max_price_index])
        #     buy_item.click()
        #     # print(buy_item.text.split("\n")[0].split(" - ")[0])

        upgrade_items(check_availability())

        five_sec = time.time() + 5

    if time.time() > five_min:
        # speed = driver.find_element(By.ID, "cps").text
        # print(speed)
        check_speed()
        break



# while True:
#     cookie.click()
#
#     if time.time() > five_sec:
#         # print("checking upgrade")
#
#         store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         price_list = [int(x.text.split(" - ")[1].replace(",", "")) for x in store_items[:-1]]
#
#         upgrade_store = {price_list[x]: items_list[x] for x in range(len(items_list))}
#         # print(upgrade_store)
#
#         money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
#         # print(money)
#
#         upgrade_options = {x: y for (x, y) in upgrade_store.items() if 2000 >= x}
#         # print(upgrade_options)
#
#         upgrade_cost = max(upgrade_options)
#         upgrade_item = upgrade_options[upgrade_cost]
#         # print(upgrade_cost, upgrade_item)
#         # print(f"{upgrade_item.strip('buy')} upgraded")
#
#         driver.find_element(By.ID, upgrade_item).click()
#
#         five_sec = time.time() + 5
#
#     if time.time() > five_min:
#         speed = driver.find_element(By.ID, "cps").text
#         print(speed)
#         break

