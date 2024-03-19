import pyzipper
import requests
from store import pw
from store import headers
from pprint import pprint


# Этап 1. Распаковка архива.
# Используя Python распакуйте предоставленный архив и извлеките файлы
with pyzipper.AESZipFile('netology.zip', 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as ex_zip:
    try:
        ex_zip.extractall(pwd=pw)
    except Exception as err:
        print(err)


# Этап 2. Анализ файлов через VirusTotal API.
# Отправьте файлы на анализ, используя ваш персональный API ключ VirusTotal.
api_url: str = 'https://www.virustotal.com/api/v3/files'
with open('invoice-42369643.html', 'rb') as file:
    files = {'file': ('invoice-42369643.html', file)}
    response = requests.post(api_url, headers=headers, files=files)

base_link = response.json()
# print(response.text)
url_for_analyses: str = base_link['data']['links']['self']
# url_for_analyses: str = 'https://www.virustotal.com/api/v3/analyses/NjEyYjU3ZTJhZmU3MDY1ZWJlOTIxMzM3MTcwZGY3ZDQ6MTcxMDg3NTAxNw=='


# Этап 3. Обработка результатов сканирования.
# Проанализируйте ответы от VirusTotal, собирая данные о детектировании угроз антивирусами.
response = requests.get(url_for_analyses, headers=headers)
# print(response.text)
all_statistic = response.json()


# Этап 4. Подготовка отчета. Составьте отчет со статистикой результатов сканирования.
# В отчет включить код скрипта и его вывода в формате скриншота (.jpg, .png)
# Укажите список антивирусов, которые обнаружили угрозы в формате: Detected, ALYac, Kaspersky
# Сравните результаты с заданным списком антивирусов и песочниц.
# Укажите, какие из указанных антивирусов (Fortinet, McAfee, Yandex, Sophos) детектировали угрозу, а какие нет.
# TODO: прописать проверку статуса, что ниже???
print(f'Status: {all_statistic['data']['attributes']['status']}')
print(f'\nBase statistic: {all_statistic['data']['attributes']['stats']}')

print('\nAntiVirus statistic.')
detected: list = list()
not_detected: list = list()
all_antivirus_stat: dict = all_statistic['data']['attributes']['results']

for antvir, stats in all_antivirus_stat.items():
    # print(f'\nAntiVirus: {antvir}')
    # print(stats['result'])
    if stats['result'] is None:
        not_detected.append(antvir)
    else:
        detected.append(antvir)

pprint(f'Detected {len(detected)}: {detected}\n')
pprint(f'Not detected {len(not_detected)}: {not_detected}')


# Дополнительные задачи.
# Если доступен отчет VirusTotal Sandbox о поведении вредоноса, проанализируйте его и включите в свой отчет ключевые
# моменты поведения вредоноса.
# Выведите список доменов и IP-адресов, с которыми вредонос общается (для блокировки), и описание поведения (Behavior)
# от VirusTotal Sandbox, если таковое доступно.

# получаем данные из песочницы
sha256: str = all_statistic['meta']['file_info']['sha256']
url_sandbox = f'https://www.virustotal.com/api/v3/file_behaviours/{sha256}_VirusTotal Jujubox'
response_sandbox = requests.get(url_sandbox, headers=headers)
# print(response_sandbox.text)

md5_id: str = all_statistic['meta']['file_info']['md5']
behaviours_url: str = f'https://www.virustotal.com/api/v3/files/{md5_id}/behaviours'
behaviour_summary_url: str = f'https://www.virustotal.com/api/v3/files/{md5_id}/behaviour_summary'

# выводим данные behaviour, список доменов и IP-адресов
response_file_behaviour = requests.get(behaviours_url, headers=headers)
response_behaviour_summary = requests.get(behaviour_summary_url, headers=headers)
# много данных, можно вывести в файлы при необходимости
# print(response_file_behaviour.text)
# print(response_behaviour_summary.text)

print('\nСписок доменов и IP-адресов.')
behaviour_summary_results = response_behaviour_summary.json()
domens_and_ip = behaviour_summary_results['data']['dns_lookups']
for elem in domens_and_ip:
    print(elem)
