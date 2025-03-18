from store import get_user_info_from_registry
from store import get_network_info_from_interfaces
from store import get_os_info_from_registry
from store import get_hardware_info
from store import get_bios_info_from_registry
from store import get_installed_software


print('Выберете, какие данные необходимо отобразить')
print('1 - Информация о пользователях')
print('2 - Информация о сетевом стеке')
print('3 - Информация о операционной системе')
print('4 - Информация об оборудовании')
print('5 - Информация о BIOS')
print('6 - Информация об установленном программном обеспечении')

choice = input('Введите номер варианта: ')

if choice not in ['1', '2', '3', '4', '5', '6']:
    print('Неверный выбор, завершение работы программы!')
    exit()
else:
    # 1
    # WINDOWS. ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЯХ
    # HKEY_USERS\\SID\\SOFTWARE\\MICROSOFT\\WINDOWS\\CURRENTVERSION\\EXPLORER\\SHELL FOLDERS
    if choice == '1':
        user_info = get_user_info_from_registry()
        if user_info:
            print("\nИнформация о пользователе:")
            for key, value in user_info.items():
                print(f"{key}: {value}")
        else:
            print("Данные о пользователе не найдены.")

    # 2
    # WINDOWS. ИНФОРМАЦИЯ О СЕТЕВОМ СТЕКЕ
    # HKEY_LOCAL_MACHINE\\SYSTEM\\CONTROLSET\\SERVICES\\TCPIP\\PARAMETERS\\INTERFACES\\
    elif choice == '2':
        if __name__ == "__main__":
            network_info = get_network_info_from_interfaces()

            if network_info:
                print("\nИнформация о сетевых интерфейсах:")
                for interface in network_info:
                    print(f"Интерфейс: {interface['Интерфейс']}")
                    for key, value in interface.items():
                        if key != "Интерфейс":
                            print(f"  {key}: {value}")
                    print("-" * 40)
            else:
                print("Данные о сетевых интерфейсах не найдены.")

    # 3
    # WINDOWS. ИНФОРМАЦИЯ О СИСТЕМЕ
    # ·      HKEY_LOCAL_MACHINE\\SOFTWARE\\MICROSOFT\\WINDOWS NT\\CURRENTVERSION
    # ·      HKEY_LOCAL_MACHINE\\SYSTEM\\SELECT
    # ·      HKEY_LOCAL_MACHINE\\SYSTEM\\CONTROLSET\\CONTROL\\PRODUCTOPTIONS
    # ·      HKEY_LOCAL_MACHINE\\SYSTEM\\CONTROLSET\\CONTROL\\TIMEZONEINFORMATION
    # ·      HKEY_LOCAL_MACHINE\\SYSTEM\\CONTROLSET\\CONTROL\\COMPUTERNAME\\COMPUTERNAME
    elif choice == '3':
        os_info = get_os_info_from_registry()
        if os_info:
            print("\nИнформация об операционной системе:")
            for key, value in os_info.items():
                print(f"{key}: {value}")
        else:
            print("Данные об ОС не найдены.")

    # 4
    # WINDOWS. ИНФОРМАЦИЯ О ОБОРУДОВАНИИ
    elif choice == '4':
        if __name__ == "__main__":
            hardware_info = get_hardware_info()

            if hardware_info:
                print("\nИнформация об оборудовании:")
                for category, data in hardware_info.items():
                    print(f"{category}:")
                    if isinstance(data, dict):
                        for key, value in data.items():
                            print(f"  {key}: {value}")
                    elif isinstance(data, list):
                        for item in data:
                            for key, value in item.items():
                                print(f"  {key}: {value}")
                    else:
                        print(f"  {data}")
                    print("-" * 40)
            else:
                print("Данные об оборудовании не найдены.")

    # 5
    # WINDOWS. ИНФОРМАЦИЯ О BIOS
    # HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\SYSTEM\BIOS
    # HKEY_LOCAL_MACHINE\SYSTEM\CURRENTCONTROLSET\CONTROL\SYSTEMINFORMATION
    elif choice == '5':
        if __name__ == "__main__":
            bios_info = get_bios_info_from_registry()

            if bios_info:
                print("\nИнформация о BIOS:")
                for key, value in bios_info.items():
                    print(f"{key}: {value}")
            else:
                print("Данные о BIOS не найдены.")

    # 6
    # WINDOWS. УСТАНОВЛЕННОЕ ПО
    # HKEY_LOCAL_MACHINE\\SOFTWARE\\MICROSOFT\\WINDOWS\\CURRENTVERSION\\UNINSTALL
    # HKLM\SOFTWARE\WOW6432NODE\MICROSOFT\WINDOWS\CURRENTVERSION\UNINSTALL
    elif choice == '6':
        if __name__ == "__main__":
            software_list = get_installed_software()

            if software_list:
                print("\nУстановленное программное обеспечение:")
                for idx, app in enumerate(software_list, 1):
                    print(f"Приложение #{idx}:")
                    for key, value in app.items():
                        print(f"  {key}: {value}")
                    print("-" * 40)
            else:
                print("Данные об установленном ПО не найдены.")
