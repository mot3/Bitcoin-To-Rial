# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bitcoin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BitCoin(object):
    def setupUi(self, BitCoin):
        BitCoin.setObjectName("BitCoin")
        BitCoin.setWindowModality(QtCore.Qt.NonModal)
        BitCoin.setEnabled(True)
        BitCoin.resize(228, 135)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BitCoin.sizePolicy().hasHeightForWidth())
        BitCoin.setSizePolicy(sizePolicy)
        BitCoin.setMinimumSize(QtCore.QSize(228, 135))
        BitCoin.setMaximumSize(QtCore.QSize(228, 135))
        BitCoin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        BitCoin.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconpath/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BitCoin.setWindowIcon(icon)
        BitCoin.setWindowFilePath("")
        BitCoin.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(BitCoin)
        self.centralwidget.setObjectName("centralwidget")
        self.bitcoin_price = QtWidgets.QLabel(self.centralwidget)
        self.bitcoin_price.setGeometry(QtCore.QRect(130, 90, 101, 21))
        self.bitcoin_price.setText("")
        self.bitcoin_price.setObjectName("bitcoin_price")
        self.get_price = QtWidgets.QPushButton(self.centralwidget)
        self.get_price.setGeometry(QtCore.QRect(150, 77, 70, 31))
        self.get_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_price.setObjectName("get_price")
        self.choose_price = QtWidgets.QComboBox(self.centralwidget)
        self.choose_price.setGeometry(QtCore.QRect(150, 10, 70, 22))
        self.choose_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_price.setObjectName("choose_price")
        self.choose_price.addItem("")
        self.choose_price.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(17, 10, 101, 20))
        self.label.setObjectName("label")
        self.show_price = QtWidgets.QLabel(self.centralwidget)
        self.show_price.setGeometry(QtCore.QRect(11, 84, 69, 13))
        self.show_price.setObjectName("show_price")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 61, 20))
        self.label_3.setObjectName("label_3")
        BitCoin.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(BitCoin)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        #self.menuBar.setVisible(False)
        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        BitCoin.setMenuBar(self.menuBar)
        self.actioncopy = QtWidgets.QAction(BitCoin)
        self.actioncopy.setObjectName("actioncopy")
        self.actiondelete = QtWidgets.QAction(BitCoin)
        self.actiondelete.setObjectName("actiondelete")
        self.actioncopy_2 = QtWidgets.QAction(BitCoin)
        self.actioncopy_2.setObjectName("actioncopy_2")
        self.actiondelete_2 = QtWidgets.QAction(BitCoin)
        self.actiondelete_2.setObjectName("actiondelete_2")
        self.menufile.addAction(self.actioncopy_2)
        self.menufile.addAction(self.actiondelete_2)
        self.menuBar.addAction(self.menufile.menuAction())

        self.retranslateUi(BitCoin)
        self.get_price.clicked.connect(self.get_price.showMenu)
        self.actioncopy_2.triggered.connect(self.show_price.clear)
        self.actiondelete_2.triggered.connect(self.show_price.clear)
        QtCore.QMetaObject.connectSlotsByName(BitCoin)

    def retranslateUi(self, BitCoin):
        _translate = QtCore.QCoreApplication.translate
        BitCoin.setWindowTitle(_translate("BitCoin", "BitCoin"))
        self.get_price.setText(_translate("BitCoin", "تبدیل"))
        self.choose_price.setItemText(0, _translate("BitCoin", "USD"))
        self.choose_price.setItemText(1, _translate("BitCoin", "EUR"))
        self.label.setText(_translate("BitCoin", "تبدیل کننده بیت کوین"))
        self.show_price.setText(_translate("BitCoin", "sfaf"))
        self.label_3.setText(_translate("BitCoin", "تبدیل شده:"))
        self.menufile.setTitle(_translate("BitCoin", "file"))
        self.actioncopy.setText(_translate("BitCoin", "copy"))
        self.actioncopy.setShortcut(_translate("BitCoin", "Ctrl+C"))
        self.actiondelete.setText(_translate("BitCoin", "delete"))
        self.actioncopy_2.setText(_translate("BitCoin", "copy"))
        self.actioncopy_2.setShortcut(_translate("BitCoin", "Ctrl+C"))
        self.actiondelete_2.setText(_translate("BitCoin", "delete"))
        self.actiondelete_2.setShortcut(_translate("BitCoin", "Ctrl+D"))
#import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BitCoin = QtWidgets.QMainWindow()
    ui = Ui_BitCoin()
    ui.setupUi(BitCoin)
    BitCoin.show()
    sys.exit(app.exec_())
