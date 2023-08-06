import logging
import os
import re
import subprocess
import sys
import time
from typing import Dict
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(
#    __file__))))  # The sys.path.append line adds the parent directory of the tests directory to the Python module search path, allowing you to import modules from the root folder.

from utils.operations import subprocess_run, subprocess_popen, subprocess_check_output, subprocess_call

import config

logger = logging.getLogger(config.APPIUM_LOG_NAME)


def get_device_uuid() -> str:
    """
    Получает UUID подключенного устройства Android с помощью команды adb.
    Returns:
        UUID в виде строки.
    """

    # Определение команды для выполнения с помощью adb для получения списка устройств
    command = ['adb', 'devices']

    # Выполнение команды и получение вывода
    response = subprocess_check_output(command)

    # Извлечение списка устройств из полученного вывода с использованием регулярных выражений
    device_list = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+|\d+)', response)

    # Возвращение первого устройства из списка (UUID подключенного устройства Android)
    return device_list[0]


def get_device_model() -> str:
    """
    Получает модель подключенного устройства Android с помощью команды adb.
    Возвращает модель устройства.
    """
    command = ["adb", "shell", "getprop", "ro.product.model"]

    # Выполнение команды и получение вывода
    model = subprocess_check_output(command)

    # Возвращение модели устройства в виде строки
    return model


def get_package_name(path_to_apk: str) -> str:
    """
    Получает название пакета APK-файла с помощью команды aapt.
    Возвращает название пакета.
    """

    command = ["aapt", "dump", "badging", os.path.join(path_to_apk)]

    # Выполнение команды и получение вывода
    output: str = subprocess_check_output(command)

    # Извлечение строки, содержащей информацию о пакете
    start_index = output.index("package: name='") + len("package: name='")
    end_index = output.index("'", start_index)

    # Извлекаем название пакета
    package_name = output[start_index:end_index]

    # Возвращение названия пакета в виде строки
    return package_name


def get_launchable_activity_from_apk(path_to_apk: str) -> str:
    """
    Получает название запускаемой активности из APK-файла с помощью команды aapt.
    Возвращает название активности в виде строки.
    """
    logger.info(f"get_launchable_activity_from_apk < {path_to_apk}")

    command = ["aapt", "dump", "badging", path_to_apk]

    # Выполнение команды и получение вывода
    output = subprocess_check_output(command)

    # Извлечение строки, содержащей информацию о запускаемой активности
    package_line = [line for line in output.splitlines() if line.startswith("launchable-activity")][0]

    # Извлечение названия активности из строки
    launchable_activity = package_line.split("'")[1]

    # Возвращение названия активности в виде строки

    logger.info(f"get_launchable_activity_from_apk > {launchable_activity}")
    return launchable_activity


def push(source: str, destination: str) -> bool:
    """
    Копирует файл или директорию на подключенное устройство.

    Аргументы:
        source (str): Путь к копируемому файлу или директории.
        destination (str): Путь назначения на устройстве.

    Возвращает:
        bool: True, если файл или директория были успешно скопированы, False в противном случае.
    """
    command = ["adb", "push", source, destination]
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.push()")
        logger.error(e)
        return False


def pull(source: str, destination: str) -> bool:
    """
    Копирует файл или директорию с подключенного устройства.

    Аргументы:
        source (str): Путь к исходному файлу или директории на устройстве.
        destination (str): Целевой путь для сохранения скопированного файла или директории.

    Возвращает:
        bool: True, если файл или директория были успешно скопированы, False в противном случае.
    """
    command = ["adb", "pull", source, destination]
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.pull()")
        logger.error(e)
        return False


def install(source: str) -> bool:
    """
    Устанавливает файл APK на подключенном устройстве.

    Аргументы:
        source (str): Путь к файлу APK для установки.

    Возвращает:
        bool: True, если файл APK был успешно установлен, False в противном случае.
    """
    command = ["adb", "install", "-r", source]
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.install()")
        logger.error(e)
        return False


def start_activity(package, activity):
    """
    Запускает активность на подключенном устройстве.

    Аргументы:
        package (str): Название пакета активности.
        activity (str): Название запускаемой активности.

    Возвращает:
        bool: True, если активность была успешно запущена, False в противном случае.
    """
    command = ['adb', 'shell', 'am', 'start', '-n', f'{package}/{activity}']
    try:
        subprocess_check_output(command)
        return True
    except Exception as e:
        logger.error("adb.start_activity()")
        logger.error(e)
        return False


