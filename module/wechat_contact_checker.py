from base.base_appium import BaseAppDriver


class WechatContactChecker(BaseAppDriver):
    def __init__(self, driver):
        super().__init__(driver)

    def click_send_msg(self):
        self.base_app_click("com.tencent.mm:id/cfb")

    def click_plus(self):
        pass

    def click_transfer(self):
        pass

    def input_amount(self):
        pass

    def click_pay(self):
        pass

