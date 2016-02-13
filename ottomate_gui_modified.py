

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow:

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 645)


        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 1261, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.insertBreaksGroupBox = QtWidgets.QGroupBox(self.frame)
        self.insertBreaksGroupBox.setGeometry(QtCore.QRect(10, 10, 391, 161))
        self.insertBreaksGroupBox.setObjectName("insertBreaksGroupBox")

        self.insertBreaksTime = QtWidgets.QDoubleSpinBox(self.insertBreaksGroupBox)
        self.insertBreaksTime.setGeometry(QtCore.QRect(70, 30, 131, 22))
        self.insertBreaksTime.setObjectName("insertBreaksTime")

        self.insertBreaksGo = QtWidgets.QCommandLinkButton(self.insertBreaksGroupBox)
        self.insertBreaksGo.setGeometry(QtCore.QRect(260, 20, 111, 41))
        self.insertBreaksGo.setObjectName("insertBreaksGo")
        
        self.insertBreaksAdvGo = QtWidgets.QCommandLinkButton(self.insertBreaksGroupBox)
        self.insertBreaksAdvGo.setGeometry(QtCore.QRect(260, 94, 111, 41))
        self.insertBreaksAdvGo.setObjectName("insertBreaksAdvGo")
        
        self.line_2 = QtWidgets.QFrame(self.insertBreaksGroupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 361, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.insertBreaksAdvRadio01 = QtWidgets.QRadioButton(self.insertBreaksGroupBox)
        self.insertBreaksAdvRadio01.setGeometry(QtCore.QRect(30, 80, 151, 20))
        self.insertBreaksAdvRadio01.setObjectName("insertBreaksAdvRadio01")

        self.insertBreaksAdvRadio02 = QtWidgets.QRadioButton(self.insertBreaksGroupBox)
        self.insertBreaksAdvRadio02.setGeometry(QtCore.QRect(30, 105, 151, 20))
        self.insertBreaksAdvRadio02.setObjectName("insertBreaksAdvRadio02")

        self.insertBreaksAdvRadio03 = QtWidgets.QRadioButton(self.insertBreaksGroupBox)
        self.insertBreaksAdvRadio03.setGeometry(QtCore.QRect(30, 130, 151, 20))
        self.insertBreaksAdvRadio03.setObjectName("insertBreaksAdvRadio03")

        self.insertBreaksAdvOptions = QtWidgets.QToolButton(self.insertBreaksGroupBox)
        self.insertBreaksAdvOptions.setGeometry(QtCore.QRect(200, 130, 27, 22))
        self.insertBreaksAdvOptions.setObjectName("insertBreaksAdvOptions")

        self.insertTextGroupBox = QtWidgets.QGroupBox(self.frame)
        self.insertTextGroupBox.setGeometry(QtCore.QRect(10, 170, 391, 111))
        self.insertTextGroupBox.setObjectName("insertTextGroupBox")

        self.insertTextField = QtWidgets.QTextEdit(self.insertTextGroupBox)
        self.insertTextField.setGeometry(QtCore.QRect(30, 34, 211, 50))
        self.insertTextField.setObjectName("insertTextField")

        self.insertTextGo = QtWidgets.QCommandLinkButton(self.insertTextGroupBox)
        self.insertTextGo.setGeometry(QtCore.QRect(260, 39, 111, 41))
        self.insertTextGo.setObjectName("insertTextGo")

        self.insertKeystrokeGroupBox = QtWidgets.QGroupBox(self.frame)
        self.insertKeystrokeGroupBox.setGeometry(QtCore.QRect(10, 280, 391, 100))
        self.insertKeystrokeGroupBox.setObjectName("insertKeystrokeGroupBox")

        self.insertKeystrokeOptions = QtWidgets.QComboBox(self.insertKeystrokeGroupBox)
        self.insertKeystrokeOptions.setGeometry(QtCore.QRect(30, 63, 211, 22))
        self.insertKeystrokeOptions.setObjectName("insertKeystrokeOptions")
        self.insertKeystrokeOptions.addItem("")
        self.insertKeystrokeOptions.addItem("")
        self.insertKeystrokeOptions.addItem("")

        self.insertKeystrokeField = QtWidgets.QTextEdit(self.insertKeystrokeGroupBox)
        self.insertKeystrokeField.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.insertKeystrokeField.setObjectName("insertKeystrokeField")

        self.insertKeystrokeGo = QtWidgets.QCommandLinkButton(self.insertKeystrokeGroupBox)
        self.insertKeystrokeGo.setGeometry(QtCore.QRect(260, 32, 111, 41))
        self.insertKeystrokeGo.setObjectName("insertKeystrokeGo")

        self.insertMouseGroupBox = QtWidgets.QGroupBox(self.frame)
        self.insertMouseGroupBox.setGeometry(QtCore.QRect(10, 380, 391, 170))
        self.insertMouseGroupBox.setObjectName("insertMouseGroupBox")

        self.insertMouseRadio01 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio01.setGeometry(QtCore.QRect(20, 26, 95, 20))
        self.insertMouseRadio01.setObjectName("insertMouseRadio01")

        self.insertMouseRadio02 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio02.setGeometry(QtCore.QRect(20, 46, 95, 20))
        self.insertMouseRadio02.setObjectName("insertMouseRadio02")

        self.insertMouseRadio03 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio03.setGeometry(QtCore.QRect(20, 66, 95, 20))
        self.insertMouseRadio03.setObjectName("insertMouseRadio03")

        self.insertMouseRadio04 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio04.setGeometry(QtCore.QRect(140, 26, 95, 20))
        self.insertMouseRadio04.setObjectName("insertMouseRadio04")

        self.insertMouseRadio05 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio05.setGeometry(QtCore.QRect(140, 46, 95, 20))
        self.insertMouseRadio05.setObjectName("insertMouseRadio05")

        self.insertMouseRadio06 = QtWidgets.QRadioButton(self.insertMouseGroupBox)
        self.insertMouseRadio06.setGeometry(QtCore.QRect(20, 100, 121, 20))
        self.insertMouseRadio06.setObjectName("insertMouseRadio06")

        self.insertMouseXYHotkey = QtWidgets.QKeySequenceEdit(self.insertMouseGroupBox)
        self.insertMouseXYHotkey.setGeometry(QtCore.QRect(260, 126, 121, 31))
        self.insertMouseXYHotkey.setObjectName("insertMouseXYHotkey")

        self.label = QtWidgets.QLabel(self.insertMouseGroupBox)
        self.label.setGeometry(QtCore.QRect(260, 110, 121, 16))
        self.label.setObjectName("label")

        self.insertMouseX = QtWidgets.QTextEdit(self.insertMouseGroupBox)
        self.insertMouseX.setGeometry(QtCore.QRect(40, 126, 81, 31))
        self.insertMouseX.setObjectName("insertMouseX")

        self.insertMouseY = QtWidgets.QTextEdit(self.insertMouseGroupBox)
        self.insertMouseY.setGeometry(QtCore.QRect(140, 126, 91, 31))
        self.insertMouseY.setObjectName("insertMouseY")

        self.label_2 = QtWidgets.QLabel(self.insertMouseGroupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 134, 21, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.insertMouseGroupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 134, 21, 16))
        self.label_3.setObjectName("label_3")

        self.line = QtWidgets.QFrame(self.insertMouseGroupBox)
        self.line.setGeometry(QtCore.QRect(10, 90, 371, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("insertBreaksLine")

        self.insertMouseGo = QtWidgets.QCommandLinkButton(self.insertMouseGroupBox)
        self.insertMouseGo.setGeometry(QtCore.QRect(260, 30, 111, 41))
        self.insertMouseGo.setObjectName("insertMouseGo")

        self.insertMouseRadio01.raise_()

        self.insertMouseRadio02.raise_()

        self.insertMouseRadio03.raise_()

        self.insertMouseRadio04.raise_()

        self.insertMouseRadio05.raise_()

        self.insertMouseRadio06.raise_()

        self.insertMouseXYHotkey.raise_()

        self.label.raise_()

        self.label_2.raise_()

        self.insertMouseX.raise_()

        self.label_3.raise_()

        self.insertMouseY.raise_()

        self.line.raise_()

        self.insertMouseGo.raise_()

        self.editorGroupBox = QtWidgets.QGroupBox(self.frame)
        self.editorGroupBox.setGeometry(QtCore.QRect(410, 10, 654, 489))
        self.editorGroupBox.setObjectName("editorGroupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.editorGroupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("editorGridLayout")

        self.workspaceTree = QtWidgets.QTreeWidget(self.editorGroupBox)
        self.workspaceTree.setMinimumSize(QtCore.QSize(361, 191))
        self.workspaceTree.setObjectName("workspaceTree")
        self.workspaceTree.setColumnCount(1)
        self.workspaceTree.setHeaderLabels(["workspace"])
        self.workspaceTree.setSortingEnabled(False)

        
        

        self.gridLayout.addWidget(self.workspaceTree, 1, 1, 1, 1)

        self.editorTransportGroupBox = QtWidgets.QGroupBox(self.editorGroupBox)
        self.editorTransportGroupBox.setMinimumSize(QtCore.QSize(191, 51))
        self.editorTransportGroupBox.setMaximumSize(QtCore.QSize(191, 51))
        self.editorTransportGroupBox.setObjectName("editorTransportGroupBox")

        self.editorBtnPlay = QtWidgets.QPushButton(self.editorTransportGroupBox)
        self.editorBtnPlay.setGeometry(QtCore.QRect(10, 20, 51, 28))
        self.editorBtnPlay.setMinimumSize(QtCore.QSize(51, 28))
        self.editorBtnPlay.setMaximumSize(QtCore.QSize(51, 28))
        self.editorBtnPlay.setObjectName("editorBtnPlay")

        self.editorBtnStop = QtWidgets.QPushButton(self.editorTransportGroupBox)
        self.editorBtnStop.setGeometry(QtCore.QRect(70, 20, 51, 28))
        self.editorBtnStop.setMinimumSize(QtCore.QSize(51, 28))
        self.editorBtnStop.setMaximumSize(QtCore.QSize(51, 28))
        self.editorBtnStop.setObjectName("editorBtnStop")

        self.editorBtnPause = QtWidgets.QPushButton(self.editorTransportGroupBox)
        self.editorBtnPause.setGeometry(QtCore.QRect(130, 20, 51, 28))
        self.editorBtnPause.setMinimumSize(QtCore.QSize(51, 28))
        self.editorBtnPause.setMaximumSize(QtCore.QSize(51, 28))
        self.editorBtnPause.setObjectName("editorBtnPause")

        self.gridLayout.addWidget(self.editorTransportGroupBox, 0, 1, 1, 1)

        self.editorListGroupBox = QtWidgets.QGroupBox(self.editorGroupBox)
        self.editorListGroupBox.setMinimumSize(QtCore.QSize(111, 151))
        self.editorListGroupBox.setMaximumSize(QtCore.QSize(111, 151))
        self.editorListGroupBox.setObjectName("editorListGroupBox")

        self.editorBtnNewMacro = QtWidgets.QPushButton(self.editorListGroupBox)
        self.editorBtnNewMacro.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.editorBtnNewMacro.setMinimumSize(QtCore.QSize(93, 28))
        self.editorBtnNewMacro.setMaximumSize(QtCore.QSize(93, 28))
        self.editorBtnNewMacro.setObjectName("editorBtnNewMacro")

        self.editorBtnEditStep = QtWidgets.QPushButton(self.editorListGroupBox)
        self.editorBtnEditStep.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.editorBtnEditStep.setMinimumSize(QtCore.QSize(93, 28))
        self.editorBtnEditStep.setMaximumSize(QtCore.QSize(93, 28))
        self.editorBtnEditStep.setObjectName("editorBtnEditStep")

        self.editorBtnCopySelection = QtWidgets.QPushButton(self.editorListGroupBox)
        self.editorBtnCopySelection.setGeometry(QtCore.QRect(10, 110, 93, 28))
        self.editorBtnCopySelection.setMinimumSize(QtCore.QSize(93, 28))
        self.editorBtnCopySelection.setMaximumSize(QtCore.QSize(93, 28))
        self.editorBtnCopySelection.setObjectName("editorBtnCopySelection")

        self.gridLayout.addWidget(self.editorListGroupBox, 1, 0, 1, 1)

        self.splitter = QtWidgets.QSplitter(self.editorGroupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("clipboardSplitter")

        self.clipboardTree = QtWidgets.QTreeView(self.splitter)
        self.clipboardTree.setMinimumSize(QtCore.QSize(253, 192))
        self.clipboardTree.setObjectName("clipboardTree")

        self.clipboardQuickViewList = QtWidgets.QListView(self.splitter)
        self.clipboardQuickViewList.setMinimumSize(QtCore.QSize(253, 192))
        self.clipboardQuickViewList.setObjectName("clipboardQuickViewList")

        self.gridLayout.addWidget(self.splitter, 2, 1, 1, 1)

        self.editorGroupBox.raise_()

        self.insertKeystrokeGroupBox.raise_()

        self.insertBreaksGroupBox.raise_()

        self.insertTextGroupBox.raise_()

        self.insertMouseGroupBox.raise_()

        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1292, 26))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)

        self.actionOpen_Workspace = QtWidgets.QAction(MainWindow)
        self.actionOpen_Workspace.setObjectName("actionOpen_Workspace")

        self.actionNew_Workspace = QtWidgets.QAction(MainWindow)
        self.actionNew_Workspace.setObjectName("actionNew_Workspace")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionClose_Workspace = QtWidgets.QAction(MainWindow)
        self.actionClose_Workspace.setObjectName("actionClose_Workspace")

        self.menuFile.addAction(self.actionNew_Workspace)
        self.menuFile.addAction(self.actionOpen_Workspace)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Workspace)

        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.insertBreaksGroupBox.setTitle(_translate("MainWindow", "Breaks"))

        self.insertBreaksGo.setText(_translate("MainWindow", "Insert"))

        self.insertBreaksAdvGo.setText(_translate("MainWindow", "Insert"))

        self.insertBreaksAdvRadio01.setText(_translate("MainWindow", "After Every Step"))

        self.insertBreaksAdvRadio02.setText(_translate("MainWindow", "After Mouse Clicks"))

        self.insertBreaksAdvRadio03.setText(_translate("MainWindow", "After Keystrokes"))

        self.insertBreaksAdvOptions.setText(_translate("MainWindow", "..."))

        self.insertTextGroupBox.setTitle(_translate("MainWindow", "Text"))

        self.insertTextGo.setText(_translate("MainWindow", "Insert"))

        self.insertKeystrokeGroupBox.setTitle(_translate("MainWindow", "Keystroke"))

        self.insertKeystrokeOptions.setItemText(0, _translate("MainWindow", "Press & Release (Down & Up)"))
        self.insertKeystrokeOptions.setItemText(1, _translate("MainWindow", "Press (Down)"))
        self.insertKeystrokeOptions.setItemText(2, _translate("MainWindow", "Release (Up)"))

        self.insertKeystrokeGo.setText(_translate("MainWindow", "Insert"))

        self.insertMouseGroupBox.setTitle(_translate("MainWindow", "Mouse"))

        self.insertMouseRadio01.setText(_translate("MainWindow", "Left Click"))

        self.insertMouseRadio02.setText(_translate("MainWindow", "Right Click"))

        self.insertMouseRadio03.setText(_translate("MainWindow", "Center Click"))

        self.insertMouseRadio04.setText(_translate("MainWindow", "Scroll Up"))

        self.insertMouseRadio05.setText(_translate("MainWindow", "Scroll Down"))

        self.insertMouseRadio06.setText(_translate("MainWindow", "New Mouse XY"))

        self.label.setText(_translate("MainWindow", "Get XY Hotkey"))

        self.label_2.setText(_translate("MainWindow", "X"))

        self.label_3.setText(_translate("MainWindow", "Y"))

        self.insertMouseGo.setText(_translate("MainWindow", "Insert"))

        self.editorGroupBox.setTitle(_translate("MainWindow", "Step Editor"))

        self.editorTransportGroupBox.setTitle(_translate("MainWindow", "Transport"))

        self.editorBtnPlay.setText(_translate("MainWindow", "Play"))

        self.editorBtnStop.setText(_translate("MainWindow", "Stop"))

        self.editorBtnPause.setText(_translate("MainWindow", "Pause"))

        self.editorListGroupBox.setTitle(_translate("MainWindow", "List"))

        self.editorBtnNewMacro.setText(_translate("MainWindow", "New Macro"))

        self.editorBtnEditStep.setText(_translate("MainWindow", "Edit Step"))

        self.editorBtnCopySelection.setText(_translate("MainWindow", "Copy Selection"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.actionOpen_Workspace.setText(_translate("MainWindow", "Open Workspace"))

        self.actionNew_Workspace.setText(_translate("MainWindow", "New Workspace"))

        self.actionSave.setText(_translate("MainWindow", "Save"))

        self.actionSave_As.setText(_translate("MainWindow", "Save As"))

        self.actionClose_Workspace.setText(_translate("MainWindow", "Close Workspace"))


