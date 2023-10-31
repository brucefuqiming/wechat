from base.base_appium import AppDriverController
from module.wechat_contact import WechatContact
from module.wechat_contact_info import WechatContactInfo
from module.wechat_me import WechatMe
from module.wechat_opener import WechatOpener


def main():
    # 初始化控制器，并开启驱动
    controller = AppDriverController()
    base_driver = controller.start_android_driver()

    # 打开微信
    WechatOpener(base_driver).run()

    # 进入"我的"
    WechatMe(base_driver).run()

    # 通讯录
    module_contact_info = WechatContactInfo(base_driver)
    WechatContact(base_driver, module_contact_info=module_contact_info).run()


if __name__ == '__main__':
    main()
