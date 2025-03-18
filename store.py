import winreg
import os
import platform
import subprocess
import wmi


def get_user_info_from_registry():
    """
    Извлекает информацию о пользователе напрямую из реестра.

    :return: Словарь с информацией о пользователе.
    """
    user_info = {}

    try:
        # Получаем SID текущего пользователя
        current_user_sid = os.environ.get("USERPROFILE").split("\\")[-1]
        user_info["SID пользователя"] = current_user_sid

        # Имя пользователя
        user_info["Имя пользователя"] = os.environ.get("USERNAME")

        # Пути к папкам пользователя
        user_info["Рабочий стол"] = os.path.join(os.environ["USERPROFILE"], "Desktop")
        user_info["Документы"] = os.path.join(os.environ["USERPROFILE"], "Documents")
        user_info["Файлы cookies"] = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Windows",
                                                  "INetCookies")
        user_info["История браузера"] = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge",
                                                     "User Data", "Default", "History")
        user_info["Временные файлы"] = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Temp")

        # Дополнительная информация из реестра
        # Пример: Путь к рабочему столу из реестра (если нужно)
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        user_info["Рабочий стол (реестр)"] = winreg.QueryValueEx(reg_key, "Desktop")[0]
        winreg.CloseKey(reg_key)

    except Exception as e:
        print(f"Ошибка при чтении реестра или получении данных: {e}")

    return user_info


def get_network_info_from_interfaces():
    """
    Извлекает информацию о сетевом стеке из ветки реестра Interfaces.

    :return: Список словарей с информацией о каждом сетевом интерфейсе.
    """
    network_info = []

    try:
        # Открываем ключ реестра для сетевых интерфейсов
        interfaces_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"
        )

        # Перебираем все GUID интерфейсов
        for i in range(winreg.QueryInfoKey(interfaces_key)[0]):
            interface_guid = winreg.EnumKey(interfaces_key, i)
            interface_key = winreg.OpenKey(interfaces_key, interface_guid)

            interface_info = {"Интерфейс": interface_guid}

            try:
                # Получаем IPv4 адрес
                try:
                    ip_address = winreg.QueryValueEx(interface_key, "DhcpIPAddress")[0]
                    interface_info["IPv4 адрес"] = ip_address
                except FileNotFoundError:
                    interface_info["IPv4 адрес"] = "Нет данных"

                # Получаем маску сети
                try:
                    subnet_mask = winreg.QueryValueEx(interface_key, "DhcpSubnetMask")[0]
                    interface_info["Маска сети"] = subnet_mask
                except FileNotFoundError:
                    interface_info["Маска сети"] = "Нет данных"

                # Получаем шлюз по умолчанию
                try:
                    default_gateway = winreg.QueryValueEx(interface_key, "DhcpDefaultGateway")[0]
                    interface_info["Шлюз по умолчанию"] = default_gateway
                except FileNotFoundError:
                    interface_info["Шлюз по умолчанию"] = "Нет данных"

                # Получаем информацию о DHCP
                try:
                    dhcp_enabled = winreg.QueryValueEx(interface_key, "EnableDHCP")[0]
                    interface_info["DHCP"] = "Включен" if dhcp_enabled == 1 else "Выключен"
                except FileNotFoundError:
                    interface_info["DHCP"] = "Нет данных"

                # Получаем адрес DHCP-сервера
                try:
                    dhcp_server = winreg.QueryValueEx(interface_key, "DhcpServer")[0]
                    interface_info["Адрес DHCP"] = dhcp_server
                except FileNotFoundError:
                    interface_info["Адрес DHCP"] = "Нет данных"

                # Получаем название DHCP
                try:
                    dhcp_name = winreg.QueryValueEx(interface_key, "DhcpDomain")[0]
                    interface_info["Название DHCP"] = dhcp_name
                except FileNotFoundError:
                    interface_info["Название DHCP"] = "Нет данных"

                # Добавляем информацию о интерфейсе в список
                network_info.append(interface_info)

            except Exception as e:
                print(f"Ошибка при обработке интерфейса {interface_guid}: {e}")
            finally:
                winreg.CloseKey(interface_key)

        winreg.CloseKey(interfaces_key)
    except Exception as e:
        print(f"Ошибка при чтении реестра: {e}")

    return network_info