def close_app(package):
    time.sleep(3)
    """
    Принудительно останавливает указанный пакет с помощью ADB.

    Аргументы:
        package (str): Название пакета приложения для закрытия.

    Возвращает:
        bool: True, если приложение успешно закрыто, False в противном случае.
    """
    command = ['adb', 'shell', 'am', 'force-stop', package]
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.close_app()")
        logger.error(e)
        return False


def reboot_app(package: str, activity: str) -> bool:
    """
    Перезапускает приложение, закрывая его и затем запуская указанную активность.

    Аргументы:
        package (str): Название пакета приложения.
        activity (str): Название активности для запуска.

    Возвращает:
        bool: True, если перезапуск приложения выполнен успешно, False в противном случае.
    """
    # Закрытие приложения
    if not close_app(package=package):
        return False

    # Запуск указанной активности
    if not start_activity(package=package, activity=activity):
        return False

    return True


def uninstall_app(package: str) -> bool:
    """
    Удаляет указанный пакет с помощью ADB.

    Аргументы:
        package (str): Название пакета приложения для удаления.

    Возвращает:
        bool: True, если приложение успешно удалено, False в противном случае.
    """
    command = ['adb', 'uninstall', package]
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.uninstall_app()")
        logger.error(e)
        return False


def press_home() -> bool:
    """
    Отправляет событие нажатия кнопки Home на устройство с помощью ADB.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    command = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME']
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.press_home()")
        logger.error(e)
        return False


def press_back() -> bool:
    """
    Отправляет событие нажатия кнопки Back на устройство с помощью ADB.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    command = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK']
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.press_back()")
        logger.error(e)
        return False


def press_menu() -> bool:
    """
    Отправляет событие нажатия кнопки Menu на устройство с помощью ADB.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    command = ['adb', 'shell', 'input', 'keyevent', 'KEYCODE_MENU']
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.press_menu()")
        logger.error(e)
        return False


def input_keycode_num_(num: int) -> bool:
    """
    Отправляет событие нажатия клавиши с числовым значением на устройство с помощью ADB.
    Допустимые значения: 0-9, ADD, COMMA, DIVIDE, DOT, ENTER, EQUALS

    Аргументы:
        num (int): Числовое значение клавиши для нажатия.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    command = ['adb', 'shell', 'input', 'keyevent', f'KEYCODE_NUMPAD_{num}']
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.input_keycode_num_()")
        logger.error(e)
        return False


def input_keycode(keycode: str) -> bool:
    """
    Вводит указанный код клавиши на устройстве с помощью ADB.

    Аргументы:
        keycode (str): Код клавиши для ввода.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    command = ['adb', 'shell', 'input', 'keyevent', f'{keycode}']
    try:
        subprocess_run(command)
        return True
    except Exception as e:
        logger.error("adb.input_keycode()")
        logger.error(e)
        return False


def input_by_virtual_keyboard(key: str, keyboard: Dict[str, tuple]) -> bool:
    """
    Вводит строку символов с помощью виртуальной клавиатуры.

    Аргументы:
        key (str): Строка символов для ввода.
        keyboard (dict): Словарь с маппингом символов на координаты нажатий.

    Возвращает:
        bool: True, если ввод выполнен успешно, False в противном случае.
    """
    try:
        for char in key:
            # Вызываем функцию tap с координатами, соответствующими символу char
            tap(*keyboard[char])
        return True
    except Exception as e:
        # Логируем ошибку и возвращаем False в случае возникновения исключения
        logging.error(f"Произошла ошибка при вводе строки с помощью виртуальной клавиатуры: {e}")
        return False


def input_text(text: str) -> bool:
    """
    Вводит указанный текст на устройстве с помощью ADB.

    Аргументы:
        text (str): Текст для ввода.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    # Формируем команду для ввода текста с использованием ADB
    command = ['adb', 'shell', 'input', 'text', text]
    try:
        # Выполняем команду
        subprocess_run(command)
        return True
    except Exception as e:
        # Логируем ошибку, если возникло исключение
        logger.error("adb.input_text()")
        logger.error(e)
        return False


