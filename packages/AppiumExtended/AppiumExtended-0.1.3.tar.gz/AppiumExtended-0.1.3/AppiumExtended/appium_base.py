# coding: utf-8
import logging
import json
import time

from appium import webdriver

import config
from AppiumServer.appium_server import AppiumServer
from AppiumHelpers.appium_image import AppiumImage


class AppiumBase(object):
    """
    Класс работы с Appium.
    Обеспечивает подключение к устройству
    """

    def __init__(self):

        # keep_alive_server: bool = False,
        # log_level = 'error',
        # url = 'http://localhost:4723/wd/hub',
        # port = 4723,

        self.url = f"http://{config.APPIUM_IP}:{config.APPIUM_PORT}/wd/hub"
        self.capabilities = None
        self.keep_alive_server = True
        self.driver = None
        self.logger = logging.getLogger(config.APPIUM_LOG_NAME)
        self.server = AppiumServer(port=config.APPIUM_IP, log_level=config.APPIUM_LOG_LEVEL)
        self.image = None

    def connect(self, capabilities: dict):
        """
        Подключение к устройству
        """
        self.capabilities = capabilities
        self.logger.debug(
            f"connect(capabilities {self.capabilities}")
        if not config.PROXY:
            # запускаем локальный сервер Аппиум
            if not self.server.is_alive():
                self.server.start()
                time.sleep(10)
                self.server.wait_until_alive()

        self.logger.info(f"Подключение к серверу: {self.url=}")
        self.driver = webdriver.Remote(command_executor=self.url,
                                       desired_capabilities=self.capabilities,
                                       keep_alive=True)

        app_capabilities = json.dumps(capabilities)

        # Инициализация объектов требующих драйвер
        self.image = AppiumImage(driver=self.driver)

        self.logger.info('Подключение установлено: '.format(app_capabilities))
        self.logger.info(f'Сессия №: {self.driver.session_id}')

    def disconnect(self):
        """
        Отключение от устройства
        """
        if self.driver:
            self.logger.debug(f"Отключение от сессии №: {self.driver.session_id}")
            self.driver.quit()
            self.driver = None
        if not self.keep_alive_server:
            self.server.stop()

    def is_running(self):
        return self.driver.is_running()

