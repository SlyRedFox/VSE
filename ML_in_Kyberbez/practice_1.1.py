from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import random
import time
import pandas as pd

url_openphish = 'https://openphish.com/'

alive_sites = []


def update_data_from_openfish():
    page = requests.get(url_openphish, stream=True, allow_redirects=True, timeout=10, verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find('table', class_='pure-table pure-table-striped')
    internal_table = table.find('tbody')
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y %H:%M:%S")
    date = current_time.split(" ")[0]

    for tr in internal_table.find_all('tr'):
        # print(tr)
        url = ""
        target = ""
        time = ""
        row = []
        for td in tr.find_all('td'):
            # print(td.text.strip())
            row.append(td.text.strip())

        # print(row)
        if row:
            url = row[0]
            target = row[1]
            time = date + " " + row[2]

            datetime_object = datetime.strptime(time, "%m/%d/%Y %H:%M:%S")
            if ((now - datetime_object).total_seconds() / 60 - 180) < 16:
                # print(row)
                alive_sites.append(row)
            print(alive_sites)


start_time = datetime.now()

print("Script start ", start_time)

while True:
    print("Request ...")
    update_data_from_openfish()
    time.sleep(300)
    if datetime.now() > start_time + timedelta(hours=1):
        break

df = pd.DataFrame(alive_sites)
df.to_csv("test2.csv")

print("Script end", datetime.now())