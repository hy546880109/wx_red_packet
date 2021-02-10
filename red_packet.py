from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "10.0",  # 系统版本号
    "deviceName": "b68548ed",  # 设备名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
    'unicodeKeyboard': True,  # 使用自带输入法
    'noReset': True  # 保留 session 信息，可以避免重新登录
}

# 判断元素是否存在

def is_element_exist(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        return False
    else:
        return True

# 删除领取后的红包记录


def del_red_envelope(wait, driver):
    # 长按领取过的红包
    r8 = wait.until(EC.element_to_be_clickable(
        (By.ID, "com.tencent.mm:id/ahs")))
    TouchAction(driver).long_press(r8).perform()
    # 点击长按后显示的删除
    wait.until(EC.element_to_be_clickable(
        (By.ID, "com.tencent.mm:id/dt5"))).click()
    # 点击弹出框的删除选项
    wait.until(EC.element_to_be_clickable(
        (By.ID, "com.tencent.mm:id/ffp"))).click()


# 删除第一个聊天框
def del_red_public(wait, driver):
    # 长按第一个聊天框
    r8 = wait.until(EC.element_to_be_clickable(
        (By.ID, "com.tencent.mm:id/fzg")))
    TouchAction(driver).long_press(r8).perform()
    # 点击长按后显示的删除
    wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='不显示该聊天']"))).click()
    # 点击弹出框的删除选项
    wait.until(EC.element_to_be_clickable(
        (By.ID, "com.tencent.mm:id/ffp"))).click()


if __name__ == '__main__':
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    # 设置等待
    wait = WebDriverWait(driver, 500)

    while True:
    # 进入第一个聊天窗口
        g73 = wait.until(EC.element_to_be_clickable(
            (By.ID, "com.tencent.mm:id/fzg")))
        g73.click()
        print("进入了第一个聊天窗口")
        # 判断聊天窗是否是公众号
        is_weichat = is_element_exist(driver, "id", "com.tencent.mm:id/u1")
        if is_weichat == True:
        # while True:
            # 有红包则点击
            wait.until(EC.element_to_be_clickable(
                (By.ID, "com.tencent.mm:id/u1"))).click()
            print("点击了红包")
            # 判断红包是否被领取
            is_open = is_element_exist(driver, "id", "com.tencent.mm:id/f4f")
            print("红包是否被领取：", is_open)
            if is_open == True:
                # 红包未被领取，点击开红包
                wait.until(EC.element_to_be_clickable(
                    (By.ID, "com.tencent.mm:id/f4f"))).click()
                print('已经领取红包')
                # 返回群聊
                driver.keyevent(4)
                # 删除领取过的红包记录
                del_red_envelope(wait, driver)
                print('···删除已经领取的红包，等待新的红包')
                driver.keyevent(4)
            else:
                # 返回群聊
                driver.keyevent(4)
                # 删除领取过的红包记录
                del_red_envelope(wait, driver)
                print('···删除无法领取的红包，等待新的红包')
                driver.keyevent(4)

        else:
            print('没有红包则隐藏此聊天框')
            # 返回群聊
            driver.keyevent(4)
            # 删除第一个公众号窗口
            del_red_public(wait, driver)
            print('隐藏了第一个聊天框')
            
