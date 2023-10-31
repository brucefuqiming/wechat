# 微信工具

> 基于 appium 框架编写，适用于 Android 微信中文版本：8.0.42
>
> 仅用于技术研究

## 已完成功能

* 导出通讯录信息
* 检测单向联系人
* 标记联系人状态

## 运行环境

* 安装 [nodejs](https://nodejs.org/en)

* 添加 [adb](https://pan.baidu.com/s/10x3DJ9sTevTyZLOUYuA7dg?pwd=5fvb) 到系统环境变量

* 安装 [python](https://www.python.org/downloads/) 3.10

* 安装 [java](https://www.oracle.com/java/technologies/downloads/) 运行环境，并添加 JAVA_HOME 的环境变量

* 从nodejs 中安装 appium

````cmd
npm i --location=global appium
````

* 使用 appium 安装 uiautomator2 驱动

````cmd
appium driver install uiautomator2
````

## 快速使用

* 从 [Release ](https://github.com/Fly1st/wechat/releases)中下载最新版本的可执行文件
* 使用 adb 连接手机至能看到手机列表

````cmd
adb devices
````

* 启动 appium 服务

````cmd
appium
````

* 运行可执行文件

## 手动安装

* 下载或克隆项目

````cmd
git clone https://github.com/Fly1st/wechat-appium
````

* 进入项目根目录创建虚拟环境

````cmd
python -m venv venv
````

* 切换虚拟环境

````cmd
call .\venv\Scripts\activate.bat
set PYTHONPATH=.
````

* 还原依赖

````cmd
pip install -r requirements.txt
````

* 使用 adb 连接手机至能看到手机列表

````cmd
adb devices
````

* 启动 appium 服务

````cmd
appium
````

* 运行程序

````cmd
python .\script\run.py
python .\script\run_with_checker.py
````

* 在项目根目录创建一个批处理方便下次运行 (Windows)

````cmd
call .\venv\Scripts\activate.bat
set PYTHONPATH=.
python .\script\run.py
pause
````

## 注意事项

* adb 建议用有线，无线模式延迟可能会更高
* run.py 只会收集联系人的基础信息，速度更快
* run_checker.py 会同时检测好友的状态，速度更慢

