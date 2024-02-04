# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 804)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.start_btn = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.start_btn.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setBold(True)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(21, 181, 34);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(22, 131, 35);\n"
"}\n"
"")
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout_4.addWidget(self.start_btn)
        self.check_btn = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_btn.sizePolicy().hasHeightForWidth())
        self.check_btn.setSizePolicy(sizePolicy)
        self.check_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.check_btn.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setBold(True)
        self.check_btn.setFont(font)
        self.check_btn.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(42, 42, 193);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(19, 32, 150);\n"
"}\n"
"\n"
"\n"
"")
        self.check_btn.setObjectName("check_btn")
        self.verticalLayout_4.addWidget(self.check_btn)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setLineWidth(0)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Pesron1 = QtWidgets.QCheckBox(self.frame_12)
        self.Pesron1.setObjectName("Pesron1")
        self.verticalLayout_8.addWidget(self.Pesron1)
        self.Pesron2 = QtWidgets.QCheckBox(self.frame_12)
        self.Pesron2.setObjectName("Pesron2")
        self.verticalLayout_8.addWidget(self.Pesron2)
        self.Pesron3 = QtWidgets.QCheckBox(self.frame_12)
        self.Pesron3.setObjectName("Pesron3")
        self.verticalLayout_8.addWidget(self.Pesron3)
        self.Pesron4 = QtWidgets.QCheckBox(self.frame_12)
        self.Pesron4.setObjectName("Pesron4")
        self.verticalLayout_8.addWidget(self.Pesron4)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Pesron5 = QtWidgets.QCheckBox(self.frame_13)
        self.Pesron5.setObjectName("Pesron5")
        self.verticalLayout_7.addWidget(self.Pesron5)
        self.Pesron6 = QtWidgets.QCheckBox(self.frame_13)
        self.Pesron6.setObjectName("Pesron6")
        self.verticalLayout_7.addWidget(self.Pesron6)
        self.Pesron7 = QtWidgets.QCheckBox(self.frame_13)
        self.Pesron7.setObjectName("Pesron7")
        self.verticalLayout_7.addWidget(self.Pesron7)
        self.Pesron8 = QtWidgets.QCheckBox(self.frame_13)
        self.Pesron8.setObjectName("Pesron8")
        self.verticalLayout_7.addWidget(self.Pesron8)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SpectrogramBox = QtWidgets.QGroupBox(self.frame_6)
        self.SpectrogramBox.setEnabled(True)
        self.SpectrogramBox.setMinimumSize(QtCore.QSize(0, 0))
        self.SpectrogramBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SpectrogramBox.setAutoFillBackground(False)
        self.SpectrogramBox.setStyleSheet("")
        self.SpectrogramBox.setFlat(False)
        self.SpectrogramBox.setCheckable(False)
        self.SpectrogramBox.setObjectName("SpectrogramBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.SpectrogramBox)
        self.gridLayout_13.setContentsMargins(-1, -1, -1, 2)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.Spectrogram_1 = QtWidgets.QVBoxLayout()
        self.Spectrogram_1.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.Spectrogram_1.setSpacing(0)
        self.Spectrogram_1.setObjectName("Spectrogram_1")
        self.gridLayout_14.addLayout(self.Spectrogram_1, 0, 0, 1, 2)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.SpectrogramBox)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(1)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.openLabel = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.openLabel.setFont(font)
        self.openLabel.setText("")
        self.openLabel.setObjectName("openLabel")
        self.horizontalLayout_5.addWidget(self.openLabel)
        self.verticalLayout_9.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.grantLabel = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.grantLabel.setFont(font)
        self.grantLabel.setText("")
        self.grantLabel.setObjectName("grantLabel")
        self.horizontalLayout_6.addWidget(self.grantLabel)
        self.verticalLayout_9.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.unlockLabel = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.unlockLabel.setFont(font)
        self.unlockLabel.setText("")
        self.unlockLabel.setObjectName("unlockLabel")
        self.horizontalLayout_7.addWidget(self.unlockLabel)
        self.verticalLayout_9.addWidget(self.frame_16)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setLineWidth(1)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_17 = QtWidgets.QFrame(self.frame_9)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setLineWidth(0)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.omarLabel = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.omarLabel.setFont(font)
        self.omarLabel.setText("")
        self.omarLabel.setObjectName("omarLabel")
        self.horizontalLayout_8.addWidget(self.omarLabel)
        self.verticalLayout_10.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.hazemLabel = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hazemLabel.setFont(font)
        self.hazemLabel.setText("")
        self.hazemLabel.setObjectName("hazemLabel")
        self.horizontalLayout_11.addWidget(self.hazemLabel)
        self.verticalLayout_10.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_17)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_17 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.ibrahimLabel = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ibrahimLabel.setFont(font)
        self.ibrahimLabel.setText("")
        self.ibrahimLabel.setObjectName("ibrahimLabel")
        self.horizontalLayout_12.addWidget(self.ibrahimLabel)
        self.verticalLayout_10.addWidget(self.frame_20)
        self.verticalLayout_11.addWidget(self.frame_17)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        self.result_label_3 = QtWidgets.QLabel(self.frame)
        self.result_label_3.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.result_label_3.setFont(font)
        self.result_label_3.setStyleSheet("color: rgb(220, 0, 4);")
        self.result_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_3.setObjectName("result_label_3")
        self.verticalLayout.addWidget(self.result_label_3)
        self.result_label_1 = QtWidgets.QLabel(self.frame)
        self.result_label_1.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.result_label_1.setFont(font)
        self.result_label_1.setStyleSheet("color: rgb(220, 0, 4);")
        self.result_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_1.setObjectName("result_label_1")
        self.verticalLayout.addWidget(self.result_label_1)
        self.result_label_2 = QtWidgets.QLabel(self.frame)
        self.result_label_2.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.result_label_2.setFont(font)
        self.result_label_2.setStyleSheet("color: rgb(220, 0, 4);")
        self.result_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_2.setObjectName("result_label_2")
        self.verticalLayout.addWidget(self.result_label_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionUniform_Range_Mode = QtWidgets.QAction(MainWindow)
        self.actionUniform_Range_Mode.setCheckable(True)
        self.actionUniform_Range_Mode.setChecked(True)
        self.actionUniform_Range_Mode.setObjectName("actionUniform_Range_Mode")
        self.actionMusical_Instruments_Mode = QtWidgets.QAction(MainWindow)
        self.actionMusical_Instruments_Mode.setCheckable(True)
        self.actionMusical_Instruments_Mode.setObjectName("actionMusical_Instruments_Mode")
        self.actionAnimals_Sound_Mode = QtWidgets.QAction(MainWindow)
        self.actionAnimals_Sound_Mode.setCheckable(True)
        self.actionAnimals_Sound_Mode.setObjectName("actionAnimals_Sound_Mode")
        self.actionECG_Mode = QtWidgets.QAction(MainWindow)
        self.actionECG_Mode.setCheckable(True)
        self.actionECG_Mode.setObjectName("actionECG_Mode")
        self.actionCall_3asfoor = QtWidgets.QAction(MainWindow)
        self.actionCall_3asfoor.setObjectName("actionCall_3asfoor")
        self.actionPlay_Input = QtWidgets.QAction(MainWindow)
        self.actionPlay_Input.setCheckable(False)
        self.actionPlay_Input.setChecked(False)
        self.actionPlay_Input.setObjectName("actionPlay_Input")
        self.actionPlay_Output = QtWidgets.QAction(MainWindow)
        self.actionPlay_Output.setObjectName("actionPlay_Output")
        self.actionPlay_Input_2 = QtWidgets.QAction(MainWindow)
        self.actionPlay_Input_2.setObjectName("actionPlay_Input_2")
        self.actionPlay_Output_2 = QtWidgets.QAction(MainWindow)
        self.actionPlay_Output_2.setObjectName("actionPlay_Output_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "Start Recording"))
        self.check_btn.setText(_translate("MainWindow", "Check Permission"))
        self.Pesron1.setText(_translate("MainWindow", "Ibrahim"))
        self.Pesron2.setText(_translate("MainWindow", "Omar"))
        self.Pesron3.setText(_translate("MainWindow", "Hazem"))
        self.Pesron4.setText(_translate("MainWindow", "Ahmed Ali"))
        self.Pesron5.setText(_translate("MainWindow", "Mohannad"))
        self.Pesron6.setText(_translate("MainWindow", "Hassan"))
        self.Pesron7.setText(_translate("MainWindow", "Ahmed K"))
        self.Pesron8.setText(_translate("MainWindow", "Abdo"))
        self.SpectrogramBox.setTitle(_translate("MainWindow", "Spectrogram"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Open Middle Door:"))
        self.label_5.setText(_translate("MainWindow", "Grant Me Access:"))
        self.label_7.setText(_translate("MainWindow", "Unlock The Gate:"))
        self.label_4.setText(_translate("MainWindow", "Person"))
        self.label_9.setText(_translate("MainWindow", "Omar:"))
        self.label_15.setText(_translate("MainWindow", "Hazem:"))
        self.label_17.setText(_translate("MainWindow", "Ibrahim:"))
        self.result_label_3.setText(_translate("MainWindow", "-"))
        self.result_label_1.setText(_translate("MainWindow", "-"))
        self.result_label_2.setText(_translate("MainWindow", "-"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionUniform_Range_Mode.setText(_translate("MainWindow", "Uniform Range Mode"))
        self.actionMusical_Instruments_Mode.setText(_translate("MainWindow", "Musical Instruments Mode"))
        self.actionAnimals_Sound_Mode.setText(_translate("MainWindow", "Animals Sound Mode"))
        self.actionECG_Mode.setText(_translate("MainWindow", "ECG Mode"))
        self.actionCall_3asfoor.setText(_translate("MainWindow", "Call 3asfoor"))
        self.actionPlay_Input.setText(_translate("MainWindow", "Play Input"))
        self.actionPlay_Output.setText(_translate("MainWindow", "Play Output"))
        self.actionPlay_Input_2.setText(_translate("MainWindow", "Play Input"))
        self.actionPlay_Output_2.setText(_translate("MainWindow", "Play Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