def get_os_info_from_registry():
    """
    Извлекает информацию о операционной системе напрямую из реестра.

    :return: Словарь с информацией о ОС.
    """
    os_info = {}

    try:
        # Открываем ключ реестра
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
        )

        # Извлекаем значения
        os_info["Тип"] = winreg.QueryValueEx(reg_key, "ProductName")[0]
        os_info["Версия"] = winreg.QueryValueEx(reg_key, "CurrentVersion")[0]
        os_info["Идентификатор ОС"] = winreg.QueryValueEx(reg_key, "ProductId")[0]
        os_info["Зарегистрированный пользователь"] = winreg.QueryValueEx(reg_key, "RegisteredOwner")[0]
        os_info["Номер сборки ОС"] = winreg.QueryValueEx(reg_key, "CurrentBuildNumber")[0]
        os_info["Тип системы"] = "64-bit" if winreg.QueryValueEx(reg_key, "InstallationType")[
                                                 0] == "Client" else "32-bit"

        # Абсолютный путь установки
        os_info["Абсолютный путь установки"] = winreg.QueryValueEx(reg_key, "SystemRoot")[0]

        # Закрываем ключ
        winreg.CloseKey(reg_key)

        # Дополнительная информация из других разделов реестра
        # Часовой пояс
        timezone_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                      r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation")
        os_info["Часовой пояс"] = winreg.QueryValueEx(timezone_key, "TimeZoneKeyName")[0]
        winreg.CloseKey(timezone_key)

        # Название компьютера
        computer_name_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                           r"SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName")
        os_info["Название компьютера"] = winreg.QueryValueEx(computer_name_key, "ComputerName")[0]
        winreg.CloseKey(computer_name_key)

    except Exception as e:
        print(f"Ошибка при чтении реестра: {e}")

    return os_info


def get_hardware_info():
    """
    Извлекает информацию обо всём оборудовании компьютера.

    :return: Словарь с информацией об оборудовании.
    """
    hardware_info = {}

    # Получаем информацию о процессоре
    hardware_info["Процессор"] = get_cpu_info()

    # Получаем информацию о памяти
    hardware_info["Память"] = get_memory_info()

    # Получаем информацию о дисках
    hardware_info["Диски"] = get_disk_info()

    # Получаем информацию о сетевых адаптерах
    hardware_info["Сетевые адаптеры"] = get_network_info()

    # Получаем информацию о видеоадаптере
    hardware_info["Видеоадаптер"] = get_gpu_info()

    return hardware_info


def get_cpu_info():
    """
    Извлекает информацию о процессоре.

    :return: Словарь с информацией о процессоре.
    """
    cpu_info = {}

    try:
        # Используем реестр для получения данных о процессоре
        cpu_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
        )
        try:
            cpu_info["Имя"] = winreg.QueryValueEx(cpu_key, "ProcessorNameString")[0]
        except FileNotFoundError:
            cpu_info["Имя"] = "Нет данных"
        try:
            cpu_info["Архитектура"] = winreg.QueryValueEx(cpu_key, "Identifier")[0]
        except FileNotFoundError:
            cpu_info["Архитектура"] = "Нет данных"
        try:
            cpu_info["Количество ядер"] = winreg.QueryValueEx(cpu_key, "NumberOfCores")[0]
        except FileNotFoundError:
            cpu_info["Количество ядер"] = "Нет данных"
        winreg.CloseKey(cpu_key)
    except Exception as e:
        cpu_info = "Нет данных"

    return cpu_info


