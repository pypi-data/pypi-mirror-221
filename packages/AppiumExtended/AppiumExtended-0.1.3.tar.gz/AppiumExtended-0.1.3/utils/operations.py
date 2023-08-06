import re
import os
import logging
import subprocess
import requests
import serial.tools.list_ports
import shutil
import json
from typing import List, Optional

import config

logger = logging.getLogger(config.APPIUM_LOG_NAME)
START_DIR = os.getcwd()


def subprocess_run(command: List[str]) -> str:
    """
    Выполняет команду в подпроцессе и возвращает вывод команды в виде строки.

    Аргументы:
        command (List[str]): Список строк, представляющих команду и ее аргументы.

    Возвращает:
        str: Вывод команды в виде строки.

    """
    if config.PROXY:
        # Если используется прокси, отправляем запрос к серверу Flask для выполнения команды
        response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/subprocess_run',
                                 data={'command': ' '.join(command)}).text
    else:
        # Иначе выполняем команду с помощью subprocess.run и получаем вывод команды
        response = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True).stdout
    return str(response).strip()


def subprocess_popen(command: List[str]) -> str:
    """
    Выполняет команду в подпроцессе с использованием Popen и возвращает вывод команды в виде строки.

    Аргументы:
        command (List[str]): Список строк, представляющих команду и ее аргументы.

    Возвращает:
        str: Вывод команды в виде строки.

    """
    if config.PROXY:
        # Если используется прокси, отправляем запрос к серверу Flask для выполнения команды
        response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/subprocess_popen',
                                 data={'command': ' '.join(command)}).text
    else:
        # Иначе выполняем команду с помощью subprocess.Popen и сохраняем объект процесса
        response = subprocess.Popen(command, shell=True)
    return str(response).strip()


def subprocess_popen_background(command: List[str]) -> str:
    """
    Выполняет команду в подпроцессе с использованием Popen и возвращает вывод команды в виде строки.

    Аргументы:
        command (List[str]): Список строк, представляющих команду и ее аргументы.

    Возвращает:
        str: Вывод команды в виде строки.

    """
    if config.PROXY:
        # Если используется прокси, отправляем запрос к серверу Flask для выполнения команды
        response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/subprocess_popen_background',
                                 data={'command': ' '.join(command)}).text
    else:
        # Иначе выполняем команду с помощью subprocess.Popen и сохраняем объект процесса
        response = subprocess.Popen(command, shell=True)
    return str(response).strip()


def subprocess_check_output(command: List[str]) -> str:
    """
    Выполняет команду в подпроцессе с использованием check_output и возвращает вывод команды в виде строки.

    Аргументы:
        command (List[str]): Список строк, представляющих команду и ее аргументы.

    Возвращает:
        str: Вывод команды в виде строки.

    """
    if config.PROXY:
        # Если используется прокси, отправляем запрос к серверу Flask для выполнения команды
        response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/subprocess_check_output',
                                 data={'command': ' '.join(command)}).text
    else:
        # Иначе выполняем команду с помощью subprocess.check_output и декодируем вывод в строку
        response = subprocess.check_output(command).decode('utf-8')
    return str(response).strip()


def subprocess_call(command: List[str]) -> str:
    """
    Выполняет команду в подпроцессе с использованием call и возвращает код завершения команды в виде строки.

    Аргументы:
        command (List[str]): Список строк, представляющих команду и ее аргументы.

    Возвращает:
        str: Код завершения команды в виде строки.

    """
    if config.PROXY:
        # Если используется прокси, отправляем запрос к серверу Flask для выполнения команды
        response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/subprocess_call',
                                 data={'command': ' '.join(command)}).text
    else:
        # Иначе выполняем команду с помощью subprocess.call
        response = subprocess.call(command)
    return str(response).strip()


def requests_get(url: str, local_path: str) -> bool:
    """
    Выполняет запрос на удаленный сервер по указанному url и загружает файл по указанному local_path.

    Аргументы:
    - url (str): URL для загрузки файла.
    - local_path (str): Путь для сохранения загруженного файла.

    Возвращает:
    - bool: True, если загрузка файла успешна, иначе False.
    """

    # Выполняем POST-запрос на удаленный сервер
    response = requests.post(f'http://{config.FLASK_IP}:{config.FLASK_PORT}/requests_get',
                             data={'url': url, 'local_path': local_path})

    # Проверяем статус и результат запроса
    if response.status_code == 200 and response.text == "OK":
        return True
    else:
        return False


def upload_file(file: str, path: str):
    """
    Загружает файл на сервер по указанному пути.

    Аргументы:
    - file (str): путь до файла (включая файл с расширением).
    - path (str): Путь для сохранения загруженного файла.

    Возвращает:
    - bool: True, если загрузка файла успешна, иначе False.
    """
    command = ['chmod', '+rwx', file]
    subprocess.run(command)
    with open(file, 'rb') as file:
        logger.info("file: < {}".format(file))
        logger.info("path: < {}".format(path))

        files = {'file': file}

        response = requests.post(url=f'http://{config.FLASK_IP}:{config.FLASK_PORT}/upload_file',
                                 files=files, data={'path': path})
    # Проверяем статус и результат запроса
    if response.status_code == 200 and response.text == "OK":
        return True
    else:
        logger.info("upload_file(): response.status_code > {}".format(response.status_code))
        logger.info("upload_file(): response.text > {}".format(response.text))
        return False


