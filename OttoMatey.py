###OttoMatey
###v1.00
###
###Records and automates keystroke and mouse function events
###Manual insertion of events, pauses, and breaks
###Store and recall user generated macros

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from OttoMatey_GUI_modified import Ui_MainWindow
from pprint import pprint
import tables



class Convert:
    def __init__(self):
        pass

    def todata(self, text):
        pass

    def totext(self, data):
        pass

class FileOps:
    def __init__(self, filename, fileurl, filedate, filedata):
        self.filename   = filename
        self.fileurl    = fileurl
        self.filedate   = filedate
        self.filedata   = filedata

    def loadmacro(self):
        pass
        
    def savemacro(self):
        pass

    def getlistofmacros(self):
        pass


class Clipboard:
    def __init__(self, clipboarddata={}):
        self.clipboarddata  = clipboarddata

    def clipboardupdate(self):
        pass

    def getactiveclip(self):
        return self.activeclip

    def show(self, markerstart, markerend):
        pass

    def add(self, clipboarddata):
        pass
        
    def delete(self, markerstart, markerend):
        pass

    def saveasmacro(self, markerstart, markerend):
        pass

    #copy/paste in the Clipboard class deals only with clipboard entries
    #data is stored and copied as dict {clipname:data}
    def copy(self, markerstart, markerend):
        pass

    #pasting copied clipboard data into the active macro list will insert 
    #a ":note: {clipname:}", followed by the {:data}
    def paste(self, markerstart, markerend):
        pass
        




class Record:
    def __init__(self, recordparams, recordlimits, recordfunction="recordnew"):
        self.recordparams   = recordparams
        self.recordlimits   = recordlimits
        self.recordfunction = recordfunction
        
    def recordstart(self):
        pass

    def recordstop(self):
        pass

    def recordpause(self):
        pass

    def recordresume(self):
        pass


class Listener:
    def __init__(self):
        pass

    def startlisten(self):
        pass

    def stoplisten(self):
        pass



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.ui.insertTextEvent = self



        #self.workspacedata contains all data shown in the workspace tree. 
        #used for storing/modifying data without needing to operate on the QTreeWidget and QTreeWidgetItem objects
        self.workspacedata = {}

        #self.loadedkeys tracks the topLevelItems by macrotype  e.g.  {'10000', QTreeWidgetItem at x000ec601}
        self.loadedkeys = {}


#####################################################################################################
#####################################################################################################
        #event signals      

        self.ui.insertBreaksGo.clicked.connect(self.mInsertBreaksGo)
        self.ui.insertBreaksAdvGo.clicked.connect(self.mInsertBreaksAdvGo)
        self.ui.insertTextGo.clicked.connect(self.mInsertTextGo)
        self.ui.insertKeystrokeGo.clicked.connect(self.mInsertKeystrokeGo)
        self.ui.insertMouseGo.clicked.connect(self.mInsertMouseGo)


    def mInsertBreaksGo(self):
        #send the event type that is highlighted, and the value in the QDoubleSpinBox
        wrk.insert(self.ui.workspaceTree.currentItem().type(), str.format("Break {0:.2f}s", self.ui.insertBreaksTime.value()), "noAdvFunction")

    def mInsertBreaksAdvGo(self):
        #insert a break after every step
        if self.ui.insertBreaksAdvRadio01.isChecked():
            tempfunction = "afterEveryStep"
        #insert a break after every mouse click
        elif self.ui.insertBreaksAdvRadio02.isChecked():
            tempfunction = "afterMouseClicks"
        #insert a break after every keystroke or text grouping
        elif self.ui.insertBreaksAdvRadio03.isChecked():
            tempfunction = "afterKeystrokes"

        wrk.insert(self.ui.workspaceTree.currentItem().type(), self.ui.insertBreaksTime.value(), tempfunction)

    def mInsertTextGo(self):
        #insert a string of text into a single event slot
        wrk.insert(self.ui.workspaceTree.currentItem().type(), self.ui.insertTextField.value(), "textInsert")

    def mInsertKeystrokeGo(self):
        pass

    def mInsertMouseGo(self):
        pass


