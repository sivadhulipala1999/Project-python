# Mini stats display window for each player
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QObject, pyqtSignal
import globalVars, Retrieve

class Communicate(QObject):
    signal = pyqtSignal()

class miniWindow(QWidget):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.nameLbl = QLabel(self)
        self.dict = Retrieve.retrieve_data(self.name)
        self.nameLbl.setText('Player Name : ' + self.dict['NAME'])
        
        self.pointLbl = QLabel(self)
        self.pointLbl.setText('Player Value : ' + str(self.dict['VALUE']))

        self.matLbl = QLabel(self)
        self.matLbl.setText('Matches played : ' + str(self.dict['MATCHES']))
        
        self.catLbl = QLabel(self)
        self.catLbl.setText('Player Category : ' + str(self.dict['CATEGORY']))
        
        self.runs = QLabel(self)
        self.runs.setText('Runs : ' + str(self.dict['RUNS']))

        self.centLbl = QLabel(self)
        self.centLbl.setText('Centuries : ' + str(self.dict['100S']))

        self.halfCentLbl = QLabel(self)
        self.halfCentLbl.setText('Half Centuries : ' + str(self.dict['50S']))

        self.runouts = QLabel(self)
        self.runouts.setText('Runouts : ' + str(self.dict['RUNOUTS']))

        self.wickets = QLabel(self)
        self.wickets.setText('Wickets : ' + str(self.dict['WICKETS']))

        self.stumps = QLabel(self)
        self.stumps.setText('Stumps : ' + str(self.dict['STUMPS']))

        self.yesbtn = QPushButton("Confirm Player",self)
        self.nobtn = QPushButton("Cancel",self)

        self.yesbtn.clicked.connect(self.yesFunc)
        self.nobtn.clicked.connect(self.noFunc)

        vbox = QVBoxLayout()
        vbox.addWidget(self.nameLbl)
        vbox.addWidget(self.pointLbl)
        vbox.addWidget(self.matLbl)
        vbox.addWidget(self.catLbl)
        vbox.addWidget(self.runs)
        vbox.addWidget(self.centLbl)
        vbox.addWidget(self.halfCentLbl)
        vbox.addWidget(self.runouts)
        vbox.addWidget(self.wickets)
        vbox.addWidget(self.stumps)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.yesbtn)
        hbox.addWidget(self.nobtn)
        
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(400,240,300,300)
        self.setWindowTitle('Player Information')
        self.show()

    def yesFunc(self):
        self.c.signal.emit()
        self.close()

    def noFunc(self):
        self.close()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    ex = miniWindow('VIRAT') # for testing
    ex.show()
    sys.exit(app.exec_())
