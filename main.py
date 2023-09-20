# from utils import get_file_paths
# from compute import getLeadFail
# from compute import getHvsFail
#
# # paths = get_file_paths(r"C:\Users\pengcheng.yan\Desktop\work\aps日常统计\0915\0906")
# # for path in paths:
# #     getLeadFail(path)
#
# paths = get_file_paths(r"C:\Users\pengcheng.yan\Desktop\work\aps日常统计\0914\0913off")
# for path in paths:
#     getHvsFail(path)

# import subprocess
#
# command = 'ffmpeg -f dshow -i video="Sharing Camera" -vcodec h264 -acodec aac -f rtsp -rtsp_transport tcp rtsp://111.230.194.21/live/test'
#
# try:
#     subprocess.run(command, shell=True, check=True)
# except subprocess.CalledProcessError as e:
#     print('命令执行失败:', e)

import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

    def load(self, splash):
        for i in range(101):
            time.sleep(0.05)
            splash.showMessage(f'加载 {i}%', Qt.AlignBottom|Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication([])

    splash = QSplashScreen()      #注释1开始
    splash.setPixmap(QPixmap('qt.png'))
    splash.show()
    splash.showMessage('加载 0%', Qt.AlignBottom|Qt.AlignCenter)#注释1结束

    window = Window()
    window.load(splash)   #注释2开始
    window.show()
    splash.finish(window) #注释2结束
    sys.exit(app.exec())