#####################################################################################################
#####################################################################################################


        
    def setWorkspaceItems(self, data):
        datakeys = data.keys()
        
        #keys of new dict pairs being sent in data
        for macrotype in datakeys: 
            if macrotype not in self.workspacedata:
                self.ui.workspaceTree.addTopLevelItem(QtWidgets.QTreeWidgetItem([data[macrotype][0]], int(macrotype)))
            
            self.workspacedata[macrotype] = data[macrotype]

        #keys of all TopLevel entries in the tree
        for i in range(0, self.ui.workspaceTree.topLevelItemCount()):
            k = str(self.ui.workspaceTree.topLevelItem(i).type())
            v = self.ui.workspaceTree.topLevelItem(i)
            v.setChildIndicatorPolicy(QtWidgets.QTreeWidgetItem.DontShowIndicatorWhenChildless)
            self.loadedkeys[k] = v

        for macrotype in datakeys:
            self.loadedkeys[macrotype].takeChildren()
            for child in data[macrotype][1:]:
                temptype = list(child.keys())[0]
                tempname = child[temptype]
                self.loadedkeys[macrotype].addChild(QtWidgets.QTreeWidgetItem(self.loadedkeys[macrotype], [tempname], int(temptype)))

    def setMacroItems(self, data, macro):
        self.loadedkeys[macro].takeChildren()
        self.workspacedata[macro] = data

        for child in data[1:]:
            temptype = list(child.keys())[0]
            tempname = child[temptype]
            print("temptype = ", temptype)
            print("tempname = ", tempname)
            self.loadedkeys[macro].addChild(QtWidgets.QTreeWidgetItem(self.loadedkeys[macro], [tempname], int(temptype)))



#####################################################################################################
#####################################################################################################


clipboard   = Clipboard()
converter   = Convert()
listener    = Listener()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()



#####################################################################################################
#####################################################################################################


class Workspace:
    def __init__(self, macrodata={"10000": ["myMacro", {"10001": "Break 1.50s"}]}):
        self.macrodata = macrodata
        self.workspaceupdate()

    def workspaceupdate(self):
        win.setWorkspaceItems(self.macrodata)

    def macroupdate(self, data):
        win.setMacroItems(self.macrodata[data], data)

    def findnexttype(self, macro):
        temptype = int(macro) + 1
        s = self.macrodata[macro]
        for s in self.macrodata[macro]:
            print(s)
            print(str(temptype))
            if str(temptype) in self.macrodata[macro]:
                temptype += 1

            else:
                return(str(temptype))

    def insert(self, temptype, editdata, methodtype):
        #use the 5 digit temptype to determine the macro and position to insert the event into
        tempmacro = str((temptype / 10000) * 10000)
        try:
            tempindex = self.macrodata[str(tempmacro)].index(str(temptype))
        except:
            tempmacro = str(10000)
            tempindex = 1

        if methodtype == "noAdvFunction":
            self.macrodata[tempmacro].insert(tempindex, {self.findnexttype(tempmacro):editdata})

        elif methodtype == "afterEveryStep":
            for ins in range(1, len(self.macrodata[tempmacro])):
                self.macrodata[tempmacro].insert((ins * 2), {self.findnexttype(tempmacro):editdata})

        elif methodtype == "afterMouseClicks":
            tempstring = ".click"
            k = 0
            for ins in range(1, len(self.macrodata[tempmacro])):
                if tempstring.lower() in self.macrodata[tempmacro][ins + k].lower:
                    self.macrodata[tempmacro].insert((ins + k), {self.findnexttype(tempmacro):editdata})
                    k += 1

        elif methodtype == "afterKeystrokes":
            tempstring = "keystroke"
            k = 0
            for ins in range(1, len(self.macrodata[tempmacro])):
                if tempstring.lower() in self.macrodata[tempmacro][ins + k].lower:
                    self.macrodata[tempmacro].insert((ins + k), {self.findnexttype(tempmacro):editdata})
                    k += 1      

        elif methodtype == "textInsert":
            self.macrodata[tempmacro].insert(tempindex, {self.findnexttype(tempmacro):editdata})

        else:
            print("error calling Workspace.insert - '{0}' not found", methodtype)


        print("self.macrodata = ", self.macrodata[tempmacro])

        self.macroupdate(tempmacro)





    def delete(self, temptype):
        tempmacro = (temptype / 10000) * 10000
        try:
            tempindex = self.macrodata[str(tempmacro)].index(str(temptype))
        except:
            tempmacro = str(10000)
            tempindex = 1
        
        self.macrodata[tempmacro].pop(tempindex)
        self.macroupdate[tempmacro]

    #copy/paste in the Macro class deals with data in the active macro list                
    def copy(self, markerstart, markerend):
        c.add(self.macrodata[markerstart:markerend])
        
    def paste(self, markerstart, markerend):
        self.insert(markerstart, markerend, c.getactiveclip)


#####################################################################################################
#####################################################################################################





wrk = Workspace()

           


if __name__ == "__main__":

    sys.exit(app.exec_())



    




