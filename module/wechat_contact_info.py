from base.base_appium import AppDriverBase


class WechatContactInfo(AppDriverBase):
    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def click_element(element):
        """
        点击当前节点
        :param element:
        :return:
        """
        element.click()

    def get_remark_text(self):
        """
        获取备注信息
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/cf8", timeout=1)

    def get_nickname_text(self):
        """
        获取昵称
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/cf7", timeout=1)

    def get_account_text(self):
        """
        获取账号
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/cff", timeout=1)

    def get_region_text(self):
        """
        获取地区
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/cf6", timeout=1)

    def get_info(self):
        remark = None
        nickname = None
        account = None
        region = None

        # 备注
        # noinspection PyBroadException
        try:
            remark = self.get_remark_text()
        except Exception:
            pass

        # 如果昵称不存在，那么显示名称就是昵称
        # 如果昵称存在，那么显示名称就是备注
        # noinspection PyBroadException
        try:
            nickname = self.get_nickname_text()
            if nickname is not None:
                nickname = nickname.split(':', 1)[1].strip()

        except Exception:
            pass

        if nickname is None:
            nickname = remark
            remark = None

        # 微信号
        # noinspection PyBroadException
        try:
            account = self.get_account_text()
            if account is not None:
                account = account.split(':', 1)[1].strip()
        except Exception:
            pass

        # 地区
        # noinspection PyBroadException
        try:
            region = self.get_region_text()
            if region is not None:
                region = region.split(':', 1)[1].strip()
        except Exception:
            pass

        return {'remark': remark, 'nickname': nickname, 'account': account, 'region': region}

    def send_back_keycode(self):
        # 返回
        self.base_app_press_keycode(4)

    def run(self, element, is_send_back=True):
        self.click_element(element)
        data = self.get_info()
        if is_send_back:
            self.send_back_keycode()
        return data
