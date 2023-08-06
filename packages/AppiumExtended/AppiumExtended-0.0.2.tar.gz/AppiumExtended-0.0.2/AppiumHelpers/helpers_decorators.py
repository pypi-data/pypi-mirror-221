# coding: utf-8
import sys
import io
import time
import functools
import logging
from functools import wraps
from datetime import datetime

import allure
import numpy as np
from PIL import Image

import config

logger = logging.getLogger(config.APPIUM_LOG_NAME)


def retry(func):
    max_retries = 3

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        for _ in range(max_retries):
            result = func(*args, **kwargs)
            if result is not None and result is not False:
                return result
            else:
                time.sleep(1)
        return result

    return wrapper


def wait_until_window_change(poll_frequency: float = 0.1):
    """
    Декоратор, который ожидает изменения содержимого окна в течение заданного периода времени.

    Аргументы:
        poll_frequency (float): Частота опроса содержимого окна на наличие изменений в секундах.
                               По умолчанию 0.1 секунды.

    Возвращает:
        function: Декорированная функция.
    """

    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """
            Оберточная функция, которая инкапсулирует декорированную функцию с логикой обнаружения изменений окна.

            Аргументы:
                self: Экземпляр класса, к которому принадлежит декорированный метод.
                *args: Произвольное число аргументов, переданных в декорированный метод.
                **kwargs: Произвольное число именованных аргументов, переданных в декорированный метод.

            Возвращает:
                bool: True, если содержимое окна изменяется в течение заданного периода времени, иначе False.
            """
            print("wait_until_window_change")

            # Инициализация
            result = False
            func_result = None
            decorator_args = kwargs.get('decorator_args', {})
            timeout_window = decorator_args.get('timeout_window', 30)
            window_not_changing_period = decorator_args.get('window_not_changing_period', 10)

            start_time = time.time()  # Запись начального времени
            print("func_result = func(self, *args, **kwargs)")
            func_result = func(self, *args, **kwargs)  # Вызов декорированной функции и сохранение результата
            print("func_result: ", func_result)

            # Обнаружение изменений экрана с экспоненциальной задержкой
            poll_interval = poll_frequency
            while time.time() - start_time < timeout_window:  # Продолжаем до достижения тайм-аута
                window_not_changing_period_start_time = time.time()  # Запускаем новый период, в течение которого окно не изменяется
                window_not_changed = True  # Флаг для отслеживания того, изменилось ли окно за период

                while time.time() - window_not_changing_period_start_time < window_not_changing_period:
                    # Делаем снимок экрана и сохраняем его в памяти
                    # self.driver.set_window_size(800, 600)  # Установить меньшее разрешение, если необходимо
                    image_bytes = self.driver.get_screenshot_as_png()
                    image = Image.open(io.BytesIO(image_bytes)).convert('L')  # Преобразуем в оттенки серого
                    # Обрезаем снимок до определенной области
                    box = (50, 50, 400, 400)  # Определяем координаты для обрезки (лево, верх, право, низ)
                    image = image.crop(box)

                    time.sleep(poll_interval)  # Ждем указанный интервал между опросами
                    new_image_bytes = self.driver.get_screenshot_as_png()
                    new_image = Image.open(io.BytesIO(new_image_bytes)).convert('L')  # Преобразуем в оттенки серого
                    new_image = new_image.crop(box)

                    # Проверяем, отличается ли сумма значений пикселей на двух изображениях
                    if np.sum(image) != np.sum(new_image):
                        window_not_changed = False  # Содержимое окна изменилось
                        break

                if window_not_changed:
                    logger.debug("Содержимое окна не изменялось в течение периода")
                    return True

                poll_interval *= 2  # Удваиваем время ожидания для каждого опроса

            if not result:
                logger.info(f"{func.__name__}() > {func_result}. Изменение экрана: False")
                return False

        return wrapper

    return func_decorator


