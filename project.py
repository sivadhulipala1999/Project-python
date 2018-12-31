# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalProject_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import NewWindow, TestOpen, evalTeam, instructionWindow, playerInfo, calculate_pt
import globalVars
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.bat = QtWidgets.QLabel(self.centralwidget)
        self.bat.setObjectName("bat")
        self.horizontalLayout.addWidget(self.bat)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.bowl = QtWidgets.QLabel(self.centralwidget)
        self.bowl.setObjectName("bowl")
        self.horizontalLayout.addWidget(self.bowl)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.ar = QtWidgets.QLabel(self.centralwidget)
        self.ar.setObjectName("ar")
        self.horizontalLayout.addWidget(self.ar)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.wk = QtWidgets.QLabel(self.centralwidget)
        self.wk.setObjectName("wk")
        self.horizontalLayout.addWidget(self.wk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pointUsed = QtWidgets.QLabel(self.centralwidget)
        self.pointUsed.setObjectName("pointUsed")
        self.verticalLayout_3.addWidget(self.pointUsed)
        self.teamView = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamView.sizePolicy().hasHeightForWidth())
        self.teamView.setSizePolicy(sizePolicy)
        self.teamView.setObjectName("teamView")
        self.verticalLayout_3.addWidget(self.teamView)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pointAvail = QtWidgets.QLabel(self.centralwidget)
        self.pointAvail.setObjectName("pointAvail")
        self.verticalLayout_2.addWidget(self.pointAvail)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.batbtn = QtWidgets.QRadioButton('BAT',self.centralwidget)
        self.bowbtn = QtWidgets.QRadioButton('BOW',self.centralwidget)
        self.arbtn = QtWidgets.QRadioButton('AR',self.centralwidget)
        self.wkbtn = QtWidgets.QRadioButton('WK',self.centralwidget)

        # addition of radio buttons via hand
        self.horizontalLayout_2.addWidget(self.batbtn)
        self.horizontalLayout_2.addWidget(self.bowbtn)
        self.horizontalLayout_2.addWidget(self.arbtn)
        self.horizontalLayout_2.addWidget(self.wkbtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.teamView.addItem('Team Name: ##')
        
        self.playerView = QtWidgets.QListWidget(self.centralwidget)
        self.playerView.setObjectName("playerView")
        self.verticalLayout_2.addWidget(self.playerView)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 21))
        self.menubar.setObjectName("menubar")
        self.menuMANAGE_TEAMS = QtWidgets.QMenu(self.menubar)
        self.menuMANAGE_TEAMS.setObjectName("menuMANAGE_TEAMS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuMANAGE_TEAMS.addAction(self.actionNEW_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionOPEN_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionSAVE_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuMANAGE_TEAMS.menuAction())

        self.actionNEW_Team.triggered.connect(self.showNewWindow)
        self.actionOPEN_Team.triggered.connect(self.showOpenWindow)
        self.actionSAVE_Team.triggered.connect(self.saveTeamFunction)
        self.actionEVALUATE_Team.triggered.connect(self.evaluateTeam)

        self.batbtn.toggled.connect(lambda : self.createBatTeam(self.batbtn))
        self.bowbtn.toggled.connect(lambda : self.createBowTeam(self.bowbtn))
        self.arbtn.toggled.connect(lambda : self.createArTeam(self.arbtn))
        self.wkbtn.toggled.connect(lambda : self.createWkTeam(self.wkbtn))

        self.playerView.itemDoubleClicked.connect(self.updateTeamView)
        self.teamView.itemDoubleClicked.connect(self.updatePlayerView)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy League Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_5.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.bat.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bowl.setText(_translate("MainWindow", "##"))
        self.label_9.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.ar.setText(_translate("MainWindow", "##"))
        self.label_11.setText(_translate("MainWindow", "Wicket Keepers(WK)"))
        self.wk.setText(_translate("MainWindow", "##"))
        self.pointUsed.setText(_translate("MainWindow", "Points Used : ##"))
        self.pointAvail.setText(_translate("MainWindow", "Points Available : ##"))
        self.menuMANAGE_TEAMS.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def showNewWindow(self):
        # NEW TEAM action should create a new team. This window is for that purpose.
        self.newWindow = NewWindow.NewWin()
        self.newWindow.show()

    def showOpenWindow(self):
        # OPEN TEAM action should show the available teams and populate the players in the list view widget
        if len(globalVars.teamNames) == 0:
            print('No Teams exist at the moment. Action Invalid')
            return
        self.openWindow = TestOpen.OpenWin()
        self.openWindow.c.signal.connect(self.changeName)
        self.openWindow.show()

    def saveTeamFunction(self):
        if globalVars.selectedTeam == '--':
            return
        if len(globalVars.teamData[globalVars.selectedTeam]) < 11:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setText('Selected Team does not have 11 players yet')
            alert.exec_()
            return
    
        alert = QMessageBox.question(self.centralwidget,'Save Team Confirmation Window', 'Is this the final team?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if alert == QMessageBox.Yes:
            finalTeamView = QMessageBox()
            finalTeamView.setIcon(QMessageBox.Information)
            s = 'Team : ' + globalVars.selectedTeam + ' Confirmed'
            s += '\n Team Players are\n\n'
            for player in globalVars.teamData[globalVars.selectedTeam]:
                s += player + '\n'
            finalTeamView.setText(s)
            finalTeamView.exec_()
            self.refresh()
            
    def evaluateTeam(self):
        self.evalTeam = evalTeam.evalTeamWindow()
        self.evalTeam.show()
        self.evalTeam.teamBox.addItems(globalVars.teamNames)
        self.evalTeam.matchBox.addItems(['--','MATCH 1','MATCH 2','MATCH 3','MATCH 4','MATCH 5'])
        self.evalTeam.teamBox.currentTextChanged.connect(self.teamDisplay)
        self.evalTeam.c.calc_signal.connect(self.pointDisplay)
        self.team = '--'
        self.match = '--'

    def teamDisplay(self,value):
        self.team = value
        self.evalTeam.playerView.clear()
        self.evalTeam.pointView.clear()
        self.evalTeam.points.setText('##')
        if value == '--':
            print('Please select a valid team')
            return
        self.evalTeam.playerView.addItems(globalVars.teamData[self.team])
        # point view widget is updated only when the button is pressed

    def pointDisplay(self):
        matchItem = self.evalTeam.matchBox.currentText()
        self.match = str(matchItem)
        self.evalTeam.pointView.clear()
        self.evalTeam.points.setText('##')
        if self.team == '--':
            print('Please select a valid team')
            return
        if self.match == '--':
            print('This match number is invalid. Select a valid match number')
            return
        match = int(self.match[6]) # we only need the match number
        point_list = calculate_pt.score_calc(match,globalVars.teamData[self.team])
        for it in point_list[:len(point_list)-1]:
            self.evalTeam.pointView.addItem(str(it))
        self.evalTeam.points.setText(str(point_list[len(point_list)-1]))
    
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        print('working')
        if point_list[len(point_list)-1] > 520:
            alert.setText('Whoa! You have hit the jackpot! Congrats!!')
            
        elif point_list[len(point_list)-1] > 400:
            alert.setText('Great! Your team has done exceptionally well')

        elif point_list[len(point_list)-1] > 280:
            alert.setText('That was a good performance. But, it could have been better')

        elif point_list[len(point_list)-1] > 0:
            alert.setText('That was not a great performance')

        alert.exec_()
        
    def createBatTeam(self,radiobtn):
        # this function is executed only when the batbtn is checked
        # this checking is done so as to prevent the unnecessary signals from
        # all the radio buttons
        if self.batbtn.isChecked(): 
            if globalVars.selectedTeam == '--':
                print('Team Name needs to be selected')
                return
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['BAT']:
                self.playerView.addItem(item)
                    
    def createBowTeam(self,radiobtn):
        if self.bowbtn.isChecked():
            if globalVars.selectedTeam == '--':
                print('Team Name needs to be selected')
                return
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['BOW']:
                self.playerView.addItem(item)            

    def createArTeam(self,radiobtn):
        if self.arbtn.isChecked():
            if globalVars.selectedTeam == '--':
                print('Team Name needs to be selected')
                return
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['AR']:
                self.playerView.addItem(item)

    def createWkTeam(self,radiobtn):
        if self.wkbtn.isChecked():
            if globalVars.selectedTeam == '--':
                print('Team Name needs to be selected')
                return
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['WK']:
                self.playerView.addItem(item)

    def updateTeamView(self):
        "this function updates the teamView widget and hence, the entire selected team"
        # functionality to limit the players in the team
        # max number of selections per category
        if len(globalVars.teamData[globalVars.selectedTeam]) == 11:
            print('Team formation has been done. You can change the team by removing the existing players')
            return            
        t = self.pointAvail.text()
        if int(t[19:]) < 60: # 60 is the lowest value of a player in the player database
            print('Required points unavailable. Please reform your team')
            return
        limit = {"batn":4,"bown":4,"arn":2,"wkn":1}
        if self.batbtn.isChecked():
            category = 'BAT'
        elif self.bowbtn.isChecked():
            category = 'BOW'
        elif self.arbtn.isChecked():
            category = 'AR'
        elif self.wkbtn.isChecked():
            category = 'WK'
        it = self.playerView.currentItem()
        if globalVars.teamSelections[globalVars.selectedTeam][category.lower()] < limit[category.lower()+'n']:
            # the teamView widget is updated here by removing the item from
            # playerView widget and adding the same item to the teamView widget
            # The available players to each team are stored in the playersAvail
            # dictionary available in the globalVars module. This dictionary is
            # updated to now state that the player transferred to the teamView
            # widget is no longer available to the team
            self.miniwin = playerInfo.miniWindow(it.text())
            self.miniwin.c.signal.connect(lambda : self.teamUpdate(category,it))
            
        else:
            alertBox = QMessageBox()
            alertBox.setIcon(QMessageBox.Warning)
            alertBox.setText('You can\'t select more than ' + str(limit[category.lower() + 'n']) + ' ' + category + ' type players for the team')
            alertBox.exec_()            

    def teamUpdate(self,category,item):
        score = globalVars.players_score_dict
        it = self.playerView.takeItem(self.playerView.currentRow())
        self.teamView.addItem(it)
        l = globalVars.playersAvail[globalVars.selectedTeam][category]
        pos = l.index(it.text()) #index where the player name is available in the list l created
        del l[pos] # remember that vars in python are used by reference which implies that deletion in this list will get reflected in the dictionary
        globalVars.teamData[globalVars.selectedTeam].append(it.text())
        globalVars.teamSelections[globalVars.selectedTeam][category.lower()] += 1
        globalVars.teamSelections[globalVars.selectedTeam]['point'] -= score[it.text()]
        globalVars.teamSelections[globalVars.selectedTeam]['used'] += score[it.text()]
        self.pointAvail.setText('Points Available : ' + str(globalVars.teamSelections[globalVars.selectedTeam]['point']))
        self.pointUsed.setText('Points Used : ' + str(globalVars.teamSelections[globalVars.selectedTeam]['used']))
        self.bat.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['bat']))
        self.bowl.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['bow']))
        self.ar.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['ar']))
        self.wk.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['wk']))
            
    def updatePlayerView(self):
        if self.teamView.currentRow() == 0:
            # this item is the team. Don't disturb it.
            print('non interactable item')
            return
        # just delete the item from the Team View widget and put it back in the
        # Player View widget
        it = self.teamView.currentItem()
        category = globalVars.players_data_dict.get(it.text())
        if category == 'ALL':
            category = 'AR'
        # the player is no longer a part of the selected team. Update the details
        # update the player view widget and available players list
        it = self.teamView.takeItem(self.teamView.currentRow())
        l = globalVars.playersAvail[globalVars.selectedTeam][category]
        l.append(it.text())
        score = globalVars.players_score_dict
        # update the team
        globalVars.teamSelections[globalVars.selectedTeam][category.lower()] -= 1
        playersList = globalVars.teamData[globalVars.selectedTeam]
        i = playersList.index(it.text())
        del playersList[i]
        globalVars.teamSelections[globalVars.selectedTeam]['point'] += score[it.text()]
        globalVars.teamSelections[globalVars.selectedTeam]['used'] -= score[it.text()]
        self.pointAvail.setText('Points Available : ' + str(globalVars.teamSelections[globalVars.selectedTeam]['point']))
        self.pointUsed.setText('Points Used : ' + str(globalVars.teamSelections[globalVars.selectedTeam]['used']))
        self.bat.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['bat']))
        self.bowl.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['bow']))
        self.ar.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['ar']))
        self.wk.setText(str(globalVars.teamSelections[globalVars.selectedTeam]['wk']))
        # update the playerView widget as soon as the dictionary gets updated
        if self.batbtn.isChecked():
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['BAT']:
                self.playerView.addItem(item)
        elif self.bowbtn.isChecked():
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['BOW']:
                self.playerView.addItem(item)
        elif self.arbtn.isChecked():
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['AR']:
                self.playerView.addItem(item)
        elif self.wkbtn.isChecked():
            self.playerView.clear()
            for item in globalVars.playersAvail[globalVars.selectedTeam]['WK']:
                self.playerView.addItem(item)

    def changeName(self):
        teamName = globalVars.selectedTeam
        if teamName == '--':
            self.refresh()
            return
        self.teamView.clear() # previous team's players should not interfere this team
        self.teamView.addItem('Team Name : ' + teamName)
        self.pointUsed.setText('Points Used : 0')
        self.pointAvail.setText('Points Available : ' + str(globalVars.teamSelections[teamName]['point']))
        self.bat.setText(str(globalVars.teamSelections[teamName]['bat']))
        self.bowl.setText(str(globalVars.teamSelections[teamName]['bow']))
        self.ar.setText(str(globalVars.teamSelections[teamName]['ar']))
        self.wk.setText(str(globalVars.teamSelections[teamName]['wk']))
        self.teamView.addItems(globalVars.teamData[teamName])

    def refresh(self):
        self.bat.setText('##')
        self.bowl.setText('##')
        self.ar.setText('##')
        self.wk.setText('##')
        self.pointUsed.setText('Points Used : ##')
        self.pointAvail.setText('Points Available : ##')
        globalVars.selectedTeam = '--'
        self.playerView.clear()
        self.teamView.clear()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    globalVars.init() # initialises the teamNames list
    players = globalVars.players_data_dict # player dictionary
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    win = instructionWindow.InstructionWindow()
    sys.exit(app.exec_())

