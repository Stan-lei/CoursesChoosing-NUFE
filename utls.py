import time
from datetime import datetime

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

USERNAME = ""
PWD = ""


# MEDIA = "./media/"
# ICODE_IMG = MEDIA + "icode_img.png"


def hint() -> None:
    while True:
        op = input("**********************************************\n"
                   "欢迎使用自动抢课平台，"
                   "由于登录需要一定的时间，\n"
                   "请计算好时间提前运行本程序\n"
                   "**********************************************\n"
                   "\n"
                   "此外，由于验证码的识别需要配置许多外部库，\n"
                   "为方便用户使用，请在程序自动键入账号密码后手动输入验证码\n"
                   "**********************************************\n"
                   "\n"
                   "输入Y/y开始进行登录："
                   )
        if op == 'Y' or op == "y":
            global USERNAME, PWD
            USERNAME = input("请输入用户名/账号：")
            PWD = input("请输入密码：")
            break
        else:
            print("\n\n\n")


def timing():

    pass


"""
这里计划做验证码识别，
但是需要很多CV和AI的库，
所以把验证码改成手动输入
"""
# def get_icode(driver):
#     driver.find_element(By.ID, 'icode').screenshot(ICODE_IMG)
#     pass


def accept_alert(driver) -> str:
    info = []
    while True:
        try:
            time.sleep(0.3)
            alert = driver.switch_to.alert
            info.append(alert.text)
            alert.accept()
        except NoAlertPresentException:
            break
    return ' '.join(info)


def login(driver):
    """
        login into system
    """
    username = driver.find_element(By.ID, "txtUserName")
    pwd = driver.find_element(By.ID, "TextBox2")
    icode = driver.find_element(By.ID, "txtSecretCode")

    ICODE = input("请输入验证码：")

    username.send_keys(USERNAME)
    pwd.send_keys(PWD)
    icode.send_keys(ICODE)
    driver.find_element(By.ID, "Button1").click()
    pass


def goto_choose_courses(driver):
    """
    跳转到通识选课
    """
    wsxk = driver.find_element(By.XPATH, '//*[@id="headDiv"]/ul/li[2]/a/span')
    ActionChains(driver).move_to_element(wsxk).perform()
    driver.find_element(By.LINK_TEXT, u'通识教育选修课').click()
    pass


def set_courses_len(driver):
    """
    设置页面最大课程数量
    """
    inner_frame = driver.find_element(By.ID, "iframeautoheight")
    driver.switch_to.frame(inner_frame)

    # courses_len = driver.find_element(By.ID, "dpkcmcGrid_lblTotalRecords").text
    driver.find_element(By.NAME, "dpkcmcGrid:txtPageSize").send_keys(200)
    driver.find_element(By.ID, "Button1").click()
    driver.switch_to.default_content()
    pass


def read_courses() -> list:
    courses_pool = []
    with open("./courses.csv", 'r') as f:
        for line in f.readlines():
            courses_pool.append(line.strip())
    courses_pool.pop(0)
    return courses_pool
    pass


def get_courses(driver) -> str:
    var_define = "var datalist = window.frames['zhuti'].document.getElementById('kcmcGrid'); " \
                 "var tabBody = datalist.tBodies[0];" \
                 "var len = tabBody.rows.length; " \
                 "var courses = " \

    courses_pool = read_courses()

    loop_body = ";for (let i = 1; i < len; i++) { \
            if (courses.includes(tabBody.rows[i].cells[2].innerText)) { \
                window.frames['zhuti'].document.getElementById('kcmcGrid__ctl' + (i+1) +  '_xk').checked = true; \
            } \
        } \
        window.frames['zhuti'].document.getElementById('Button1').click();"

    JS_CODE = var_define + str(courses_pool) + loop_body
    driver.execute_script(JS_CODE)
    return accept_alert(driver)


def batch(driver):
    set_courses_len(driver)
    i = 1
    while True:
        rlt = get_courses(driver)
        print("第{0}次抢课结果：".format(i), rlt)
        if "成功" in rlt:
            break
        i += 1
    pass
