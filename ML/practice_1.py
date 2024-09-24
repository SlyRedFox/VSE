from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import csv


url = 'https://openphish.com/'

def fetch_incidents():
    """Ищем данные на странице."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найти таблицу на странице
    table = soup.find('table')

    # if not table:
    #     return []

    rows = table.find_all('tr')

    # список словарей данных
    incidents: list = []

    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) == 3:
            incident = {
                        'url': cols[0].text.strip(),
                        'brand': cols[1].text.strip(),
                        'time': cols[2].text.strip()
                        }
            incidents.append(incident)

    return incidents


def save_to_csv(incidents, filename='final.csv'):
    """Добавление данных в csv-файл."""

    # Открываем файл на чтение, проверка дубликатов
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        existing_incidents = {row['url']: row for row in reader}

    # Открываем файл на запись
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'brand', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Если файл пустой, пишем заголовки
        if not existing_incidents:
            writer.writeheader()

        # Добавляем новые записи
        new_count = 0
        for incident in incidents:
            if incident['url'] not in existing_incidents:
                writer.writerow(incident)
                new_count += 1

        print(f'Добавлено новых инцидентов: {new_count}')


# Основная функция
def main():
    now = datetime.now()
    current_time = now.strftime('%m-%d-%Y %H:%M:%S')
    print(f'Время начала сбора данных: {current_time}')

    # Служебные переменные
    run_time_sec: int = 3600
    interval_sec: int = 300
    end_time = time.time() + run_time_sec

    while time.time() < end_time:
        print('Проверка инцидентов.')
        incidents = fetch_incidents()
        if incidents:
            save_to_csv(incidents)
        else:
            print('Нет новых инцидентов.')

        print(f'Пауза на 5 минут.')
        time.sleep(interval_sec)

    final_time = now.strftime('%m-%d-%Y %H:%M:%S')
    print(f'Время окончания сбора данных: {final_time}')


if __name__ == '__main__':
    main()
