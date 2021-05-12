# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2021/5/12
    File Name: __init__.py
    Description:
        .
        ├── WeatherUI.py    UI设计与信号绑定
        ├── __init__.py     主函数启动
        ├── city_data.py    城市数据读取
        └── get_weather.py  获取城市天气

-------------------------------------------------
"""
import sys
import WeatherUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from city_data import *

if __name__ == '__main__':
    # data store
    storeCity()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/weather.png"))
    mainWindow = QMainWindow()
    ui = WeatherUI.WeatherUI()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
