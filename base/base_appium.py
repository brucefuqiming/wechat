"""
******************************************************************************************
      Appium 功能封装
      Coder：落叶
      EMail：avb@live.com
     Github：https://github.com/Fly1st
******************************************************************************************
"""
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class AppDriverController(object):
    """
    AppDriver控制器
    """

    def __init__(self, server_url='http://127.0.0.1:4723', android_version=None, chromedriver_executable=None):
        self.server_url = server_url
        self.android_version = android_version
        self.chromedriver_executable = chromedriver_executable
        self.base_driver = None

    def start_android_driver(self, custom_capabilities=None):
        """
        开启驱动
        :return:
        """
        if self.server_url is None:
            self.server_url = 'http://127.0.0.1:4723'

        capabilities = {'platformName': 'Android', 'appium:automationName': 'uiautomator2',
                        'appium:deviceName': 'Android',
                        'appium:noReset': True, 'appium:forceAppLaunch': True,
                        'appium:unicodeKeyboard': True, 'appium:resetKeyboard': True}
        if self.android_version is not None:
            capabilities['appium:platformVersion'] = self.android_version
        if self.chromedriver_executable is not None:
            capabilities['appium:chromedriverExecutable'] = self.chromedriver_executable
        if custom_capabilities is not None and type(custom_capabilities) is dict:
            capabilities.update(custom_capabilities)

        options = UiAutomator2Options().load_capabilities(capabilities)
        self.base_driver = webdriver.Remote(command_executor=self.server_url, options=options)

        return self.base_driver

    def stop_driver(self):
        """
        停止驱动
        :return:
        """
        if self.base_driver is not None:
            self.base_driver.quit()
            self.base_driver = None


class AppDriverBase(object):
    def __init__(self, driver):
        self.base_driver = driver

    def base_get_page_source(self):
        return self.base_driver.page_source

    def base_get_window_size(self, window_handle: str = "current"):
        return self.base_driver.get_window_size(window_handle)

    def base_press_keycode(self, keycode: int):
        self.base_driver.press_keycode(keycode)

    def base_is_installed(self, app_id):
        """
        检测app是否安装,返回bool
        :param app_id:
        :return:
        """
        return self.base_driver.execute_script('mobile: isAppInstalled', {'appId': app_id})

    def base_query_app_state(self, app_id):
        """
        检测app状态
        0, not install
        1, installed and not running
        3, running in background
        4, running in foreground
        :param app_id:
        :return:
        """
        return self.base_driver.execute_script('mobile: queryAppState', {'appId': app_id})

    def base_activate_app(self, app_id):
        """
        启动app
        :param app_id:
        :return:
        """
        self.base_driver.execute_script('mobile: activateApp', {'appId': app_id})

    def base_remove_app(self, app_id):
        """
        移除app，返回bool
        :param app_id:
        :return:
        """
        return self.base_driver.execute_script('mobile: removeApp', {'appId': app_id})

    def base_terminate_app(self, app_id):
        """
        停止app
        :param app_id:
        :return:
        """
        return self.base_driver.execute_script('mobile: terminateApp', {'appId': app_id})

    def base_install_app(self, app_path):
        """
        安装app
        :param app_path:
        :return:
        """
        self.base_driver.execute_script('mobile: installApp', {'appPath': app_path})

    def base_clear_app(self, app_path):
        """
        清除app数据
        :param app_path:
        :return:
        """
        return self.base_driver.execute_script('mobile: clearApp', {'appPath': app_path})

    def base_start_activity(self, intent):
        """
        打开app活动
        :param intent:
        :return:
        """
        self.base_driver.execute_script('mobile: startActivity', {'intent': intent})

    def base_switch_webview(self, webview):
        self.base_driver.switch_to.context(webview)

    def base_switch_native(self):
        self.base_driver.switch_to.context("NATIVE_APP")

    def base_find_element(self, loc, timeout=5, poll_frequency=0.05):
        type_loc = type(loc)
        if type_loc is tuple or type_loc is str:
            wdw = WebDriverWait(self.base_driver, timeout=timeout, poll_frequency=poll_frequency)
            if type_loc is tuple:
                return wdw.until(lambda x: x.find_element(*loc))
            elif type_loc is str:
                return wdw.until(lambda x: x.find_element(AppiumBy.ID, loc))

    def base_find_elements(self, loc, timeout=5, poll_frequency=0.05):
        type_loc = type(loc)
        if type_loc is tuple or type_loc is str:
            wdw = WebDriverWait(self.base_driver, timeout=timeout, poll_frequency=poll_frequency)
            if type_loc is tuple:
                return wdw.until(lambda x: x.find_elements(*loc))
            elif type_loc is str:
                return wdw.until(lambda x: x.find_elements(AppiumBy.ID, loc))

    @staticmethod
    def base_find_sub_element(loc, element):
        type_loc = type(loc)
        if type_loc is tuple:
            return element.find_element(*loc)
        elif type_loc is str:
            return element.find_element(AppiumBy.ID, loc)

    @staticmethod
    def base_find_sub_elements(loc, element):
        type_loc = type(loc)
        if type_loc is tuple:
            return element.find_elements(*loc)
        elif type_loc is str:
            return element.find_elements(AppiumBy.ID, loc)

    def base_click(self, loc, **kwargs):
        self.base_find_element(loc, **kwargs).click()

    def base_input(self, loc, val, clear=True, **kwargs):
        el = self.base_find_element(loc, **kwargs)
        if clear:
            el.clear()
        el.send_keys(val)

    def base_get_text(self, loc, **kwargs):
        return self.base_find_element(loc, **kwargs).text

    def base_get_is_displayed(self, loc, **kwargs):
        return self.base_find_element(loc, **kwargs).is_displayed()

    def base_get_attribute(self, loc, name, **kwargs):
        return self.base_find_element(loc, **kwargs).get_attribute(name)

    def base_get_dom_attribute(self, loc, name, **kwargs):
        return self.base_find_element(loc, **kwargs).get_dom_attribute(name)

    def base_get_property(self, loc, name, **kwargs):
        return self.base_find_element(loc, **kwargs).get_property(name)

    def base_get_is_enabled(self, loc, **kwargs):
        return self.base_find_element(loc, **kwargs).is_enabled()

    def base_get_is_selected(self, loc, **kwargs):
        return self.base_find_element(loc, **kwargs).is_selected()

    def base_set_text(self, loc, keys, **kwargs):
        self.base_find_element(loc, **kwargs).set_text(keys)

    def base_set_value(self, loc, val, **kwargs):
        self.base_find_element(loc, **kwargs).set_value(val)

    def base_send_keys(self, loc, *val, **kwargs):
        self.base_find_element(loc, **kwargs).send_keys(*val)

    def base_scroll(self, loc_origin, loc_destination, duration=None, **kwargs):
        self.base_driver.scroll(self.base_find_element(loc_origin, **kwargs),
                                self.base_find_element(loc_destination, **kwargs), duration)

    def base_drag_and_drop(self, loc_origin, loc_destination, **kwargs):
        self.base_driver.drag_and_drop(self.base_find_element(loc_origin, **kwargs),
                                       self.base_find_element(loc_destination, **kwargs))


