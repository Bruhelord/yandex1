from PyQt5 import QtCore, QtGui, QtWidgets


class UiStartPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(501, 151)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 502, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_make_variant = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_make_variant.setFont(font)
        self.btn_make_variant.setObjectName("btn_make_variant")
        self.verticalLayout.addWidget(self.btn_make_variant)
        self.btn_open_history = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.btn_open_history.setFont(font)
        self.btn_open_history.setObjectName("btn_open_history")
        self.verticalLayout.addWidget(self.btn_open_history)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Главная"))
        self.btn_make_variant.setText(_translate("Dialog", "Составить вариант"))
        self.btn_open_history.setText(_translate("Dialog", "Открыть историю решений"))
