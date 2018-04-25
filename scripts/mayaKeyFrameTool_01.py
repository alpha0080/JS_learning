# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/mayaTool/spineTools/mainwindow.ui'
#
# Created: Wed Apr 25 21:56:32 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 180, 191, 221))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_rootName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rootName.setGeometry(QtCore.QRect(40, 40, 231, 41))
        self.lineEdit_rootName.setObjectName("lineEdit_rootName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))





class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):

        self.pushButton.clicked.connect(self.getItems)
        self.initialUI()
    
    def initialUI(self):
        self.lineEdit_rootName.setText("select or fill in root")
    
    
    def cycleKeys(self,obj,offsetIn,offsetOut,repeatTimes):
        
        keyAbleAttList= ["tx","ty","tz","rx","ry","rz","sx","sy","sz"]
        for attr in keyAbleAttList:
            keyFrameList = cmds.keyframe(obj,at=attr,q=True)
            startKeyFrame = keyFrameList[0]
            endKeyFrame = keyFrameList[-1]
            offsetRange = offsetOut -offsetIn +1
           # print attr,keyFrameList,startKeyFrame,endKeyFrame
            for i in range(0,repeatTimes):
                for j in keyFrameList:
                    frame = i*offsetRange + j
                   # print"attr",attr, i*offsetRange + j
                    getValue = float(cmds.keyframe(obj,at= attr,time=(j,j) ,query=True,ev=True)[0])
                    cmds.setKeyframe(obj,v=getValue,at=attr,time=(frame,frame))
                    print getValue

           # frame = i *offsetRange
            
    
    def getItems(self):
        
        print "get Items"
        self.cycleKeys("pSphere1",1,100,8)
       # selectItems = cmds.ls(sl=True)
       # print selectItems
       # for obj in selectItems:
       #     print self.getKeyFrameList(obj)
       #     
        
    def getKeyFrameList(self,obj):
        
        keyFrameList = cmds.keyframe(obj,q=True)
        
        return keyFrameList
        


def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()


 