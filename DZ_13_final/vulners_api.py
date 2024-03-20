from store import v_key
from store import progs_for_analysis
import vulners

print('Begin...')
vulners_api = vulners.VulnersApi(api_key=v_key)

# Get vulnerabilities/exploits by software name and version
# https://vulners.com/docs/api_reference/search_strategies/#get-vulnerabilitiesexploits-by-software-name-and-version
# получаем данные по файлам из подготовленного списка
no_vulnerabilities: list = list()
yes_vulnerabilities: list = list()

for element in range(len(progs_for_analysis)):
    results = vulners_api.get_software_vulnerabilities(progs_for_analysis[element]['Program'], progs_for_analysis[element]['Version'])
    exploit_list = results.get('exploit')
    if exploit_list is None:
        no_vulnerabilities.append(progs_for_analysis[element]['Program'])
    else:
        yes_vulnerabilities.append(progs_for_analysis[element]['Program'])

        cve_all_info: list = list()
        for elem in exploit_list:
            cve_all_info.append(elem.get('cvelist'))

        cve_raw: list = list()
        for elem in range(len(cve_all_info)):
            cve_raw.append(cve_all_info[elem][0])

        href_raw: list = list()
        for elem in exploit_list:
            href_raw.append(elem.get('href'))

        description_raw: list = list()
        for elem in exploit_list:
            description_raw.append(elem.get('description'))

        with open(f'{progs_for_analysis[element]['Program']}.txt', 'w', encoding='utf-8') as file:
            for elem in range(len(cve_raw)):
                file.write(f'Номер: {elem}\n')
                file.write(f'Уязвимость: {cve_raw[elem]}\n')
                file.write(f'Ссылка на описание: {href_raw[elem]}\n')
                file.write(f'Детальное описание: {description_raw[elem]}\n')
                file.write('\n\n')


print('\nНе обнаружены уязвимости в следующем ПО:')
print(no_vulnerabilities)
print('\nЕсть уязвимости в ПО:')
print(yes_vulnerabilities)
print('\nДетальное описание уязвимостей сохранено в файлах (расширение txt) с именами ПО в папке со скриптом!')


# TODO: some addons
# # Search public available exploits
# # https://vulners.com/docs/api_reference/search_strategies/#search-public-available-exploits
# wordpress_exploits = vulners_api.find_exploit_all("cisco ios xe")
# cve_exploits = vulners_api.find_exploit_all("CVE-2023-20198", limit=5)
# search_exploits = vulners_api.find_all("bulletinFamily:exploit AND cisco ios xe", limit=5)


# Vulnerability summary report
# https://vulners.com/docs/api_reference/api_methods/#vulnerability-summary-report
# report = vulners_api.vulnssummary_report()