def extract_numeric(variable: str) -> Optional[float]:
    """
    Извлекает числовое значение из переменной.

    Аргументы:
        variable (str): Переменная, из которой нужно извлечь числовое значение.

    Возвращает:
        Optional[float]: Числовое значение, извлеченное из переменной.
        Если числовое значение не найдено, возвращает None.
    """
    number: Optional[float] = None  # Инициализируем переменную number значением None
    regex = r'-?\d+(?:,\d+)?'  # Регулярное выражение для поиска числового значения
    match = re.search(regex, variable)  # Поиск совпадения в переменной с помощью регулярного выражения
    if match:
        # Если найдено совпадение, извлекаем числовое значение и преобразуем его в тип float
        number = float(match.group().replace(',', '.'))
    return number


def find_latest_folder(path: str) -> Optional[str]:
    """
    Находит последнюю папку по указанному пути.

    Аргументы:
        path (str): Путь, в котором нужно найти последнюю папку.

    Возвращает:
        Optional[str]: Имя последней найденной папки. Если папки не найдены, возвращает None.
    """
    # Шаблон имени папки
    pattern = re.compile(r"launch_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}")
    # Получение списка папок в указанном пути
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # Фильтрация папок по шаблону имени
    dirs = [d for d in dirs if pattern.match(d)]
    # Сортировка папок в обратном порядке
    dirs.sort(reverse=True)
    if dirs:
        # Последняя папка в отсортированном списке
        latest_dir = dirs[0]
        return str(latest_dir)
    else:
        return None


def get_com() -> Optional[str]:
    """
    Возвращает номер COM-порта для подключенного устройства.

    Возвращает:
        Optional[str]: Номер COM-порта. Если порт не найден, возвращает None.
    """
    ports = serial.tools.list_ports.comports()  # Получение списка доступных COM-портов
    for port in ports:
        if int(port.device[3:]) > 10:  # Проверка, является ли номер порта числом больше 10
            try:
                ser = serial.Serial(port.device)  # Попытка открыть последовательное соединение с портом
                ser.close()  # Закрытие соединения
                return port.device[3:]  # Возврат номера порта (без префикса "COM")
            except serial.SerialException:
                pass
    return None  # Если порт не найден, возвращается None


def copy_file(source: str, destination: str) -> None:
    """
    Копирует файл из исходного пути в целевой путь.

    Аргументы:
        source (str): Исходный путь файла.
        destination (str): Целевой путь для копирования файла.

    Возвращает:
        None
    """
    # Отладочное сообщение с выводом исходного и целевого пути
    logger.debug("copy_file() source %s, destination %s", source, destination)
    try:
        # Копирование файла из исходного пути в целевой путь
        shutil.copy(source, destination)
        # Отладочное сообщение об успешном копировании файла
        logger.debug("File copied successfully!")
    except IOError as e:
        # Сообщение об ошибке при копировании файла
        logger.error("Unable to copy file: %s" % e)


def count_currency_numbers(number: int) -> tuple:
    """
    Вычисляет количество вхождений купюр разных достоинств в заданную сумму.

    Аргументы:
        number (int): Сумма, для которой нужно вычислить количество купюр.

    Возвращает:
        tuple: Кортеж, содержащий количество купюр разных достоинств в порядке убывания достоинства:
               (количество купюр 5000, количество купюр 1000, количество купюр 500, количество купюр 100).
    """
    if number < 100:
        number = 100  # Если сумма меньше 100, устанавливаем ее равной 100 (важно для вычисления сдачи)
    count_5000 = number // 5000  # Вычисляем количество купюр достоинством 5000
    remainder = number % 5000  # Вычисляем остаток после вычета купюр достоинством 5000
    count_1000 = remainder // 1000  # Вычисляем количество купюр достоинством 1000
    remainder = remainder % 1000  # Вычисляем остаток после вычета купюр достоинством 1000
    count_500 = remainder // 500  # Вычисляем количество купюр достоинством 500
    remainder = remainder % 500  # Вычисляем остаток после вычета купюр достоинством 500
    count_100 = remainder // 100  # Вычисляем количество купюр достоинством 100
    return count_5000, count_1000, count_500, count_100  # Возвращаем кортеж с количеством купюр разных достоинств


def read_json(path: str, filename: str):
    """
    Читает JSON-файл из указанного пути и возвращает его данные.

    Аргументы:
        path (str): Относительный путь к директории, где находится JSON-файл.
        filename (str): Имя JSON-файла.

    Возвращает:
        dict: Данные JSON-файла. Если файл не найден, возвращает None.
    """
    filepath = os.path.join(START_DIR, path, filename)  # Формируем полный путь к JSON-файлу
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # Открываем JSON-файл для чтения
            data = json.load(f)  # Загружаем данные из JSON-файла
    except FileNotFoundError:
        logger.error("Файл не найден")  # Выводим сообщение об ошибке, если файл не найден
        return None
    return data  # Возвращаем данные из JSON-файла


def str_to_float(number: str) -> float:
    """
    Преобразует строковое представление суммы в формате float.

    Аргументы:
        number (str): Строковое представление суммы.

    Возвращает:
        float: Сумма в формате float.
    """
    # Преобразуем аргумент в строку (на случай, если он уже является строкой)
    number = str(number)
    # Заменяем запятую на точку и удаляем символы "₽" и пробелы, затем преобразуем в float
    number = float(number.replace(',', '.').replace('₽', '').replace(' ', ''))
    # Возвращаем сумму в формате float
    return number






