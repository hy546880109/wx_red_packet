# wx_red_packet
python + appium 实现微信自动抢红包功能，因为运行需要先隐藏聊天框，介意的勿用。
运行的是真机小米9，需要按自己的实际场景运行的请自行修改如下配置信息：

desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "10.0",  # 系统版本号
    "deviceName": "b68548ed",  # 设备名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
    'unicodeKeyboard': True,  # 使用自带输入法
    'noReset': True  # 保留 session 信息，可以避免重新登录
}