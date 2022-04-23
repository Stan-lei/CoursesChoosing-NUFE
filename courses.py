"""
Author: Stanlei
Create date: 2022/04/23
Github: https://github.com/Stan-lei
version: 0.2
feather: 初步实现了登录自动化与抢课自动化
"""
import re
import sched

from utls import *
from selenium import webdriver


def print_info() -> None:
    print("**********************************************\n"
          "Author: Stanlei\n"
          "Create date: 2022/04/23\n"
          "Github: https://github.com/Stan-lei\n"
          "version: 0.2\n"
          "feather: 初步实现了登录自动化与抢课自动化\n"
          "**********************************************\n")


if __name__ == "__main__":
    print_info()
    hint()
    browser = webdriver.Chrome()
    browser.get("http://210.28.81.11/")
    login(browser)

    goto_choose_courses(browser)
    batch(browser)
    browser.quit()

    print("hello world!", read_courses())