def tap(x, y):
    """
    Выполняет нажатие на указанные координаты на устройстве с помощью ADB.

    Аргументы:
        x: Координата X для нажатия.
        y: Координата Y для нажатия.

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    # Формируем команду для выполнения нажатия по указанным координатам с использованием ADB
    command = ['adb', 'shell', 'input', 'tap', x, y]
    try:
        # Выполняем команду
        subprocess_run(command)
        return True
    except Exception as e:
        # Логируем ошибку, если возникло исключение
        logger.error("adb.tap()")
        logger.error(e)
        return False


def swipe(start_x, start_y, end_x, end_y, duration: int = 300):
    """
    Выполняет свайп (перетаскивание) с одной точки на экране в другую на устройстве с помощью ADB.

    Аргументы:
        start_x: Координата X начальной точки свайпа.
        start_y: Координата Y начальной точки свайпа.
        end_x: Координата X конечной точки свайпа.
        end_y: Координата Y конечной точки свайпа.
        duration (int): Длительность свайпа в миллисекундах (по умолчанию 300).

    Возвращает:
        bool: True, если команда была успешно выполнена, False в противном случае.
    """
    # Формируем команду для выполнения свайпа с использованием ADB
    command = ['adb', 'shell', 'input', 'swipe', str(start_x), str(start_y), str(end_x), str(end_y), str(duration)]
    try:
        # Выполняем команду
        subprocess_run(command)
        return True
    except Exception as e:
        # Логируем ошибку, если возникло исключение
        logger.error("adb.swipe()")
        logger.error(e)
        return False


def get_current_app_package():
    """
    Получает пакет текущего запущенного приложения на устройстве с помощью ADB.

    Возвращает:
        str: Название пакета текущего запущенного приложения, либо None, если произошла ошибка.
    """
    # Определяем команду в виде списка строк
    command = [
        "adb", "shell", "dumpsys", "window", "windows", "|", "grep", "-E", "'mCurrentFocus|mFocusedApp'",
        "|", "grep", "-e", "'mFo'"
    ]
    try:
        # Выполняем команду и получаем результат
        result = subprocess_check_output(command)
        # Находим позицию последнего вхождения подстроки "/." в строке
        end_index = result.rfind("/")
        # Извлекаем название приложения из предшествующих символов
        start_index = result.rfind(" ", 0, end_index) + 1
        app_name = result[start_index:end_index]
        return app_name
    except Exception as e:
        # Логируем ошибку, если возникло исключение
        logger.error("adb.get_current_app_package()")
        logger.error(e)
        return None


def check_VPN(ip: str = ''):
    """
    Проверяет, активно ли VPN-соединение на устройстве с помощью ADB.

    Аргументы:
        ip (str): IP-адрес для проверки VPN-соединения. Если не указан, используется значение из конфигурации.

    Возвращает:
        bool: True, если VPN-соединение активно, False в противном случае.
    """
    if ip == '':
        ip = config.VPN_IP
    # Определяем команду в виде списка строк
    command = ['adb', 'shell', 'netstat', '|', 'grep', '-w', '-e', ip]
    try:
        # Выполняем команду и получаем вывод
        output = subprocess_run(command)
        if "ESTABLISHED" in output:
            logger.debug("check_VPN() True")
            return True
        else:
            logger.debug("check_VPN() False")
            return False
    except Exception as e:
        # Логируем ошибку, если возникло исключение
        logger.error("adb.check_VPN")
        logger.error(e)
        return False


def stop_logcat():
    """
    Останавливает выполнение logcat на устройстве с помощью ADB.

    Возвращает:
        bool: True, если выполнение logcat остановлено успешно, False в противном случае.
    """
    command = ['adb', 'shell', 'ps', '|', 'grep', 'logcat']
    # Получаем список выполняющихся процессов logcat
    try:
        process_list = subprocess_check_output(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    # Проходим по списку процессов и отправляем каждому сигнал SIGINT
    for process in process_list.splitlines():
        pid = process.split()[1]
        try:
            subprocess_call(['adb', 'shell', 'kill', '-s', 'SIGINT', pid])
        except Exception as e:
            logger.error("adb.stop_logcat")
            logger.error(e)
            return False
    return True


def reload_adb():
    """
    Перезапускает adb-сервер на устройстве.

    Возвращает:
        bool: True, если adb-сервер успешно перезапущен, False в противном случае.
    """
    try:
        command = ['adb', 'kill-server']
        subprocess_run(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    # Ожидаем некоторое время перед запуском adb-сервера
    time.sleep(3)
    try:
        command = ['adb', 'start-server']
        subprocess_run(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def kill_by_pid(pid: str):
    """
    Отправляет сигнал SIGINT для остановки процесса по указанному идентификатору PID с помощью ADB.

    Аргументы:
        pid (str): Идентификатор PID процесса для остановки.

    Возвращает:
        bool: True, если процесс успешно остановлен, False в противном случае.
    """
    command = ['adb', 'shell', 'kill', '-s', 'SIGINT', str(pid)]
    try:
        subprocess_call(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def kill_by_name(name: str):
    """
    Останавливает все процессы с указанным именем на устройстве с помощью ADB.

    Аргументы:
        name (str): Имя процесса для остановки.

    Возвращает:
        bool: True, если все процессы успешно остановлены, False в противном случае.
    """
    command = ['adb', 'shell', 'pkill', '-l', 'SIGINT', str(name)]
    try:
        subprocess_call(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def kill_all(name: str):
    """
    Останавливает все процессы, соответствующие указанному имени, на устройстве с помощью ADB.

    Аргументы:
        name (str): Имя процесса или шаблон имени для остановки.

    Возвращает:
        bool: True, если все процессы успешно остановлены, False в противном случае.
    """
    command = ['adb', 'shell', 'pkill', '-f', str(name)]
    try:
        subprocess_call(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def delete_files_from_internal_storage(path):
    """
    Удаляет файлы из внутреннего хранилища устройства с помощью ADB.

    Аргументы:
        path (str): Путь к файлам для удаления.

    Возвращает:
        bool: True, если файлы успешно удалены, False в противном случае.
    """
    command = ['adb', 'shell', 'rm', '-rf', f'{path}*']
    try:
        subprocess_run(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def pull_video(path):
    """
    Копирует видеофайлы с устройства на компьютер с помощью ADB.

    Аргументы:
        path (str): Путь для сохранения скопированных видеофайлов.

    Возвращает:
        bool: True, если видеофайлы успешно скопированы, False в противном случае.
    """
    command = ['adb', 'pull', '/sdcard/Movies/', f'{path}']
    try:
        subprocess_popen(command)
        time.sleep(30)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    command = ['adb', 'shell', 'rm', '-rf', '/sdcard/Movies/*']
    try:
        subprocess_popen(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def stop_video():
    """
    Останавливает запись видео на устройстве с помощью ADB.

    Возвращает:
        bool: True, если запись видео успешно остановлена, False в противном случае.
    """
    command = ['adb', 'shell', 'pkill', '-l', 'SIGINT', 'screenrecord']
    try:
        subprocess_call(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def record_video(filename):
    """
    Записывает видео на устройстве с помощью ADB.

    Аргументы:
        filename (str): Имя файла для сохранения видео.

    Возвращает:
        bool: True, если запись видео успешно начата, False в противном случае.
    """
    command = ['adb', 'shell', 'screenrecord', f'sdcard/Movies/{filename}']
    try:
        subprocess_popen(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def reboot():
    """
    Перезагружает устройство с помощью ADB.

    Возвращает:
        bool: True, если перезагрузка успешно запущена, False в противном случае.
    """
    command = ['adb', 'shell', 'reboot']
    try:
        subprocess_call(command)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return False
    return True


def get_screen_resolution():
    """
    Возвращает разрешение экрана устройства с помощью ADB.

    Возвращает:
        tuple[int, int] or None: Кортеж с шириной и высотой экрана в пикселях, или None в случае ошибки.
    """
    command = ['adb', 'shell', 'wm', 'size']
    try:
        output = subprocess_run(command)
        if "Physical size" in output:
            resolution_str = output.split(":")[1].strip()
            width, height = resolution_str.split("x")
            return int(width), int(height)
    except Exception as e:
        logger.error("adb.stop_logcat")
        logger.error(e)
        return None