def get_memory_info():
    """
    Извлекает информацию о памяти.

    :return: Словарь с информацией о памяти.
    """
    memory_info = {}

    try:
        # Используем системные команды для получения данных о памяти
        if platform.system() == "Windows":
            result = subprocess.run(["wmic", "memorychip", "get", "Capacity"], capture_output=True, text=True)
            memory_sizes = [int(size) for size in result.stdout.split()[1:] if size.isdigit()]
            total_memory = sum(memory_sizes) // (1024 ** 3)  # Преобразуем в гигабайты
            memory_info["Общий объем"] = f"{total_memory} ГБ"
        else:
            memory_info["Общий объем"] = "Нет данных"
    except Exception as e:
        memory_info["Общий объем"] = "Нет данных"

    return memory_info


def get_disk_info():
    """
    Извлекает информацию о дисках.

    :return: Список словарей с информацией о дисках.
    """
    disk_info = []

    try:
        # Используем системные команды для получения данных о дисках
        if platform.system() == "Windows":
            result = subprocess.run(["wmic", "diskdrive", "get", "Model,SerialNumber,Size"], capture_output=True,
                                    text=True)
            lines = result.stdout.strip().split("\n")[1:]
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 2:
                    model = " ".join(parts[:-2])
                    serial = parts[-2]
                    size = int(parts[-1]) // (1024 ** 3)  # Преобразуем в гигабайты
                    disk_info.append({
                        "Модель": model,
                        "Серийный номер": serial,
                        "Размер": f"{size} ГБ"
                    })
    except Exception as e:
        disk_info.append({"Модель": "Нет данных", "Серийный номер": "Нет данных", "Размер": "Нет данных"})

    return disk_info


def get_network_info():
    """
    Извлекает информацию о сетевых адаптерах.

    :return: Список словарей с информацией о сетевых адаптерах.
    """
    network_info = []

    try:
        # Используем системные команды для получения данных о сетевых адаптерах
        if platform.system() == "Windows":
            result = subprocess.run(["wmic", "nic", "get", "Name,MACAddress"], capture_output=True, text=True)
            lines = result.stdout.strip().split("\n")[1:]
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 2:
                    name = " ".join(parts[:-1])
                    mac = parts[-1]
                    network_info.append({
                        "Имя": name,
                        "MAC-адрес": mac
                    })
    except Exception as e:
        network_info.append({"Имя": "Нет данных", "MAC-адрес": "Нет данных"})

    return network_info


def get_gpu_info():
    """
    Извлекает информацию о видеоадаптере с использованием WMI.

    :return: Список словарей с информацией о видеоадаптерах.
    """
    gpu_info = []

    try:
        # Используем WMI для получения данных о видеоадаптере
        c = wmi.WMI()
        for gpu in c.Win32_VideoController():
            gpu_info.append({
                "Имя": gpu.Name,
                "Версия драйвера": gpu.DriverVersion,
                "Разрешение": f"{gpu.CurrentHorizontalResolution}x{gpu.CurrentVerticalResolution}",
                "Память": f"{int(gpu.AdapterRAM) // (1024 ** 2)} МБ" if gpu.AdapterRAM else "Нет данных"
            })
    except Exception as e:
        gpu_info.append(
            {"Имя": "Нет данных", "Версия драйвера": "Нет данных", "Разрешение": "Нет данных", "Память": "Нет данных"})

    return gpu_info


