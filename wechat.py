from script.run import main as script_run
from script.run_with_checker import main as script_run_with_checker

# pyinstaller --clean --onefile --icon .\test\wechat_128_icon.ico wechat.py

print("")
print("## WeChat Tools")
print("## Version: v1.1-20231031\n")
print("## MADE BY FLY1ST")
print("## avb@live.com\n")
print("## 该程序完全免费，已开源到Github")
print("## 项目地址: https://github.com/Fly1st/wechat\n")
print("## 确保手机已连接到adb, 以及 appium 服务已开启\n")

print("1, 仅导出基本信息 (速度快)")
print("2, 导出所有信息 (速度慢)\n")

while True:
    result = input("输入选项: ")
    if result == '1' or result == '2':
        break
    else:
        print("# 请输入正确的选项\n")

if result == '1':
    script_run()
elif result == '2':
    script_run_with_checker()

input('\ninput any key to exit ..')
