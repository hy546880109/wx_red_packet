# wx_red_packet
python + appium 实现微信自动抢红包功能，因为运行需要先隐藏聊天框，介意的勿用。
运行的是真机小米9，需要按自己的实际场景运行的请自行修改如下配置信息：
需要已经登陆好微信账号再运行。
优化：对不同设备的兼容，可以让用户输入不同设备的名称和版本进行兼容。
desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "10.0",  # 系统版本号
    "deviceName": "b68548ed",  # 设备名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
    'unicodeKeyboard': True,  # 使用自带输入法
    'noReset': True  # 保留 session 信息，可以避免重新登录
}
实现思路：
https://github.com/hy546880109/wx_red_packet/blob/main/1510016-20210210113946506-1400512179.png