def get_bios_info_from_registry():
    """
    Извлекает информацию о BIOS напрямую из реестра.

    :return: Словарь с информацией о BIOS.
    """
    bios_info = {}

    try:
        # Открываем ключ реестра для BIOS
        bios_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"HARDWARE\DESCRIPTION\System\BIOS"
        )

        # Получаем производителя BIOS
        try:
            manufacturer = winreg.QueryValueEx(bios_key, "BIOSVendor")[0]
            bios_info["Производитель BIOS"] = manufacturer
        except FileNotFoundError:
            bios_info["Производитель BIOS"] = "Нет данных"

        # Получаем версию BIOS
        try:
            version = winreg.QueryValueEx(bios_key, "BIOSVersion")[0]
            bios_info["Версия BIOS"] = version
        except FileNotFoundError:
            bios_info["Версия BIOS"] = "Нет данных"

        # Получаем дату выпуска BIOS
        try:
            release_date = winreg.QueryValueEx(bios_key, "BIOSReleaseDate")[0]
            bios_info["Дата выпуска BIOS"] = release_date
        except FileNotFoundError:
            bios_info["Дата выпуска BIOS"] = "Нет данных"

        # Получаем производителя системы (материнской платы)
        try:
            system_manufacturer = winreg.QueryValueEx(bios_key, "SystemManufacturer")[0]
            bios_info["Производитель системы"] = system_manufacturer
        except FileNotFoundError:
            bios_info["Производитель системы"] = "Нет данных"

        # Получаем модель системы (материнской платы)
        try:
            system_model = winreg.QueryValueEx(bios_key, "SystemProductName")[0]
            bios_info["Модель системы"] = system_model
        except FileNotFoundError:
            bios_info["Модель системы"] = "Нет данных"

        # Получаем серийный номер системы
        try:
            system_serial_number = winreg.QueryValueEx(bios_key, "SystemSerialNumber")[0]
            bios_info["Серийный номер системы"] = system_serial_number
        except FileNotFoundError:
            bios_info["Серийный номер системы"] = "Нет данных"

        winreg.CloseKey(bios_key)
    except Exception as e:
        print(f"Ошибка при чтении реестра: {e}")

    return bios_info


def get_installed_software():
    """
    Извлекает информацию об установленном программном обеспечении напрямую из реестра.

    :return: Список словарей с информацией о каждом установленном приложении.
    """
    installed_software = []

    # Ветки реестра для 64-битных и 32-битных программ
    registry_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    for path in registry_paths:
        try:
            # Открываем ключ реестра
            uninstall_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)

            # Перебираем все подразделы (каждый подраздел — это отдельное приложение)
            for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                try:
                    app_key_name = winreg.EnumKey(uninstall_key, i)
                    app_key = winreg.OpenKey(uninstall_key, app_key_name)

                    # Получаем информацию о приложении
                    app_info = {}
                    try:
                        app_info["Имя"] = winreg.QueryValueEx(app_key, "DisplayName")[0]
                    except FileNotFoundError:
                        continue  # Пропускаем, если нет имени

                    try:
                        app_info["Версия"] = winreg.QueryValueEx(app_key, "DisplayVersion")[0]
                    except FileNotFoundError:
                        app_info["Версия"] = "Нет данных"

                    try:
                        app_info["Издатель"] = winreg.QueryValueEx(app_key, "Publisher")[0]
                    except FileNotFoundError:
                        app_info["Издатель"] = "Нет данных"

                    try:
                        app_info["Путь установки"] = winreg.QueryValueEx(app_key, "InstallLocation")[0]
                    except FileNotFoundError:
                        app_info["Путь установки"] = "Нет данных"

                    try:
                        app_info["Комментарий"] = winreg.QueryValueEx(app_key, "Comments")[0]
                    except FileNotFoundError:
                        app_info["Комментарий"] = "Нет данных"

                    try:
                        app_info["Дата установки"] = winreg.QueryValueEx(app_key, "InstallDate")[0]
                    except FileNotFoundError:
                        app_info["Дата установки"] = "Нет данных"

                    # Добавляем информацию о приложении в список
                    installed_software.append(app_info)

                    winreg.CloseKey(app_key)
                except Exception as e:
                    print(f"Ошибка при обработке приложения {app_key_name}: {e}")

            winreg.CloseKey(uninstall_key)
        except Exception as e:
            print(f"Ошибка при чтении реестра {path}: {e}")

    return installed_software