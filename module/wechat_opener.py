from base.base_appium import AppDriverBase


class WechatOpener(AppDriverBase):
    def __init__(self, driver):
        super().__init__(driver)

    def run(self):
        print("")
        print("## MADE BY FLY1ST")
        print("## avb@live.com")
        print("## https://github.com/Fly1st\n")
        print("# 启动微信\n")
        self.base_terminate_app("com.tencent.mm")
        self.base_start_activity("com.tencent.mm/com.tencent.mm.ui.LauncherUI")

