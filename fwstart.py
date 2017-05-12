# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fwstart.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import config_parser as CP
import start_fw
import os
import subprocess
from time import sleep
from dmrlogger import Syslogger
from dmrlogger import Filelogger

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FwStartWindow(QtGui.QWidget):
    def setupUi(self, FwStartWindow):
        FwStartWindow.setObjectName(_fromUtf8("FwStartWindow"))
        FwStartWindow.move(200,100)
        FwStartWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FwStartWindow.sizePolicy().hasHeightForWidth())
        FwStartWindow.setSizePolicy(sizePolicy)
        FwStartWindow.setMinimumSize(QtCore.QSize(800, 600))
        FwStartWindow.setMaximumSize(QtCore.QSize(800, 600))
        FwStartWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 236, 207);"))
        self.centralwidget = QtGui.QWidget(FwStartWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_con_set = QtGui.QPushButton(self.centralwidget)
        self.btn_con_set.setGeometry(QtCore.QRect(340, 430, 181, 50))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(490, 120, 301, 181))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_con_set.sizePolicy().hasHeightForWidth())
        self.btn_con_set.setSizePolicy(sizePolicy)
        self.btn_con_set.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_con_set.setAcceptDrops(False)
        self.btn_con_set.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_con_set.setObjectName(_fromUtf8("btn_con_set"))
        self.btn_loc_set = QtGui.QPushButton(self.centralwidget)
        self.btn_loc_set.setGeometry(QtCore.QRect(150, 430, 181, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_loc_set.sizePolicy().hasHeightForWidth())
        self.btn_loc_set.setSizePolicy(sizePolicy)
        self.btn_loc_set.setMinimumSize(QtCore.QSize(160, 50))
        self.btn_loc_set.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_loc_set.setObjectName(_fromUtf8("btn_loc_set"))
        self.lbl_error_start = QtGui.QLabel(self.centralwidget)
        self.lbl_error_start.setGeometry(QtCore.QRect(20, 260, 375, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbl_error_start.setFont(font)
        self.lbl_error_start.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_error_start.setText(_fromUtf8(""))
        self.lbl_error_start.setObjectName(_fromUtf8("lbl_error_start"))

        self.btn_kill_fw = QtGui.QPushButton(self.centralwidget)
        self.btn_kill_fw.setGeometry(QtCore.QRect(10, 300, 51, 50))
        self.btn_kill_fw.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_kill_fw.setAcceptDrops(False)
        self.btn_kill_fw.setStyleSheet(_fromUtf8("background-color: rgb(159, 173, 176);"))
        self.btn_kill_fw.setObjectName(_fromUtf8("btn_kill_fw"))
        self.btn_kill_fw.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 10, 571, 31))
        self.progressBar.setVisible(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.lbl_warning = QtGui.QLabel(self.frame)
        self.lbl_warning.setGeometry(QtCore.QRect(1, 1, 300, 180))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_warning.sizePolicy().hasHeightForWidth())
        self.lbl_warning.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl_warning.setFont(font)
        self.lbl_warning.setAutoFillBackground(False)
        self.lbl_warning.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_warning.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.lbl_warning.setObjectName(_fromUtf8("lbl_warning"))
        FwStartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FwStartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        FwStartWindow.setMenuBar(self.menubar)
        self.action_refresh = QtGui.QAction(FwStartWindow)
        self.action_refresh.setObjectName(_fromUtf8("action_refresh"))
        self.action_definitions = QtGui.QAction(FwStartWindow)
        self.action_definitions.setObjectName(_fromUtf8("action_definitions"))
        self.action_about = QtGui.QAction(FwStartWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_exit = QtGui.QAction(FwStartWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.menu_edit.addAction(self.action_refresh)
        self.menu_edit.addAction(self.action_exit)
        self.menu_help.addAction(self.action_definitions)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.auto_refresh)

        self.def_window = None
        self.about_window = None


        self.retranslateUi(FwStartWindow)
        self.child = False
        self.old_config = {}
        self.active_user = "None"
        self.current_user = "None"

        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"
        with open(full_path+"current_user.dmr","r") as current_user:
            self.active_user = current_user.readline()
        self.full_path = full_path
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)

        #stylesheets
        FwStartWindow.setStyleSheet(_fromUtf8("QMainWindow#FwStartWindow {border-image: url("+full_path+"img/ahtapot_logo.png);}"))

        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), exit)
        QtCore.QObject.connect(self.action_refresh, QtCore.SIGNAL(_fromUtf8("triggered()")), self.refresh_method)
        QtCore.QObject.connect(self.action_definitions, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_def_window)
        QtCore.QObject.connect(self.action_about, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_about_window)


        QtCore.QObject.connect(self.btn_loc_set, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_fwbuilder)
        QtCore.QObject.connect(self.btn_con_set, QtCore.SIGNAL(_fromUtf8("clicked()")), self.load_new_rules)
        QtCore.QObject.connect(self.btn_kill_fw, QtCore.SIGNAL(_fromUtf8("clicked()")), self.kill_all)

        QtCore.QMetaObject.connectSlotsByName(FwStartWindow)



    def retranslateUi(self, FwStartWindow):
        FwStartWindow.setWindowTitle(_translate("FwStartWindow", " Ahtapot - GDYS", None))
        self.btn_con_set.setText(_translate("FwStartWindow", "Derlenmiş Ayarlar\n"
"    ile Çalıştır", None))
        self.btn_loc_set.setText(_translate("FwStartWindow", "Yerel Ayarlar \n"
"  ile Çalıştır", None))
        self.btn_kill_fw.setText(_translate("FwStartWindow", "Sonlandır", None))
        self.lbl_warning.setText(_translate("FwStartWindow", "<p>Derlenmiş Ayarlar ile Çalıştır<br/>butonu Yerel Ayarların üzerine<br/> yazar!!!.</p>", None))
        self.menu_edit.setTitle(_translate("FwStartWindow", "Düzenle", None))
        self.menu_help.setTitle(_translate("FwStartWindow", "Yardım", None))
        self.action_refresh.setText(_translate("FwStartWindow", "Yenile", None))
        self.action_refresh.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.action_definitions.setText(_translate("FwStartWindow", "Açıklamalar", None))
        self.action_definitions.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.action_about.setText(_translate("FwStartWindow", "Hakkında", None))
        self.action_about.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.action_exit.setText(_translate("FwStartWindow", "Çıkış", None))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.timer.start(3000)

    def set_windows(self,old,new):
        self.old_window = old
        self.new_window = new

    def show_def_window(self):
        self.def_window.show()

    def show_about_window(self):
        self.about_window.show()

    def set_error_message(self,message):
        self.lbl_error_start.setText(message)

    def start_fwbuilder(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        self.lbl_error_start.setText("<p></p>")
        if start_fw.check_if_runs() == False:
            with open(self.full_path + "current_user.dmr", "w") as current_user:
                current_user.write(self.current_user)
            fw_path = CP.get_configs()["fw_path"]
            start_fw.start_fwbuilder()
            self.logger.send_log("info"," Firewall Builder Started with Local settings")
            self.filelogger.send_log("info"," Firewall Builder Started with Local settings")
        else:
            self.warn_if_fw_runs()
            subprocess.call(["xdotool search --name \"Firewall Builder\" windowactivate windowsize 90\% 90\%"],shell=True)

    def refresh_method(self):
        self.progressBar.setVisible(True)
        self.centralwidget.setEnabled(False)
        self.set_progressbar()
        self.lbl_error_start.setText(u"<p></p>")
        self.warn_if_fw_runs()
        self.centralwidget.setEnabled(True)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)
  
    def pull_repo(self):
        fw_path = CP.get_configs()["fw_path"]
        fwb_file_name = CP.get_configs()["fwb_file_name"]
        cmd_git_pull = "cd "+fw_path + "&& git pull"
        cmd_git_checkout = "cd " + fw_path + "&& git checkout " + fwb_file_name
        subprocess.call([cmd_git_checkout],shell=True)
        subprocess.call([cmd_git_pull],shell=True)
        start_fw.kill_fw()
        fw_path = CP.get_configs()["fw_path"]
        start_fw.start_fwbuilder()

    def load_new_rules(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        self.lbl_error_start.setText("<p></p>")
        if start_fw.check_if_runs() is True:
            self.warn_if_fw_runs()
        else:
            self.progressBar.setVisible(True)
            self.centralwidget.setEnabled(False)
            self.set_progressbar()
            abs_path = os.path.abspath(__file__)
            path_list = abs_path.split("/")
            del path_list[-1]
            path_name = "/".join(path_list)
            full_path = path_name + "/"
            self.pull_repo()
            self.logger.send_log("warning", " Rule Settings pulled from Master and Firewall Builder Started")
            self.filelogger.send_log("warning", " Rule Settings pulled from Master and Firewall Builder Started")
            self.centralwidget.setEnabled(True)
            self.progressBar.setValue(0)
            self.progressBar.setVisible(False)

    def set_progressbar(self):
        self.progressBar.setValue(30)
        sleep(1)
        self.progressBar.setValue(60)
        sleep(1)
        self.progressBar.setValue(100)

    def warn_if_fw_runs(self):
        if start_fw.check_if_runs() == True:
            with open(self.full_path + "current_user.dmr", "r") as active_user:
                self.active_user = active_user.readline()
            self.lbl_error_start.setText(u"<b>UYARI:</b> Şuan kullanılan başka bir Firewall Builder mevcut.<br/><b>Kullanıcı : </b>" + self.active_user)
            self.btn_kill_fw.setEnabled(True)
            self.btn_con_set.setEnabled(False)
        else:
            self.btn_kill_fw.setEnabled(False)

    def auto_refresh(self):
        self.centralwidget.setEnabled(False)
        self.lbl_error_start.setText(u"<p></p>")
        self.auto_check_and_refresh()
        self.warn_if_fw_runs()
        self.centralwidget.setEnabled(True)

    def auto_check_and_refresh(self):
        new_config = CP.get_configs()

        self.lbl_error_start.setText("")
        self.btn_con_set.setEnabled(True)
        self.btn_loc_set.setEnabled(True)
        self.warn_if_fw_runs()
        return True

    def kill_all(self):
        self.logger = Syslogger("FWBUILDER-AHTAPOT",'%(name)s %(levelname)s %(message)s',"/dev/log", self.current_user)
        self.filelogger = Filelogger("FWBUILDER-AHTAPOT",'%(asctime)s %(name)s %(levelname)s %(message)s',"/var/log/ahtapot/gdys-gui.log","a",self.current_user)
        start_fw.kill_fw()
        try:
            start_fw.kill_gui_user(self.current_user)
        except Exception as e :
            self.filelogger.send_log("error", "Error While Killing Previous GUI {}".format(str(e)))
        abs_path = os.path.abspath(__file__)
        path_list = abs_path.split("/")
        del path_list[-1]
        path_name="/".join(path_list)
        full_path = path_name + "/"
        with open(full_path + "current_user.dmr", "w") as current_user:
            current_user.write(self.current_user)
        self.filelogger.send_log("warning", " previous gui was killed by " + self.current_user + " : gui ")
        self.btn_kill_fw.setEnabled(False)
        sleep(2)
        self.load_new_rules()
        sleep(3)
        self.auto_refresh()
        self.lbl_error_start.setText(u"<b>SONLANDIRILDI</b>")
