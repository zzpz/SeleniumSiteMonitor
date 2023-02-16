from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from timeit import default_timer as timer
import os
import random

JSON_FILE = "WebsiteStates.json"
start = timer()


url_param = os.environ["ENV_URL"]
url = url_param
op = webdriver.ChromeOptions()
op.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")


def alert():
    print("\033[31m" + "GOGOGOGOGO" * 5 + "\033[0m")


imgs = []
for link in soup.find_all("span", {"class": "snize-thumbnail"}):
    if not (link.img["alt"] in imgs):
        print(link.img["alt"])
        imgs.append(link.img["alt"])
print("------")

n = 1
while True:
    time_between_checks = random.randint(3, 16) + random.random()

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for link in soup.find_all("span", {"class": "snize-thumbnail"}):
        if not (link.img["alt"] in imgs):
            alert()
            print("NOT FOUND:" + link.img["alt"])

    end = timer()
    if n % 10 == 0:
        print("Try: " + str(n) + " Time: " + str((end - start) / 60) + " minutes")
    n = n + 1
