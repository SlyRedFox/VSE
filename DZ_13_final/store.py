
# В рабочих проектах пароли надо хранить в системных переменных, а не тут.
# Но это же учебный проект :-)

# ключ и данные для virus_total
a_key: str = '385ae740f1609779847752f5c800b85c22ae3474dba6bf1f391b9d5c45f29c29'
headers = {'x-apikey' : a_key}
pw = b'netology'

# ключ для vulners
v_key: str = '8JVG2TFKYO8D9EXMDMCBPJ1FO94GVMS30913UIBQIY1YPNDCD412NIRKRFWNNBOU'

# исходные данные для vulners-анализа
progs_for_analysis: list = [
                        {'Program': 'LibreOffice', 'Version': '6.0.7'},
                        {'Program': '7zip', 'Version': '18.05'},
                        {'Program': 'Adobe Reader', 'Version': '2018.011.20035'},
                        {'Program': 'nginx', 'Version': '1.14.0'},
                        {'Program': 'Apache HTTP Server', 'Version': '2.4.29'},
                        {'Program': 'DjVu Reader', 'Version': '2.0.0.27'},
                        {'Program': 'Wireshark', 'Version': '2.6.1'},
                        {'Program': 'Notepad++', 'Version': '7.5.6'},
                        {'Program': 'Google Chrome', 'Version': '68.0.3440.106'},
                        {'Program': 'Mozilla Firefox', 'Version': '61.0.1'}
]
