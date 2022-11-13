from PyQt5 import QtCore, QtGui, QtWidgets


class UiTaskPage(object):
    def setupUi(self, dialog):
        dialog.setObjectName("задача")
        dialog.resize(449, 285)
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_task = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_task.setFont(font)
        self.lbl_task.setAutoFillBackground(False)
        self.lbl_task.setObjectName("task")
        self.verticalLayout.addWidget(self.lbl_task)
        self.lineEditAnswer = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditAnswer.setFont(font)
        self.lineEditAnswer.setObjectName("lineEditAnswer")
        self.verticalLayout.addWidget(self.lineEditAnswer)
        self.btn_send_a_reply = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_send_a_reply.setFont(font)
        self.btn_send_a_reply.setObjectName("btn_send_a_reply")
        self.verticalLayout.addWidget(self.btn_send_a_reply)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Вариант"))
        self.lbl_task.setText(_translate("dialog", "TextLabel"))
        self.lineEditAnswer.setPlaceholderText(_translate("dialog", "Ответ:"))
        self.btn_send_a_reply.setText(_translate("dialog", "Сохранить ответ"))



