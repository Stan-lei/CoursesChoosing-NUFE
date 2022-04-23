本程序可以初步实现南财教务通识课的自动化选课功能，仅供学习使用。
此外，由于各学校教务服务器均性能较差，本程序并不能保证可以抢到课。

【前提条件】
    1、需要保证已安装python；
    2、使用pip install selenium命令，安装selenium外部包；
    3、安装谷歌浏览器（具有同样内核的EDGE应该也可以）；
    4、安装并配置chromedriver；(https://www.cnblogs.com/lfri/p/10542797.html)
【使用说明】
    1、用excel打开courses.csv，在其中第一列输入合法的课程代码；
    2、运行course.py；（在cmd中键入python ./course.py）
    3、按照说明进行登录；
【注意事项】
    1、为保证能够正常选到课，请在开放选课前提前运行本程序；
    2、请妥善使用本程序，因使用不当造成的后果，由使用者自行承担。