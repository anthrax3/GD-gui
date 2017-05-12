#!/usr/bin/env python
#coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import  fwstart, fwstartdef, fwabout
from time import sleep
import start_fw
import config_parser as CP
import os
import time


class MovieSplashScreen(QtGui.QSplashScreen):
     def __init__(self, movie, parent = None):
        movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(movie.frameRect().size())
        QtGui.QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
     def showEvent(self, event):
        self.movie.start()

     def hideEvent(self, event):
        self.movie.stop()

     def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
     def sizeHint(self):
        return self.movie.scaledSize()

if __name__ == "__main__":
    import sys

    args = sys.argv
    active_user = ""
    if len(args) == 1:
        active_user = "BilgiYok"
    elif len(args) == 2:
        active_user = args[1]
    else:
        active_user = "BilgiYok"



    app = QtGui.QApplication(sys.argv)
    abs_path = os.path.abspath(__file__)
    path_list = abs_path.split("/")
    del path_list[-1]
    path_name="/".join(path_list)
    full_path = path_name + "/"

    app.setWindowIcon(QtGui.QIcon(full_path + "img/" + 'ahtapot_icon.png'))

    movie = QtGui.QMovie(full_path+"img/"+"splash.gif")
    splash = MovieSplashScreen(movie)
    splash.show()
    #app.aboutToQuit.connect(start_fw.kill_fw)

    #for commit message
    if start_fw.check_if_runs() is False:
        with open(full_path + "current_user.dmr", "w") as current_user:
            current_user.write(active_user)

    FwStartWindow = QtGui.QMainWindow()
    ui_start = fwstart.Ui_FwStartWindow()
    ui_start.setupUi(FwStartWindow)

    FwStartDefWindow = QtGui.QMainWindow()
    ui_start_def = fwstartdef.Ui_Form()
    ui_start_def.setupUi(FwStartDefWindow)

    FwAboutWindow = QtGui.QMainWindow()
    ui_about = fwabout.Ui_Form()
    ui_about.setupUi(FwAboutWindow)

    ui_start.def_window = FwStartDefWindow
    ui_start.about_window = FwAboutWindow


    ui_start.current_user = active_user


    start = time.time()

    while movie.state() == QtGui.QMovie.Running and time.time() < start + 3 :
        app.processEvents()

    ui_start.logger.send_log("info"," GUI Started")
    ui_start.filelogger.send_log("info"," GUI Started")
    FwStartWindow.show()
    splash.finish(ui_start)
    sys.exit(app.exec_())
