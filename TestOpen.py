# open window test
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QComboBox, QWidget, QVBoxLayout, QListWidget, QDesktopWidget
import globalVars

class Communicate(QObject):

    signal = pyqtSignal()
    
class OpenWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # creating the widgets combo box and list view
        self.comboBox = QComboBox(self)
        self.listWidget = QListWidget(self)
        print(globalVars.teamNames)
        self.comboBox.addItems(globalVars.teamNames)
        ## add the members of the selected team to the list widget

        # put the selected team's name in the globalVars module for future ref
        self.comboBox.currentTextChanged.connect(self.updateSelectedTeam)

        # object instance which emits a signal to change the current team name in display
        self.c = Communicate()
                
        # putting the widgets in a vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)

        #centering the window
        fr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fr.moveCenter(cp)
        self.move(fr.topLeft())

        self.resize(400,300)
        self.setWindowTitle('Open Window')

    def updateSelectedTeam(self,value):
        globalVars.selectedTeam = value
        self.c.signal.emit()
        self.listWidget.clear()
        if value == '--':
            return
        if len(globalVars.teamData[globalVars.selectedTeam]):
            self.listWidget.addItems(globalVars.teamData[globalVars.selectedTeam])

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    globalVars.init()
    op = OpenWin()
    '''
    stuff for testing purpose
    op.comboBox.addItems(['Dream11','Dream11.2'])
    globalVars.teamData['Dream11'] = ['Virat']
    globalVars.teamData['Dream11.2'] = []
    '''
    op.show()
    sys.exit(app.exec_())
