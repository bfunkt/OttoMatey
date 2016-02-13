###OttoMatey
###v1.00
###
###Records and automates keystroke and mouse function events
###Manual insertion of events, pauses, and breaks
###Store and recall user generated macros

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from OttoMatey_GUI_modified import Ui_MainWindow



MACROHANDLEBASE = 10000
MAXMACROS       = 50

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
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)




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

    
    def setChildIndicatorPolicy(self, reference):
        reference.setChildIndicatorPolicy(QtWidgets.QTreeWidgetItem.DontShowIndicatorWhenChildless)

    def searchTopLevelItems(self):
        for i in range(0, self.ui.workspaceTree.topLevelItemCount()):
            handle  = self.ui.workspaceTree.topLevelItem(i).type()
            ref     = self.ui.workspaceTree.topLevelItem(i)
            wrk.setObjectReference(handle, i, ref)

    def searchChildItems(self, parentobjectreference):
        children = parentobjectreference.children()
        for ref in children:
            handle  = ref.type()
            index   = ref.indexOfChild()
            wrk.setObjectReference(handle, index, ref)


    #the presence of a parenthandle determines if the  is parent or child
    def addUiItem(self, handle, parentobjectreference, index, name): 
        #add a top level 
        if handle % MACROHANDLEBASE == 0:
            parent = self.ui.workspaceTree.insertTopLevelItem(index, QtWidgets.QTreeWidgetItem([name], handle))

            self.searchTopLevelItems()

        #add a child 
        else:
            parentobjectreference.insertChild(index, parent([name], handle))

            self.searchChildItems(parentobjectreference)

    def removeUiItem(self, index, parentobjectreference):
        if parentobjectreference is None:
            self.ui.workspaceTree.takeTopLevelItem(index)

        else:
            parentobjectreference.takeChild(index)

    def getCurrentIndex(self):
        return(self.ui.workspaceTree.currentItem())


#####################################################################################################
#####################################################################################################
class Data:
    def __init__(self, importdata=None):
        self.sessdata   = {}        #all widget data, hashed by handle
        self.sessmacros = []        #list of all the top level handles e.g. '10000', '30000', etc
        if importdata is not None:
            self.importdata = importdata
            #populate data to self.sessdata
        else:
            pass

    def initFirstTreeObject(self):
        self.addItem(10000, 0, 'myMacro', None)


    def returnParentHandle(self, handle):
        handle -= handle % MACROHANDLEBASE
        return(handle)

    def addUiItem(self, parenthandle, parentobjectreference, index, name):
        win.addUiItem(parenthandle, parentobjectreference, index, name)

    def removeUiItem(self, parentobjectreference):
        win.removeUiItem(parentobjectreference)

        #returns the list of events in a specified macro
    def getMacroList(self, handle):
        d       = []
        count   = 0

        for k, v in self.sessdata.items():
            if v[2] == handle:
                d.append([k, v[2]])

        d = sorted(d, key=lambda col: col[1])

        return(d)

    def organizeMacro(self, handle):
        d = self.getMacroList(handle)
        for i in range(0, len(d)):
            self.sessdata[d[i][0]] = i

        return(d)

    def organizeData(self, macro=None):
            if macro == None:
                for handle in self.sessmacros:
                    self.organizeMacro(handle)
            else:
                for i in macro:
                    i = i - (i % MACROHANDLEBASE) #find the top level handle
                    self.organizeMacro(i)

    def addItem(self, handle=None, index=None, name=None, parenthandle=None, reference=QtWidgets.QTreeWidgetItem):
        self.sessdata[handle]   = [     index,              #0
                                        name,               #1
                                        parenthandle,       #2
                                        reference]          #3

        self.organizeData([handle])
        self.addUiItem(handle, self.sessdata[handle][3], self.sessdata[handle][0], self.sessdata[handle][1])


    def removeItem(self, handles):
        deletedset = ()
        for handle in handles:
            if handle in self.sessdata:
                if self.returnParentHandle(handle) in sessmacros:
                    deletedset.add(self.returnParentHandle(handle))
                else:
                    deletedset.add(handle)
                self.removeUiItem(self.sessdata[handle][3]) #send the handle and the object reference to remove UI s
                del self.sessdata[handle]
        self.organizeData(deletedset)

    def setObjectReference(self, handle, index, reference):
        self.sessdata[handle][0] = index
        self.sessdata[handle][3] = reference
        win.setChildIndicatorPolicy(reference)


    def findNextHandle(self, handle):
        #if searching for a macro handle / top level  (multiples of 10000)
        if int(handle % MACROHANDLEBASE) == 0:
            i = 0
            while i < MAXMACROS:
                i += 1
                j = i * MACROHANDLEBASE
                if j in self.sessmacros:
                    pass
                else:
                    return(j)
            return(0)

        #if searching for a child handle
        else:
            handle -= handle % MACROHANDLEBASE
            while i < MACROHANDLEBASE:
                i += 1
                j = handle + i
                if j in self.sessdata:
                    pass
                else:
                    return(j)
            return(0)
          

    def insert(self, handle, data, methodtype):
        if handle is None or handle not in self.sessdata:
            for i in range(1, MAXMACROS):
                i *= MACROHANDLEBASE
                if i in self.macrodata:
                    handle = i

        if methodtype == "noAdvFunction":
            self.addItem(self.findNextHandle(handle), win.getCurrentIndex(), data, self.returnParentHandle(handle))

        elif methodtype == "afterEveryStep":
            i = 1
            for item in self.getMacroList(self.returnParentHandle(handle)):
                self.addItem(self.findNextHandle(handle), (i * 2 - 1), data, self.returnParentHandle(handle))
                i += 1

        elif methodtype == "afterMouseClicks":
            tempstring = ".Click"
            k = 1
            for item in self.getMacroList(self.returnParentHandle(handle)):
                if tempstring.lower() in self.sessdata[item][2].lower:
                    k += 1
                    self.addItem(findNextHandle(handle), k, data, self.returnParentHandle(handle))
                k += 1

        elif methodtype == "afterKeystrokes":
            tempstring = "Keystrokes"
            k = 1
            for item in self.getMacroList(self.returnParentHandle(handle)):
                if tempstring.lower() in self.sessdata[item][2].lower:
                    k += 1
                    self.addItem(self.findNextHandle(handle), k, data, self.returnParentHandle(handle))
                k += 1

        elif methodtype == "textInsert":
            self.addItem(self.findNextHandle(handle), win.getCurrentIndex(), data, self.returnParentHandle(handle))
        else:
            print("error calling Workspace.insert - '{0}' not found", methodtype)

        self.organizeMacro(self.returnParentHandle(handle))



    # #copy/paste in the Macro class deals with data in the active macro list                
    # def copy(self, markerstart, markerend):
    #     c.add(self.macrodata[markerstart:markerend])
        
    # def paste(self, markerstart, markerend):
    #     self.insert(markerstart, markerend, c.getactiveclip)


#####################################################################################################
#####################################################################################################

#####################################################################################################
#####################################################################################################


clipboard   = Clipboard()
converter   = Convert()
listener    = Listener()


wrk = Data()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()


wrk.initFirstTreeObject()


           


if __name__ == "__main__":

    sys.exit(app.exec_())



    




