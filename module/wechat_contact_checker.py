import re
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from base.base_appium import BaseAppDriver


class WechatContactChecker(BaseAppDriver):
    def __init__(self, driver):
        super().__init__(driver)

    def click_contact(self):
        """
        点击通讯录
        :return:
        """
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5y'])[2]"))

    def click_send_msg(self):
        """
        点击发送消息
        :return:
        """
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5n'])[1]"), timeout=1)

    def click_plus(self):
        """
        点击加号
        :return:
        """
        self.base_app_click("com.tencent.mm:id/bqn", timeout=1)

    def click_transfer(self):
        """
        点击转账
        :return:
        """
        # self.base_app_click(
        #     loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/a1u']/android.widget.LinearLayout)[6]"),
        #     timeout=1)
        self.base_app_click(loc=(AppiumBy.XPATH, "//*[@resource-id='com.tencent.mm:id/a12' and @text='转账']"),
                            timeout=1)

    def get_transfer_title_text(self):
        """
        获取转账页面的名称信息
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/lwo")

    def input_amount(self):
        """
        支付页面点击按钮输入金额
        :return:
        """
        # 0.1
        self.base_app_click("com.tencent.mm:id/hqb")
        self.base_app_click("com.tencent.mm:id/hqz")
        self.base_app_click("com.tencent.mm:id/hqc")

    def click_pay(self):
        """
        支付页面点击转账
        :return:
        """
        self.base_app_click("com.tencent.mm:id/hql")

    def get_pay_error_result_text(self):
        """
        支付页面转账失败提示文字
        :return:
        """
        return self.base_app_get_text("com.tencent.mm:id/jlg")

    def click_pay_i_know(self):
        """
        支付页面转账失败，点击"我知道了"
        :return:
        """
        self.base_app_click("com.tencent.mm:id/jln")

    def get_pay_success_button_element(self):
        """
        获取支付页面 支付节点
        :return:
        """
        return self.base_app_find_element(loc=(AppiumBy.XPATH, "//android.widget.TextView[@text='支付']"),
                                          timeout=3)

    def parse_transfer_title(self):
        """
        解析转账人名称
        :return:
        """
        transfer_title = self.get_transfer_title_text()
        pattern1 = r"^.*\((\*.)\)$"
        pattern2 = r"^.*\((\*\*.)\)$"
        result = re.findall(pattern1, transfer_title)

        if result is None or len(result) == 0:
            result = re.findall(pattern2, transfer_title)
            if result is None or len(result) == 0:
                return None
        return result[0]

    def get_transfer_info(self):
        """
        获取转账详细信息
        :return:
        """
        transfer_name = self.parse_transfer_title()
        if transfer_name is not None:
            # 用户为好友关系
            return {'name': transfer_name, 'state': 0}

        # 需再次判断才能确定不是好友
        self.input_amount()
        self.click_pay()
        result = self.check_pay_result()
        if result == 0:
            # 返回一次
            self.send_back(1)
            sleep(0.5)
        else:
            # 点击"我知道了"
            self.click_pay_i_know()
            sleep(0.5)
        return {'name': transfer_name, 'state': result}

    def check_pay_result(self):
        """
        检测转账状态
        :return:
        """
        # 获取不是好友的信息，如果不是单向好友，则处理异常
        # noinspection PyBroadException
        try:
            error_result_text = self.get_pay_error_result_text()
        except Exception:
            error_result_text = None

        if error_result_text is not None:
            if "你不是收款方好友" in error_result_text:
                # 不是收款方好友
                return 1
            elif "对方微信号已被限制登录" in error_result_text:
                # 被限制登录
                return 2
            else:
                # 其它情况
                return 3
        else:
            # 确认正常状态
            success_result = self.get_pay_success_button_element()
            if success_result is not None:
                # 是好友
                return 0
            else:
                # 不是好友，属于未知情况了
                return 4

    def send_back(self, back_count):
        """
        返回
        :param back_count:
        :return:
        """
        for i in range(0, back_count):
            self.base_app_press_keycode(4)

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
        result = self.get_transfer_info()
        self.send_back(4)
        self.click_contact()

        code = result['state']

        if code == 0:
            result['desc'] = "正常状态"
        elif code == 1:
            result['desc'] = "单向好友"
        elif code == 2:
            result['desc'] = "限制登录"
        elif code == 3:
            result['desc'] = "其它状态"
        elif code == 4:
            result['desc'] = "未知状态"

        return result
