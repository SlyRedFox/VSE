from store import v_key
import requests
import vulners


vulners_api = vulners.VulnersApi(api_key=v_key)
# search_result = vulners_api.find_all("type:cve AND enchantments.exploitation.wildExploited:*")
# print('Result')
# print(search_result)



# Get vulnerabilities/exploits by software name and version
results = vulners_api.get_software_vulnerabilities("ivanti connect secure", "22.1")
exploit_list = results.get('exploit')
vulnerabilities_list = [results.get(key) for key in results if key in ['exploit']]



# Search public available exploits
wordpress_exploits = vulners_api.find_exploit_all("cisco ios xe")
cve_exploits = vulners_api.find_exploit_all("CVE-2023-20198", limit=5)
search_exploits = vulners_api.find_all("bulletinFamily:exploit AND cisco ios xe", limit=5)



# Audit installed KB's and software
kb = ['KB4052623', 'KB5019959', 'KB5017888', 'KB890830', 'KB2267602', 'KB4023057']
software = [{'software': '7-Zip 19.00 (x64)', 'version': '19.00'},
            {'software': 'Git', 'version': '2.33.0.2'},
            {'software': 'Notepad++ (64-bit x64)', 'version': '8.4.6'},
            {'software': 'Microsoft 365 - en-us', 'version': '16.0.15726.20202'},
            {'software': 'Microsoft 365 - ru-ru', 'version': '16.0.15726.20202'},
            {'software': 'Microsoft OneDrive', 'version': '22.227.1030.0001'},
            {'software': 'Total Commander 64-bit (Remove or Repair)', 'version': '10.00'},
            {'software': 'Microsoft .NET AppHost Pack - 6.0.0 (x64_x86)', 'version': '48.3.31210'},
            {'software': 'Microsoft .NET Host FX Resolver - 6.0.0 (x64)', 'version': '48.3.31210'},
            {'software': 'VMware Player', 'version': '16.2.4'},
            {'software': 'Foxit PDF Reader', 'version': '12.0.1.12430'}]
os_name = 'windows'
os_version = '10.0.19045'
report = vulners_api.winaudit(os=os_name, os_version=os_version, kb_list=kb, software=software)
print('Result software:')
print(report)


# Vulnerability summary report
# report = vulners_api.vulnssummary_report()
