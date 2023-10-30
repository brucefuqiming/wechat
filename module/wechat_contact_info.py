from selenium.common import TimeoutException

from base.base_appium import BaseAppDriver


class WechatContactInfo(BaseAppDriver):
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def click_element(element):
        element.click()

    def get_info(self):
        remark = None
        nickname = None
        account = None
        region = None

        # 备注
        try:
            remark = self.base_app_get_text("com.tencent.mm:id/cf8", timeout=1, poll_frequency=0.05)
        except:
            pass

        # 如果昵称不存在，那么显示名称就是昵称
        # 如果昵称存在，那么显示名称就是备注
        try:
            nickname = self.base_app_get_text("com.tencent.mm:id/cf7", timeout=1, poll_frequency=0.05)
            if nickname is not None:
                nickname = nickname.split(':', 1)[1].strip()

        except TimeoutException:
            pass

        if nickname is None:
            nickname = remark
            remark = None

        # 微信号
        try:
            account = self.base_app_get_text("com.tencent.mm:id/cff", timeout=1, poll_frequency=0.05)
            if account is not None:
                account = account.split(':', 1)[1].strip()
        except TimeoutException:
            pass

        # 地区
        try:
            region = self.base_app_get_text("com.tencent.mm:id/cf6", timeout=1, poll_frequency=0.05)
            if region is not None:
                region = region.split(':', 1)[1].strip()
        except TimeoutException:
            pass

        return {'remark': remark, 'nickname': nickname, 'account': account, 'region': region}

    def send_back_keycode(self):
        # 返回
        self.base_app_press_keycode(4)

    def run(self, element):
        self.click_element(element)
        data = self.get_info()
        self.send_back_keycode()
        return data