class AppDriverTaBase(object):
    """
    TouchAction相关功能
    """

    def __init__(self, driver):
        self.base_driver = driver
        self.base_driver_ta = TouchAction(driver)

    def base_ta_find_element(self, loc, timeout=5, poll_frequency=0.05):
        type_loc = type(loc)
        if type_loc is tuple or type_loc is str:
            wdw = WebDriverWait(self.base_driver, timeout=timeout, poll_frequency=poll_frequency)
            if type_loc is tuple:
                return wdw.until(lambda x: x.find_element(*loc))
            elif type_loc is str:
                return wdw.until(lambda x: x.find_element(AppiumBy.ID, loc))

    def base_ta_tap_element(self, loc, count=1, **kwargs):
        self.base_driver_ta.tap(element=self.base_ta_find_element(loc, **kwargs), count=count).perform()

    def base_ta_tap_location(self, x, y, count=1):
        self.base_driver_ta.tap(x=x, y=y, count=count).perform()

    def base_ta_press_element(self, loc, **kwargs):
        self.base_driver_ta.press(el=self.base_ta_find_element(loc, **kwargs)).perform()

    def base_ta_press_location(self, x, y):
        self.base_driver_ta.press(x=x, y=y).perform()

    def base_ta_long_press_element(self, loc, duration=1000, **kwargs):
        self.base_driver_ta.long_press(el=self.base_ta_find_element(loc, **kwargs), duration=duration).perform()

    def base_ta_long_press_location(self, x, y, duration=1000):
        self.base_driver_ta.long_press(x=x, y=y, duration=duration).perform()

    def base_ta_move_to_element(self, loc, **kwargs):
        self.base_driver_ta.move_to(el=self.base_ta_find_element(loc, **kwargs)).perform()

    def base_ta_move_to_location(self, x, y):
        self.base_driver_ta.move_to(x=x, y=y)
