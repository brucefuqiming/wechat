from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from base.base_appium import BaseAppDriver


class WechatContactChecker(BaseAppDriver):
    def __init__(self, driver):
        super().__init__(driver)

    def click_send_msg(self):
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5n'])[1]"), timeout=1)

    def click_plus(self):
        self.base_app_click("com.tencent.mm:id/bqn", timeout=1)

    def click_transfer(self):
        self.base_app_click(
            loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/a1u']/android.widget.LinearLayout)[6]"),
            timeout=1)

    def get_transfer_name_text(self):
        transfer_name = self.base_app_get_text("com.tencent.mm:id/lwo")
        print(transfer_name)

    def input_amount(self):
        pass

    def click_pay(self):
        pass

    def send_back(self, back_count):
        for i in range(0, back_count):
            self.base_app_press_keycode(4)

    def click_contact(self):
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5y'])[2]"))

    def run(self):

        # noinspection PyBroadException
        try:
            self.click_send_msg()
        except Exception:
            self.send_back(1)
            return

        # noinspection PyBroadException
        try:
            self.click_plus()
        except Exception:
            self.send_back(1)
            self.click_contact()
            return

        # noinspection PyBroadException
        try:
            self.click_transfer()
        except Exception:
            self.send_back(2)
            self.click_contact()
            return

        sleep(0.1)
        self.get_transfer_name_text()
        self.send_back(4)
        self.click_contact()


