# 微信工具

> 适用于 Android 微信版本：8.0.42

## 已完成功能

* 导出所有通讯录信息到csv
  * 包括 备注，昵称，微信号，地区


## 开发中功能

* 检测单向联系人
* 删除单向联系人
* 标记异常联系人
* 统计联系人信息

## 运行环境

* 安装 [nodejs](https://nodejs.org/en)

* 下载 [adb](https://pan.baidu.com/s/10x3DJ9sTevTyZLOUYuA7dg?pwd=5fvb) 工具包并添加到系统环境变量

* 安装 [python 3.10](https://www.python.org/downloads/)

* 安装 [java](https://www.oracle.com/java/technologies/downloads/) 运行环境

* 从nodejs 中安装 appium

````cmd
npm i --location=global appium
````

* 使用 appium 安装 uiautomator2 驱动

````cmd
appium driver install uiautomator2
````

## 安装

* 下载或克隆项目

````cmd
git clone https://github.com/Fly1st/wechat
````

* 进入项目根目录创建虚拟环境

````cmd
python -m venv venv
````

* 切换虚拟环境

````cmd
call .\venv\Scripts\activate.bat
````

* 还原依赖

````cmd
pip install -r requirements.txt
````

* 使用 adb 连接手机至 adb devices 能看到手机列表

````cmd
adb devices
````

* 启动 appium 服务器

````cmd
appium
````

* 运行程序

````cmd
python run.py
````

* 在项目跟文件夹创建一个批处理方便下次运行

````cmd
call .\venv\Scripts\activate.bat
python run.py
pause
````