def wait_for_window_change(poll_frequency: float = 0.5):
    """
    Декоратор, который ожидает изменения окна перед выполнением декорированной функции.
    Он делает снимок экрана окна, обрезает его и сравнивает с последующими снимками,
    чтобы обнаружить любые изменения.

    Аргументы:
        poll_frequency (float): Частота проверки окна на изменения.

    Возвращает:
        Декоратор функции.
    """

    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            """
            Оберточная функция, которая выполняет обнаружение изменения окна и выполнение декорированной функции.

            Аргументы:
                self: Экземпляр класса, содержащего декорированную функцию.
                *args: Переменное число аргументов.
                **kwargs: Произвольные именованные аргументы.

            Возвращает:
                Результат декорированной функции или False, если изменение окна не было обнаружено.
            """

            # Инициализация
            result = False
            func_result = None
            decorator_args = kwargs.get('decorator_args', {})
            timeout_window = decorator_args.get('timeout_window', 10)
            tries = decorator_args.get('tries', 3)

            # Сделать снимок экрана и сохранить его в памяти
            image_bytes = self.driver.get_screenshot_as_png()  # Сделать снимок экрана окна и получить данные изображения в виде байтов
            image = Image.open(io.BytesIO(image_bytes)).convert(
                'L')  # Открыть изображение из байтов и преобразовать его в оттенки серого

            # Обрезать снимок экрана до определенной области
            box = (50, 50, 400, 400)  # Определить координаты прямоугольной области для обрезки (лево, верх, право, низ)
            image = image.crop(box)  # Обрезать изображение на основе заданных координат области

            # Попытаться обнаружить изменение экрана
            for _ in range(tries):  # Выполнить попытки обнаружения на основе заданного числа попыток
                start_time = time.time()  # Записать текущее время начала попытки обнаружения
                func_result = func(self, *args, **kwargs)  # Выполнить декорированную функцию и сохранить результат

                # Обнаружить изменение экрана с экспоненциальной задержкой
                poll_interval = poll_frequency  # Установить начальный интервал проверки равным заданной частоте проверки
                while time.time() - start_time < timeout_window:  # Проверить, находится ли прошедшее время в пределах заданного окна времени ожидания
                    time.sleep(poll_interval)  # Приостановить выполнение на заданный интервал проверки
                    new_image_bytes = self.driver.get_screenshot_as_png()  # Сделать новый снимок экрана окна и получить данные изображения в виде байтов
                    new_image = Image.open(io.BytesIO(new_image_bytes)).convert(
                        'L')  # Открыть новое изображение из байтов и преобразовать его в оттенки серого
                    new_image = new_image.crop(box)  # Обрезать новое изображение на основе заданных координат области

                    if not np.sum(image) == np.sum(
                            new_image):  # Сравнить суммы значений пикселей между исходным и новым изображениями
                        logger.debug(
                            "Изменение экрана обнаружено")  # Записать сообщение о том, что произошло изменение экрана
                        return True  # Вернуть True для обозначения обнаружения изменения экрана

                    poll_interval *= 2  # Удвоить интервал проверки для следующей итерации (экспоненциальная задержка)

            if not result:
                logger.info(
                    f"{func.__name__}() > {func_result}. Изменение экрана: False")  # Записать сообщение о том, что изменение экрана не было обнаружено
                return False  # Вернуть False для обозначения отсутствия обнаружения изменения экрана

        return wrapper

    return func_decorator


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.2f} seconds")
        return result

    return wrapper


def step_info(my_str):
    """
    Декоратор, который перед вызовом метода вызывает logger.info и @allure.step,
    передавая в них строковую переменную, принятую в параметрах.

    Аргументы:
        my_str (str): Строковая переменная для использования в logger.info и @allure.step.

    Возвращает:
        function: Декоратор функций.

    Пример использования:
        @my_step_info("Мой шаг")
        def my_function():
            ...
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        @allure.step(my_str)
        def wrapper(*args, **kwargs):
            # Логируем информацию перед вызовом метода
            logger.info(my_str)
            # Выполняем исходную функцию
            result = func(*args, **kwargs)
            # Логируем информацию после успешного выполнения метода
            logger.info(f"{my_str} [выполнено успешно]")
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


def screenshots():
    """
    В случае возникновения AssertionError в обернутом методе - прикрепляет к allure report скриншот до выполнения
    метода и после возникновения исключения, а также информацию об ошибке.
    В ином случае скриншот не прикрепляется.
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Получаем скриншот до вызова метода
            screenshot = self.driver.get_screenshot_as_png()
            # Генерируем временную метку для имени скриншота
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # Устанавливаем имя скриншота до вызова метода
            screenshot_name_begin = f"screenshot_begin_{timestamp}.png"
            try:
                # Выполняем исходную функцию
                result = func(self, *args, **kwargs)
            except AssertionError as e:
                # Если произошло исключение, прикрепляем скриншот до вызова метода к отчету
                allure.attach(screenshot, name=screenshot_name_begin, attachment_type=allure.attachment_type.PNG)
                # Прикрепляем информацию об ошибке AssertionError к отчету
                allure.attach(str(e), name="AssertionError", attachment_type=allure.attachment_type.TEXT)
                # Рейзим исключение AssertionError с сохраненным traceback
                raise AssertionError(str(e)).with_traceback(sys.exc_info()[2])
            finally:
                # Получаем скриншот после вызова метода
                screenshot = self.driver.get_screenshot_as_png()
                # Обновляем временную метку для имени скриншота
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                # Устанавливаем имя скриншота после вызова метода
                screenshot_name_end = f"screenshot_end_{timestamp}.png"
                # Прикрепляем скриншот после вызова метода к отчету
                allure.attach(screenshot, name=screenshot_name_end, attachment_type=allure.attachment_type.PNG)
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


def log_debug():
    """
    Логирует начало и завершение обернутого метода
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        def wrapper(*args, **kwargs):
            # Получаем имя метода
            method_name = func.__name__
            # Логируем начало выполнения метода и переданные аргументы
            logger.debug(f"{method_name}() < {', '.join(map(str, args))}, "
                         f"{', '.join(f'{k}={v}' for k, v in kwargs.items())}")
            # Выполняем исходную функцию
            result = func(*args, **kwargs)
            # Если результат существует, логируем его
            if result:
                logger.debug(f"{method_name}() > {str(result)}")
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator


def print_me():
    """
    Печатает начало и завершение обернутого метода
    """

    # Определяем декоратор функций
    def func_decorator(func):
        # Создаем обертку функции, сохраняющую метаданные исходной функции
        def wrapper(*args, **kwargs):
            # Получаем имя метода
            method_name = func.__name__
            # Печатаем начало выполнения метода и переданные аргументы
            print(f"{method_name}() < {', '.join(map(str, args))}, "
                  f"{', '.join(f'{k}={v}' for k, v in kwargs.items())}")
            # Выполняем исходную функцию
            result = func(*args, **kwargs)
            # Если результат существует, логируем его
            if result:
                print(f"{method_name}() > {str(result)}")
            # Возвращаем результат выполнения исходной функции
            return result

        # Возвращаем обертку функции
        return wrapper

    # Возвращаем декоратор функций
    return func_decorator
