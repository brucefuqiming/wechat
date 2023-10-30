from appium.webdriver.common.appiumby import AppiumBy
from base.base_appium import BaseAppDriver
from common.contact_handler import ContactHandler
from module.wechat_contact_info import WechatContactInfo


class WechatContact(BaseAppDriver):
    def __init__(self, driver, module_contact_info: WechatContactInfo):
        super().__init__(driver)
        self.contact_handler = ContactHandler()
        self.module_contact_info = module_contact_info
        self.contact_count = 0

    def click_contact(self):
        self.base_app_click(loc=(AppiumBy.XPATH, "(//*[@resource-id='com.tencent.mm:id/h5y'])[2]"))

    def scroll_contact(self):
        # 滑动方向：往上滑动
        # 滑动起点：当前页最后一个好友
        # 滑动终点：顶部的新的好友 位置

        end_scroll_location = self.base_app_find_element("com.tencent.mm:id/obc").location

        while True:
            # 获取当前页面的所有好友
            list_contract_el = self.base_app_find_elements("com.tencent.mm:id/kbo")
            if len(list_contract_el) == 0:
                break

            # # TODO 处理联系人列表
            for ct in list_contract_el:
                # 如果为True，表示已点击过
                if not self.contact_handler.element_is_exists(ct):
                    # 获取详细信息
                    data = self.module_contact_info.run(ct)
                    # 写入
                    self.contact_handler.append_element(ct)
                    self.contact_handler.write_row(data)
                    self.contact_count += 1
                    print(data)
                    # print(ct)

            # 底部最后一个好友的位置，滑动开始的地方
            start_scroll_location = list_contract_el[len(list_contract_el) - 1].location

            # 开始滑动
            self.base_driver.swipe(start_scroll_location['x'], start_scroll_location['y'],
                                   end_scroll_location['x'], end_scroll_location['y'], 2500)

            # 判断是否到底，对比最后三项联系人
            if len(list_contract_el) > 3:
                list_contract_el = list_contract_el[-3:]

            scrolled_element = self.base_app_find_elements("com.tencent.mm:id/kbo")
            if len(scrolled_element) > 3:
                scrolled_element = scrolled_element[-3:]

            if list_contract_el == scrolled_element:
                break

        print(f"一共 {self.contact_count}条数据")

    def run(self):
        print("# 获取通讯录")
        self.click_contact()
        self.scroll_contact()
        self.contact_handler.close_stream()
