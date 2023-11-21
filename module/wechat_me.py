from appium.webdriver.common.appiumby import AppiumBy
from base.base_appium import AppDriverBase


class WechatMe(AppDriverBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_me(self):
        self.base_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5y'])[4]"))

    def get_nickname_text(self):
        return self.base_get_text("com.tencent.mm:id/kbb")

    def get_account_text(self):
        return self.base_get_text("com.tencent.mm:id/ouv")

    def run(self):
        print("# 获取微信信息")
        self.click_me()
        nickname = self.get_nickname_text()
        account = self.get_account_text()
        print(f"昵称: {nickname}\n{account}\n")
