from appium.webdriver.common.appiumby import AppiumBy
from base.base_appium import AppDriverBase
from common.contact_handler import ContactHandler
from module.wechat_contact_info import WechatContactInfo


class WechatContact(AppDriverBase):
    def __init__(self, driver, module_contact_info: WechatContactInfo, module_contact_checker=None):
        super().__init__(driver)
        # 联系人处理程序
        self.contact_handler = ContactHandler()
        # 联系人信息模块
        self.module_contact_info = module_contact_info
        # 联系人检查器模块
        self.module_contact_checker = module_contact_checker
        # 用于记录总数
        self.contact_count = 0

    def click_contact(self):
        """
        点击联系人
        :return:
        """
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5y'])[2]"))

    def get_new_friends_location(self):
        """
        获取"新的朋友"位置
        :return:
        """
        return self.base_app_find_element("com.tencent.mm:id/obc").location

    def get_all_contact_elements(self):
        """
        获取当前页所有好友节点
        :return:
        """
        return self.base_app_find_elements("com.tencent.mm:id/kbo")

    def get_bottom_exists(self):
        # noinspection PyBroadException
        try:
            return self.base_app_find_element("com.tencent.mm:id/cak", timeout=0.2)
        except Exception:
            pass

    def scroll_contact(self):
        """
        滑动好友列表
        :return:
        """
        # 滑动方向：往上滑动
        # 滑动起点：当前页最后一个好友
        # 滑动终点：顶部的新的好友 位置

        end_scroll_location = self.get_new_friends_location()

        while True:
            # 获取当前页面的所有好友
            list_contract_el = self.get_all_contact_elements()
            if len(list_contract_el) == 0:
                break

            # # TODO 处理联系人列表
            for ct in list_contract_el:
                # 如果为True，表示已点击过
                if not self.contact_handler.element_is_exists(ct):
                    # 获取详细信息
                    if self.module_contact_checker is not None:
                        data = self.module_contact_info.run(ct, is_send_back=False)
                        data_check = self.module_contact_checker.run()
                        if data_check is not None:
                            data = {**data, **data_check}
                    else:
                        data = self.module_contact_info.run(ct)

                    # 写入
                    self.contact_handler.append_element(ct)
                    self.contact_handler.write_row(data)
                    self.contact_count += 1
                    print(data)

            # 判断到底
            if self.get_bottom_exists() is not None:
                break

            # 底部最后一个好友的位置，滑动开始的地方
            start_scroll_location = list_contract_el[len(list_contract_el) - 1].location

            # 开始滑动
            self.base_driver.swipe(start_scroll_location['x'], start_scroll_location['y'],
                                   end_scroll_location['x'], end_scroll_location['y'], 2500)

        print(f"一共 {self.contact_count}条数据")

    def run(self):
        print("# 获取通讯录")
        self.click_contact()
        self.scroll_contact()
        self.contact_handler.close_stream()
