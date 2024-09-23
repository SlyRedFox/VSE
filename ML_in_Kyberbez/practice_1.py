from bs4 import BeautifulSoup
import requests
from datetime import datetime
import random
import time



url_openphish = 'https://openphish.com/'


page = requests.get(url_openphish, stream=True, allow_redirects=True, timeout=10, verify=False)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find('table', class_ = 'pure-table pure-table-striped')
internal_table = table.find('tbody')
internal_table

alive_sites = []
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
    print(row)
    if row:
        url = row[0]
        target = row[1]
        time = date + " " + row[2]

        datetime_object = datetime.strptime(time,"%m/%d/%Y %H:%M:%S")
        if ((now - datetime_object).total_seconds()/60-180)<16:
            # print(row)
            alive_sites.append(row)

df = pd.DataFrame(alive_sites)
df.to_csv("test2.csv")