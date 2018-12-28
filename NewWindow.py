# NEW window
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget, QHBoxLayout, QVBoxLayout
import globalVars

class NewWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Placing the widgets
        self.line = QLineEdit(self)
        self.text = "Team Name goes Here"
        self.line.setPlaceholderText(self.text)
        self.pbtn = QPushButton("Confirm",self)
        self.pbtn.setToolTip('Confirm the team name you have entered')
        self.pbtn.clicked.connect(self.confirm)
        self.line.move(20,20)
        self.pbtn.move(180,20)

        self.lbl = QLabel('Team Name Input Validation',self)

        #Addition of Layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.line)
        hbox.addWidget(self.pbtn)
        vbox.addLayout(hbox)
        vbox.addWidget(self.pbtn)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        # Centering the window
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.resize(300,300)
        self.setWindowTitle('New Window')

    def confirm(self):
        # team name length validation
        if len(self.line.text()) > 40:
            self.lbl.setText('Team Name should be less than 40 characters long')
            return
        else:
            self.lbl.setText('Team Name is of valid length')

        # alert message popup
        question = QMessageBox.question(self,'Team Name Confirmation', 'Do you want to confirm the Team name?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if question == QMessageBox.Yes:
            self.text = self.line.text()
            self.lbl.setText('Team Name accepted')
            self.endFunction()
        else:
            pass # Do nothing

    def endFunction(self):
        if self.text in globalVars.teamNames: # to prevent repetition of team names
            self.lbl.setText('Team Name already exists. Try another one.')
            return
        globalVars.teamNames.append(self.text)
        MAX_POINTS = 840 # 4 best, 2 above avg, 2 avg, 3 below avg players
        globalVars.teamSelections[self.text] = {"bat":0,"bow":0,"ar":0,"wk":0,"point":MAX_POINTS,"used":0}
        globalVars.teamData[self.text] = []
        players = globalVars.players_data_dict
        globalVars.playersAvail[self.text] = {"BAT":[],"BOW":[],"AR":[],"WK":[]}
        for person in players:
            if players[person] == "BAT":
                globalVars.playersAvail[self.text]['BAT'].append(person)
            elif players[person] == "BOW":
                globalVars.playersAvail[self.text]['BOW'].append(person)
            elif players[person] == "ALL":
                globalVars.playersAvail[self.text]['AR'].append(person)
            elif players[person] == "WK":
                globalVars.playersAvail[self.text]['WK'].append(person)
        self.close()

if __name__ == "__main__":
    # do this only if the program is launched as a standalone application 
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    globalVars.init()
    s = NewWin()
    s.show()
    sys.exit(app.exec_())
            
