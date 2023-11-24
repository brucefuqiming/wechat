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



---------------------------------------------
其他

* 需要[node 18.17](https://nodejs.org/dist/v18.17.0/)以上
* 需要[java 17](https://www.oracle.com/java/technologies/downloads/#jdk17-mac)以上
* 下载[android sdk](https://dl-ssl.google.com/android/repository/android-21_r01.zip)、platform-tools、build-tools，参考[下载Android SDK tools完成Android SDK 安装、配置环境变量](https://cloud.tencent.com/developer/article/2107040)、[AndroidDevTools](https://www.androiddevtools.cn/)，必要情况下可能需要从官网安装Android开发工具套件或[命令行工具](https://developer.android.com/studio?hl=zh-tw#command-tools)
* 将sdk、build-tools、platform-tools放在同一目录下，同时把build-tools中的/lib/apksigner.jar拷贝到根目录下，
<img width="608" alt="image" src="https://github.com/brucefuqiming/wechat/assets/11450222/4704cde8-26f3-4541-b37f-959f789a0b63">

* 配置环境变量(.bash_profile)如下所示：
```
export ANDROID_SDK_ROOT=/Users/xxx/android-5.0
export ANDROID_PLATFORM_TOOLS=/Users/xxx/android-5.0/platform-tools
export ANDROID_BUILD_TOOLS=/Users/brucefu/xxx/android-5.0/build-tools
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home
```
配置完成后记得source ~/.bash_profile

* mac下，将run.py和run_with_checker.py拷贝到根目录下运行

* 小米手机，在开发者模式中“关闭MIUI优化”
