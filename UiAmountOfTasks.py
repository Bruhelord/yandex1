from PyQt5 import QtCore, QtGui, QtWidgets


class UiAmountOfTasks(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 243)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox_amount_of_tasks = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_amount_of_tasks.setFont(font)
        self.spinBox_amount_of_tasks.setMinimum(5)
        self.spinBox_amount_of_tasks.setMaximum(15)
        self.spinBox_amount_of_tasks.setObjectName("spinBox_amount_of_tasks")
        self.verticalLayout.addWidget(self.spinBox_amount_of_tasks)
        self.btn_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_start.setFont(font)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "Количество заданий:"))
        self.btn_start.setText(_translate("Dialog", "Перейти к решению варианта"))
