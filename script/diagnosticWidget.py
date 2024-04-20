# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'diagnosticWidgetui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import settings

class DiagnosticWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(DiagnosticWidget, self).__init__(*args, **kwargs)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.input_on = QtWidgets.QLabel(self.frame_5)
        self.input_on.setAlignment(QtCore.Qt.AlignCenter)
        self.input_on.setStyleSheet("QLabel {\n"
"background-color: #ffff00;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"}`\n")
        self.input_on.setObjectName("input_on")
        self.horizontalLayout_8.addWidget(self.input_on)
        self.input_off = QtWidgets.QLabel(self.frame_5)
        self.input_off.setAlignment(QtCore.Qt.AlignCenter)
        self.input_off.setStyleSheet("QLabel {\n"
"background-color: #ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"}`\n")
        self.input_off.setObjectName("input_off")
        self.horizontalLayout_8.addWidget(self.input_off)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.diagnostic_state = QtWidgets.QPushButton(self.frame_5)
        self.diagnostic_state.setObjectName("diagnostic_state")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diagnostic_state.sizePolicy().hasHeightForWidth())
        self.diagnostic_state.setSizePolicy(sizePolicy)
        self.diagnostic_state.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.diagnostic_state.setStyleSheet(
            "QPushButton\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #DCDCDC;\n"
"}\n")
        self.horizontalLayout_8.addWidget(self.diagnostic_state)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.out_on = QtWidgets.QLabel(self.frame_5)
        self.out_on.setAlignment(QtCore.Qt.AlignCenter)
        self.out_on.setStyleSheet("QLabel {\n"
"background-color: #00bb00;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"color: #ffffff;"
"}\n")
        self.out_on.setObjectName("out_on")
        self.horizontalLayout_8.addWidget(self.out_on)
        self.out_off = QtWidgets.QLabel(self.frame_5)
        self.out_off.setAlignment(QtCore.Qt.AlignCenter)
        self.out_off.setStyleSheet("QLabel {\n"
"background-color: #bb0000;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"color: #ffffff;"
"}\n")
        self.out_off.setObjectName("out_off")
        self.horizontalLayout_8.addWidget(self.out_off)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.r1_state = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1_state.sizePolicy().hasHeightForWidth())
        self.r1_state.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r1_state.setFont(font)
        self.r1_state.setStyleSheet("QLabel{\n"
"    border-style: dashed;\n"
"    border-width: 3px;\n"
"    border-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 0, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.r1_state.setObjectName("r1_state")
        self.gridLayout.addWidget(self.r1_state, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.r2_state = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2_state.sizePolicy().hasHeightForWidth())
        self.r2_state.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r2_state.setFont(font)
        self.r2_state.setStyleSheet("QLabel{\n"
"    border-style: dashed;\n"
"    border-width: 3px;\n"
"    border-color: rgb(0, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"    border-radius: 8px;\n"
"}")
        self.r2_state.setObjectName("r2_state")
        self.gridLayout_2.addWidget(self.r2_state, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")


        self.setStyleSheet("QFrame{\n"
"   background-color: rgba(255, 255, 255, 0);\n"
"}\n")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setSpacing(4)
        self.r1p1 = QtWidgets.QLabel(self.frame)
        self.r1p1.setText("")
        self.r1p1.setObjectName("r1p1")
        self.verticalLayout.addWidget(self.r1p1)
        self.r1p3 = QtWidgets.QLabel(self.frame)
        self.r1p3.setText("")
        self.r1p3.setObjectName("r1p3")
        self.verticalLayout.addWidget(self.r1p3)
        self.r1p5 = QtWidgets.QLabel(self.frame)
        self.r1p5.setText("")
        self.r1p5.setObjectName("r1p5")
        self.verticalLayout.addWidget(self.r1p5)
        self.r1i1 = QtWidgets.QLabel(self.frame)
        self.r1i1.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i1.setObjectName("r1i1")
        self.verticalLayout.addWidget(self.r1i1)
        self.r1p9 = QtWidgets.QLabel(self.frame)
        self.r1p9.setText("")
        self.r1p9.setObjectName("r1p9")
        self.verticalLayout.addWidget(self.r1p9)
        self.r1i2 = QtWidgets.QLabel(self.frame)
        self.r1i2.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i2.setObjectName("r1i2")
        self.verticalLayout.addWidget(self.r1i2)
        self.r1i3 = QtWidgets.QLabel(self.frame)
        self.r1i3.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i3.setObjectName("r1i3")
        self.verticalLayout.addWidget(self.r1i3)
        self.r1i4 = QtWidgets.QLabel(self.frame)
        self.r1i4.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i4.setObjectName("r1i4")
        self.verticalLayout.addWidget(self.r1i4)
        self.r1p17 = QtWidgets.QLabel(self.frame)
        self.r1p17.setText("")
        self.r1p17.setObjectName("r1p17")
        self.verticalLayout.addWidget(self.r1p17)
        self.r1i5 = QtWidgets.QLabel(self.frame)
        self.r1i5.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i5.setObjectName("r1i5")
        self.verticalLayout.addWidget(self.r1i5)
        self.r1i6 = QtWidgets.QLabel(self.frame)
        self.r1i6.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i6.setObjectName("r1i6")
        self.verticalLayout.addWidget(self.r1i6)
        self.r1i7 = QtWidgets.QLabel(self.frame)
        self.r1i7.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i7.setObjectName("r1i7")
        self.verticalLayout.addWidget(self.r1i7)
        self.r1p25 = QtWidgets.QLabel(self.frame)
        self.r1p25.setText("")
        self.r1p25.setObjectName("r1p25")
        self.verticalLayout.addWidget(self.r1p25)
        self.r1p27 = QtWidgets.QLabel(self.frame)
        self.r1p27.setText("")
        self.r1p27.setObjectName("r1p27")
        self.verticalLayout.addWidget(self.r1p27)
        self.r1i8 = QtWidgets.QLabel(self.frame)
        self.r1i8.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i8.setObjectName("r1i8")
        self.verticalLayout.addWidget(self.r1i8)
        self.r1i9 = QtWidgets.QLabel(self.frame)
        self.r1i9.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i9.setObjectName("r1i9")
        self.verticalLayout.addWidget(self.r1i9)
        self.r1i10 = QtWidgets.QLabel(self.frame)
        self.r1i10.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i10.setObjectName("r1i10")
        self.verticalLayout.addWidget(self.r1i10)
        self.r1i11 = QtWidgets.QLabel(self.frame)
        self.r1i11.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i11.setObjectName("r1i11")
        self.verticalLayout.addWidget(self.r1i11)
        self.r1i12 = QtWidgets.QLabel(self.frame)
        self.r1i12.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i12.setObjectName("r1i12")
        self.verticalLayout.addWidget(self.r1i12)
        self.r1p39 = QtWidgets.QLabel(self.frame)
        self.r1p39.setText("")
        self.r1p39.setObjectName("r1p39")
        self.verticalLayout.addWidget(self.r1p39)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.r1 = QtWidgets.QLabel(self.frame)
        self.r1.setStyleSheet("")
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.r1.setPixmap(QtGui.QPixmap('img/GPIO.jpg'))
        self.r1.setScaledContents(True)
        self.horizontalLayout_2.addWidget(self.r1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_2.setSpacing(4)
        self.r1p2 = QtWidgets.QLabel(self.frame)
        self.r1p2.setText("")
        self.r1p2.setObjectName("r1p2")
        self.verticalLayout_2.addWidget(self.r1p2)
        self.r1p4 = QtWidgets.QLabel(self.frame)
        self.r1p4.setText("")
        self.r1p4.setObjectName("r1p4")
        self.verticalLayout_2.addWidget(self.r1p4)
        self.r1p6 = QtWidgets.QLabel(self.frame)
        self.r1p6.setText("")
        self.r1p6.setObjectName("r1p6")
        self.verticalLayout_2.addWidget(self.r1p6)
        self.r1i13 = QtWidgets.QLabel(self.frame)
        self.r1i13.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i13.setObjectName("r1i13")
        self.verticalLayout_2.addWidget(self.r1i13)
        self.r1i14 = QtWidgets.QLabel(self.frame)
        self.r1i14.setAlignment(QtCore.Qt.AlignCenter)
        self.r1i14.setObjectName("r1i14")
        self.verticalLayout_2.addWidget(self.r1i14)
        self.r1o1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o1.sizePolicy().hasHeightForWidth())
        self.r1o1.setSizePolicy(sizePolicy)
        self.r1o1.setObjectName("r1o1")
        self.verticalLayout_2.addWidget(self.r1o1)
        self.r1p14 = QtWidgets.QLabel(self.frame)
        self.r1p14.setText("")
        self.r1p14.setObjectName("r1p14")
        self.verticalLayout_2.addWidget(self.r1p14)
        self.r1o2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o2.sizePolicy().hasHeightForWidth())
        self.r1o2.setSizePolicy(sizePolicy)
        self.r1o2.setObjectName("r1o2")
        self.verticalLayout_2.addWidget(self.r1o2)
        self.r1o3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o3.sizePolicy().hasHeightForWidth())
        self.r1o3.setSizePolicy(sizePolicy)
        self.r1o3.setObjectName("r1o3")
        self.verticalLayout_2.addWidget(self.r1o3)
        self.r1p20 = QtWidgets.QLabel(self.frame)
        self.r1p20.setText("")
        self.r1p20.setObjectName("r1p20")
        self.verticalLayout_2.addWidget(self.r1p20)
        self.r1o4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o4.sizePolicy().hasHeightForWidth())
        self.r1o4.setSizePolicy(sizePolicy)
        self.r1o4.setObjectName("r1o4")
        self.verticalLayout_2.addWidget(self.r1o4)
        self.r1o5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o5.sizePolicy().hasHeightForWidth())
        self.r1o5.setSizePolicy(sizePolicy)
        self.r1o5.setObjectName("r1o5")
        self.verticalLayout_2.addWidget(self.r1o5)
        self.r1o6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r1o6.sizePolicy().hasHeightForWidth())
        self.r1o6.setSizePolicy(sizePolicy)
        self.r1o6.setObjectName("r1o6")
        self.verticalLayout_2.addWidget(self.r1o6)
        self.r1p28 = QtWidgets.QLabel(self.frame)
        self.r1p28.setText("")
        self.r1p28.setObjectName("r1p28")
        self.verticalLayout_2.addWidget(self.r1p28)
        self.r1p30 = QtWidgets.QLabel(self.frame)
        self.r1p30.setText("")
        self.r1p30.setObjectName("r1p30")
        self.verticalLayout_2.addWidget(self.r1p30)
        self.r1p32 = QtWidgets.QLabel(self.frame)
        self.r1p32.setAlignment(QtCore.Qt.AlignCenter)
        self.r1p32.setObjectName("r1p32")
        self.verticalLayout_2.addWidget(self.r1p32)
        self.r1p34 = QtWidgets.QLabel(self.frame)
        self.r1p34.setText("")
        self.r1p34.setObjectName("r1p34")
        self.verticalLayout_2.addWidget(self.r1p34)
        self.r1p36 = QtWidgets.QLabel(self.frame)
        self.r1p36.setAlignment(QtCore.Qt.AlignCenter)
        self.r1p36.setObjectName("r1p36")
        self.verticalLayout_2.addWidget(self.r1p36)
        self.r1p38 = QtWidgets.QLabel(self.frame)
        self.r1p38.setAlignment(QtCore.Qt.AlignCenter)
        self.r1p38.setObjectName("r1p38")
        self.verticalLayout_2.addWidget(self.r1p38)
        self.r1p40 = QtWidgets.QLabel(self.frame)
        self.r1p40.setAlignment(QtCore.Qt.AlignCenter)
        self.r1p40.setObjectName("r1p40")
        self.verticalLayout_2.addWidget(self.r1p40)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.r2p1 = QtWidgets.QLabel(self.frame_2)
        self.r2p1.setText("")
        self.r2p1.setObjectName("r2p1")
        self.verticalLayout_9.addWidget(self.r2p1)
        self.r2p3 = QtWidgets.QLabel(self.frame_2)
        self.r2p3.setText("")
        self.r2p3.setObjectName("r2p3")
        self.verticalLayout_9.addWidget(self.r2p3)
        self.r2p5 = QtWidgets.QLabel(self.frame_2)
        self.r2p5.setText("")
        self.r2p5.setObjectName("r2p5")
        self.verticalLayout_9.addWidget(self.r2p5)
        self.r2o7 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o7.sizePolicy().hasHeightForWidth())
        self.r2o7.setSizePolicy(sizePolicy)
        self.r2o7.setObjectName("r2o7")
        self.verticalLayout_9.addWidget(self.r2o7)
        self.r2p9 = QtWidgets.QLabel(self.frame_2)
        self.r2p9.setText("")
        self.r2p9.setObjectName("r2p9")
        self.verticalLayout_9.addWidget(self.r2p9)
        self.r2o8 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o8.sizePolicy().hasHeightForWidth())
        self.r2o8.setSizePolicy(sizePolicy)
        self.r2o8.setObjectName("r2o8")
        self.verticalLayout_9.addWidget(self.r2o8)
        self.r2o9 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o9.sizePolicy().hasHeightForWidth())
        self.r2o9.setSizePolicy(sizePolicy)
        self.r2o9.setObjectName("r2o9")
        self.verticalLayout_9.addWidget(self.r2o9)
        self.r2o10 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o10.sizePolicy().hasHeightForWidth())
        self.r2o10.setSizePolicy(sizePolicy)
        self.r2o10.setObjectName("r2o10")
        self.verticalLayout_9.addWidget(self.r2o10)
        self.r2p17 = QtWidgets.QLabel(self.frame_2)
        self.r2p17.setText("")
        self.r2p17.setObjectName("r2p17")
        self.verticalLayout_9.addWidget(self.r2p17)
        self.r2o11 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o11.sizePolicy().hasHeightForWidth())
        self.r2o11.setSizePolicy(sizePolicy)
        self.r2o11.setObjectName("r2o11")
        self.verticalLayout_9.addWidget(self.r2o11)
        self.r2o12 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o12.sizePolicy().hasHeightForWidth())
        self.r2o12.setSizePolicy(sizePolicy)
        self.r2o12.setObjectName("r2o12")
        self.verticalLayout_9.addWidget(self.r2o12)
        self.r2o13 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o13.sizePolicy().hasHeightForWidth())
        self.r2o13.setSizePolicy(sizePolicy)
        self.r2o13.setObjectName("r2o13")
        self.verticalLayout_9.addWidget(self.r2o13)
        self.r2p25 = QtWidgets.QLabel(self.frame_2)
        self.r2p25.setText("")
        self.r2p25.setObjectName("r2p25")
        self.verticalLayout_9.addWidget(self.r2p25)
        self.r2p27 = QtWidgets.QLabel(self.frame_2)
        self.r2p27.setText("")
        self.r2p27.setObjectName("r2p27")
        self.verticalLayout_9.addWidget(self.r2p27)
        self.r2o14 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o14.sizePolicy().hasHeightForWidth())
        self.r2o14.setSizePolicy(sizePolicy)
        self.r2o14.setObjectName("r2o14")
        self.verticalLayout_9.addWidget(self.r2o14)
        self.r2o15 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o15.sizePolicy().hasHeightForWidth())
        self.r2o15.setSizePolicy(sizePolicy)
        self.r2o15.setObjectName("r2o15")
        self.verticalLayout_9.addWidget(self.r2o15)
        self.r2o16 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o16.sizePolicy().hasHeightForWidth())
        self.r2o16.setSizePolicy(sizePolicy)
        self.r2o16.setObjectName("r2o16")
        self.verticalLayout_9.addWidget(self.r2o16)
        self.r2o17 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o17.sizePolicy().hasHeightForWidth())
        self.r2o17.setSizePolicy(sizePolicy)
        self.r2o17.setObjectName("r2o17")
        self.verticalLayout_9.addWidget(self.r2o17)
        self.r2o18 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o18.sizePolicy().hasHeightForWidth())
        self.r2o18.setSizePolicy(sizePolicy)
        self.r2o18.setObjectName("r2o18")
        self.verticalLayout_9.addWidget(self.r2o18)
        self.r2p39 = QtWidgets.QLabel(self.frame_2)
        self.r2p39.setText("")
        self.r2p39.setObjectName("r2p39")
        self.verticalLayout_9.addWidget(self.r2p39)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.r2 = QtWidgets.QLabel(self.frame_2)
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.r2.setPixmap(QtGui.QPixmap('img/GPIO.jpg'))
        self.r2.setScaledContents(True)
        self.horizontalLayout_5.addWidget(self.r2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_8.setSpacing(4)
        self.r2p2 = QtWidgets.QLabel(self.frame_2)
        self.r2p2.setText("")
        self.r2p2.setObjectName("r2p2")
        self.verticalLayout_8.addWidget(self.r2p2)
        self.r2p4 = QtWidgets.QLabel(self.frame_2)
        self.r2p4.setText("")
        self.r2p4.setObjectName("r2p4")
        self.verticalLayout_8.addWidget(self.r2p4)
        self.r2p6 = QtWidgets.QLabel(self.frame_2)
        self.r2p6.setText("")
        self.r2p6.setObjectName("r2p6")
        self.verticalLayout_8.addWidget(self.r2p6)
        self.r2o19 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o19.sizePolicy().hasHeightForWidth())
        self.r2o19.setSizePolicy(sizePolicy)
        self.r2o19.setObjectName("r2o19")
        self.verticalLayout_8.addWidget(self.r2o19)
        self.r2o20 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o20.sizePolicy().hasHeightForWidth())
        self.r2o20.setSizePolicy(sizePolicy)
        self.r2o20.setObjectName("r2o20")
        self.verticalLayout_8.addWidget(self.r2o20)
        self.r2o21 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2o21.sizePolicy().hasHeightForWidth())
        self.r2o21.setSizePolicy(sizePolicy)
        self.r2o21.setObjectName("r2o21")
        self.verticalLayout_8.addWidget(self.r2o21)
        self.r2p14 = QtWidgets.QLabel(self.frame_2)
        self.r2p14.setText("")
        self.r2p14.setObjectName("r2p14")
        self.verticalLayout_8.addWidget(self.r2p14)
        self.r2p16 = QtWidgets.QLabel(self.frame_2)
        self.r2p16.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p16.setObjectName("r2p16")
        self.verticalLayout_8.addWidget(self.r2p16)
        self.r2p18 = QtWidgets.QLabel(self.frame_2)
        self.r2p18.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p18.setObjectName("r2p18")
        self.verticalLayout_8.addWidget(self.r2p18)
        self.r2p20 = QtWidgets.QLabel(self.frame_2)
        self.r2p20.setText("")
        self.r2p20.setObjectName("r2p20")
        self.verticalLayout_8.addWidget(self.r2p20)
        self.r2p22 = QtWidgets.QLabel(self.frame_2)
        self.r2p22.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p22.setObjectName("r2p22")
        self.verticalLayout_8.addWidget(self.r2p22)
        self.r2p24 = QtWidgets.QLabel(self.frame_2)
        self.r2p24.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p24.setObjectName("r2p24")
        self.verticalLayout_8.addWidget(self.r2p24)
        self.r2p26 = QtWidgets.QLabel(self.frame_2)
        self.r2p26.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p26.setObjectName("r2p26")
        self.verticalLayout_8.addWidget(self.r2p26)
        self.r2p28 = QtWidgets.QLabel(self.frame_2)
        self.r2p28.setText("")
        self.r2p28.setObjectName("r2p28")
        self.verticalLayout_8.addWidget(self.r2p28)
        self.r2p30 = QtWidgets.QLabel(self.frame_2)
        self.r2p30.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p30.setObjectName("r2p30")
        self.verticalLayout_8.addWidget(self.r2p30)
        self.r2p32 = QtWidgets.QLabel(self.frame_2)
        self.r2p32.setText("")
        self.r2p32.setObjectName("r2p32")
        self.r2p32.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_8.addWidget(self.r2p32)
        self.r2p34 = QtWidgets.QLabel(self.frame_2)
        self.r2p34.setText("")
        self.r2p34.setObjectName("r2p34")
        self.verticalLayout_8.addWidget(self.r2p34)
        self.r2p36 = QtWidgets.QLabel(self.frame_2)
        self.r2p36.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p36.setObjectName("r2p36")
        self.verticalLayout_8.addWidget(self.r2p36)
        self.r2p38 = QtWidgets.QLabel(self.frame_2)
        self.r2p38.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p38.setObjectName("r2p38")
        self.verticalLayout_8.addWidget(self.r2p38)
        self.r2p40 = QtWidgets.QLabel(self.frame_2)
        self.r2p40.setAlignment(QtCore.Qt.AlignCenter)
        self.r2p40.setObjectName("r2p40")
        self.verticalLayout_8.addWidget(self.r2p40)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.status = False
        self.add_inputs()
        self.add_outs()
        self.add_not_using()
        self.disable_buttons()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def add_inputs(self):
        self.inputs = {
            'r1i1': self.r1i1,
            'r1i2': self.r1i2,
            'r1i3': self.r1i3,
            'r1i4': self.r1i4,
            'r1i5': self.r1i5,
            'r1i6': self.r1i6,
            'r1i7': self.r1i7,
            'r1i8': self.r1i8,
            'r1i9': self.r1i9,
            'r1i10': self.r1i10,
            'r1i11': self.r1i11,
            'r1i12': self.r1i12,
            'r1i13': self.r1i13,
            'r1i14': self.r1i14,
        }
        self.reset_inputs()

    def add_not_using(self):
        self.not_using = {
            'r1p32': self.r1p32,
            'r1p36': self.r1p36,
            'r1p38': self.r1p38,
            'r1p40': self.r1p40,
            'r2p16': self.r2p16,
            'r2p18': self.r2p18,
            'r2p22': self.r2p22,
            'r2p24': self.r2p24,
            'r2p26': self.r2p26,
            'r2p30': self.r2p32,
            'r2p36': self.r2p36,
            'r2p38': self.r2p38,
            'r2p40': self.r2p40,
        }

        for pin in self.not_using:
            self.not_using[pin].setStyleSheet("QLabel {\n"
"background-color: #ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"}`\n"
"")

    def add_outs(self):
        self.outs = {
            'r1o1': self.r1o1,
            'r1o2': self.r1o2,
            'r1o3': self.r1o3,
            'r1o4': self.r1o4,
            'r1o5': self.r1o5,
            'r1o6': self.r1o6,
            'r2o7': self.r2o7,
            'r2o8': self.r2o8,
            'r2o9': self.r2o9,
            'r2o10': self.r2o10,
            'r2o11': self.r2o11,
            'r2o12': self.r2o12,
            'r2o13': self.r2o13,
            'r2o14': self.r2o14,
            'r2o15': self.r2o15,
            'r2o16': self.r2o16,
            'r2o17': self.r2o17,
            'r2o18': self.r2o18,
            'r2o19': self.r2o19,
            'r2o20': self.r2o20,
            'r2o21': self.r2o21,
        }
        self.reset_outs()

    def reset_outs(self):
        for out in self.outs:
            if settings.outs[out] == settings.LOW:
                self.outs[out].setStyleSheet("QPushButton {\n"
"background-color: #00bb00;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"color: #ffffff;"
"}\n"
"QPushButton:hover {"
"    background-color: #00aa00;"
"}"
"QPushButton:pressed {"
"    background-color: #009900; "
"}")
            else:
                self.outs[out].setStyleSheet("QPushButton {\n"
"background-color: #bb0000;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"color: #ffffff;"
"}\n"
"QPushButton:hover {"
"    background-color: #aa0000;"
"}"
"QPushButton:pressed {"
"    background-color: #990000; "
"}")

    def reset_inputs(self):
        for input in self.inputs:
            if settings.inputs[input] == settings.HIGHT:
                self.inputs[input].setStyleSheet("QLabel {\n"
"background-color: #ffff00;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"}`\n"
"")
            else:
                self.inputs[input].setStyleSheet("QLabel {\n"
"background-color: #ffffff;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color:  #000000;\n"
"}`\n"
"")

    def disable_buttons(self):
        for out in self.outs:
            self.outs[out].setDisabled(True)

    def enable_buttons(self):
        for out in self.outs:
            self.outs[out].setDisabled(False)

    def disable_diagnostic(self):
        self.diagnostic_state.setDisabled(True)
        self.disable_buttons()
        settings.static_outs.clear()

    def enable_diagnostic(self):
        self.diagnostic_state.setDisabled(False)

    def bt_diagnostic_press(self):
        self.status = not self.status
        if self.status:
            self.enable_buttons()
            self.diagnostic_state.setText('Выключить ручное управление')
        else:
            self.disable_buttons()
            settings.static_outs.clear()
            self.diagnostic_state.setText('Включить ручное управление')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.input_on.setText(_translate("self", "Вход включен"))
        self.input_off.setText(_translate("self", "Вход отключен"))
        self.diagnostic_state.setText(_translate("self", "Включить ручное управление"))
        self.out_on.setText(_translate("self", "Выход включен"))
        self.out_off.setText(_translate("self", "Выход отключен"))
        self.r1_state.setText(_translate("self", "<b>Малинка 1 отключена"))
        self.r2_state.setText(_translate("self", "<b>Малинка 2 подключена"))
        self.r1i1.setText(_translate("self", "X1.1 Запускостановка игры"))
        self.r1i2.setText(_translate("self", "X1.2 Запуск сценария"))
        self.r1i3.setText(_translate("self", "X1.3 Остановка сценария"))
        self.r1i4.setText(_translate("self", "X1.4 Отключитьвключить звук"))
        self.r1i5.setText(_translate("self", "X1.5 Отключитьвключить осн. свет"))
        self.r1i6.setText(_translate("self", "X1.6 Сигнал \"R\" от КТ"))
        self.r1i7.setText(_translate("self", "X1.7Сигнал \"G\" от КТ"))
        self.r1i8.setText(_translate("self", "X1.8 Сигнал \"B\" от КТ"))
        self.r1i9.setText(_translate("self", "X1.9 Флаг забрали. База \"A\""))
        self.r1i10.setText(_translate("self", "X1.10 Флаг забрали. База \"B\""))
        self.r1i11.setText(_translate("self", "X1.11 Флаг принесли. База \"А\""))
        self.r1i12.setText(_translate("self", "X1.12 Флаг принесли. База \"B\""))
        self.r1i13.setText(_translate("self", "X1.13 Бомба заложена"))
        self.r1i14.setText(_translate("self", "X1.14 Бомба взорвана"))
        self.r1o1.setText(_translate("self", "Y1.1 Подсветка на столе"))
        self.r1o2.setText(_translate("self", "Y1.2 Красная подсветка A"))
        self.r1o3.setText(_translate("self", "Y1.3 Синяя подсветка A"))
        self.r1o4.setText(_translate("self", "Y1.4 Красная подсветка B"))
        self.r1o5.setText(_translate("self", "Y1.5 Синяя подсветка B"))
        self.r1o6.setText(_translate("self", "Y1.6 Админ свет"))
        self.r1p32.setText(_translate("self", "Не используется"))
        self.r1p36.setText(_translate("self", "Не используется"))
        self.r1p38.setText(_translate("self", "Не используется"))
        self.r1p40.setText(_translate("self", "Не используется"))
        self.r2o7.setText(_translate("self", "Y2.7 Подсветка зоны 1 W1"))
        self.r2o8.setText(_translate("self", "Y2.8 Подсветка зоны 1 TL1"))
        self.r2o9.setText(_translate("self", "Y2.9 Подсветка зоны 2 W2"))
        self.r2o10.setText(_translate("self", "Y2.10 Подсветка зоны 2 TL2"))
        self.r2o11.setText(_translate("self", "Y2.11 Подсветка зоны 3 W3"))
        self.r2o12.setText(_translate("self", "Y2.12 Подсветка зоны 3 TL3"))
        self.r2o13.setText(_translate("self", "Y2.13 Подсветка зоны 4 W4"))
        self.r2o14.setText(_translate("self", "Y2.14 Подсветка зоны 4 TL4"))
        self.r2o15.setText(_translate("self", "Y2.15 Подсветка кор.1 WK1"))
        self.r2o16.setText(_translate("self", "Y2.16 Подсветка кор.1 TLK1"))
        self.r2o17.setText(_translate("self", "Y2.17 Подсветка кор.2 WK2"))
        self.r2o18.setText(_translate("self", "Y2.18 Подсветка кор.2 TLK2"))
        self.r2o19.setText(_translate("self", "Y2.19 Свет в зоне выдачи LK1"))
        self.r2o20.setText(_translate("self", "Y2.20 Питание аптечки. База \"A\""))
        self.r2o21.setText(_translate("self", "Y2.21 Питание аптечки. База \"B\""))
        self.r2p16.setText(_translate("self", "Не используется"))
        self.r2p18.setText(_translate("self", "Не используется"))
        self.r2p22.setText(_translate("self", "Не используется"))
        self.r2p24.setText(_translate("self", "Не используется"))
        self.r2p26.setText(_translate("self", "Не используется"))
        self.r2p32.setText(_translate("self", "Не используется"))
        self.r2p36.setText(_translate("self", "Не используется"))
        self.r2p38.setText(_translate("self", "Не используется"))
        self.r2p40.setText(_translate("self", "Не используется"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = DiagnosticWidget()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())