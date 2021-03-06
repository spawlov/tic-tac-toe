from PyQt6 import QtCore, QtGui, QtWidgets


class UiForm(object):
    def __init__(self):
        self.gridLayoutWidget_2 = None
        self.gridLayout_2 = None
        self.pBtn_1 = None
        self.pBtn_2 = None
        self.pBtn_3 = None
        self.pBtn_4 = None
        self.pBtn_5 = None
        self.pBtn_6 = None
        self.pBtn_7 = None
        self.pBtn_8 = None
        self.pBtn_9 = None
        self.pBtn_10 = None
        self.gridLayout = None
        self.gridLayoutWidget = None
        self.label = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(381, 402)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(381, 402))
        Form.setMaximumSize(QtCore.QSize(381, 402))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pBtn_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_10.sizePolicy().hasHeightForWidth())
        self.pBtn_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_10.setFont(font)
        self.pBtn_10.setObjectName("pBtn_10")
        self.gridLayout.addWidget(self.pBtn_10, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 361, 334))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pBtn_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_2.sizePolicy().hasHeightForWidth())
        self.pBtn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_2.setFont(font)
        self.pBtn_2.setObjectName("pBtn_2")
        self.gridLayout_2.addWidget(self.pBtn_2, 0, 1, 1, 1)
        self.pBtn_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_4.sizePolicy().hasHeightForWidth())
        self.pBtn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_4.setFont(font)
        self.pBtn_4.setObjectName("pBtn_4")
        self.gridLayout_2.addWidget(self.pBtn_4, 1, 0, 1, 1)
        self.pBtn_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_5.sizePolicy().hasHeightForWidth())
        self.pBtn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_5.setFont(font)
        self.pBtn_5.setObjectName("pBtn_5")
        self.gridLayout_2.addWidget(self.pBtn_5, 1, 1, 1, 1)
        self.pBtn_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_6.sizePolicy().hasHeightForWidth())
        self.pBtn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_6.setFont(font)
        self.pBtn_6.setObjectName("pBtn_6")
        self.gridLayout_2.addWidget(self.pBtn_6, 1, 2, 1, 1)
        self.pBtn_1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_1.sizePolicy().hasHeightForWidth())
        self.pBtn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_1.setFont(font)
        self.pBtn_1.setCheckable(False)
        self.pBtn_1.setChecked(False)
        self.pBtn_1.setAutoDefault(False)
        self.pBtn_1.setObjectName("pBtn_1")
        self.gridLayout_2.addWidget(self.pBtn_1, 0, 0, 1, 1)
        self.pBtn_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_3.sizePolicy().hasHeightForWidth())
        self.pBtn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_3.setFont(font)
        self.pBtn_3.setObjectName("pBtn_3")
        self.gridLayout_2.addWidget(self.pBtn_3, 0, 2, 1, 1)
        self.pBtn_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_7.sizePolicy().hasHeightForWidth())
        self.pBtn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_7.setFont(font)
        self.pBtn_7.setObjectName("pBtn_7")
        self.gridLayout_2.addWidget(self.pBtn_7, 2, 0, 1, 1)
        self.pBtn_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_8.sizePolicy().hasHeightForWidth())
        self.pBtn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_8.setFont(font)
        self.pBtn_8.setObjectName("pBtn_8")
        self.gridLayout_2.addWidget(self.pBtn_8, 2, 1, 1, 1)
        self.pBtn_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pBtn_9.sizePolicy().hasHeightForWidth())
        self.pBtn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn_9.setFont(font)
        self.pBtn_9.setObjectName("pBtn_9")
        self.gridLayout_2.addWidget(self.pBtn_9, 2, 2, 1, 1)

        self.re_translate_ui(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def re_translate_ui(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " "))
        self.pBtn_10.setText(_translate("Form", "??????????????"))
        self.pBtn_2.setText(_translate("Form", " "))
        self.pBtn_4.setText(_translate("Form", " "))
        self.pBtn_5.setText(_translate("Form", " "))
        self.pBtn_6.setText(_translate("Form", " "))
        self.pBtn_1.setText(_translate("Form", " "))
        self.pBtn_3.setText(_translate("Form", " "))
        self.pBtn_7.setText(_translate("Form", " "))
        self.pBtn_8.setText(_translate("Form", " "))
        self.pBtn_9.setText(_translate("Form", " "))
