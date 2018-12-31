# Evaluate Team Window
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QGridLayout, QHBoxLayout, QVBoxLayout, QListWidget, QPushButton, QFrame, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    calc_signal = pyqtSignal()

class evalTeamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # creating the widgets
        self.heading = QLabel('Evaluate the Performances of your Fantasy Team',self)
        self.teamBox = QComboBox(self)
        self.matchBox = QComboBox(self)

        self.playerlbl = QLabel('Players',self)
        self.pointlbl = QLabel('Points: ',self)
        self.points = QLabel('##',self)

        self.playerView = QListWidget(self)
        self.pointView = QListWidget(self)

        self.calcScore = QPushButton('Calculate Score',self)
        self.calcScore.clicked.connect(self.signal_emit)
        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # adding the widgets to a grid layout
        self.gridLayout = QGridLayout()
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.teamBox)
        self.horizontalLayout.addWidget(self.matchBox)
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.gridLayout.addWidget(self.playerlbl, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.points, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.pointlbl, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.calcScore, 6, 1, 1, 2)
        self.gridLayout.addWidget(self.pointView, 5, 2, 1, 2)
        self.gridLayout.addWidget(self.playerView, 5, 0, 1, 2)
        self.gridLayout.addWidget(self.heading, 1, 1, 1, 2)

        self.setLayout(self.gridLayout)

        # centering the widget
        cp = self.frameGeometry()
        qr = QDesktopWidget().availableGeometry().center()
        cp.moveCenter(qr)
        self.move(cp.topLeft())

        self.setWindowTitle('Evaluate Team')

    def signal_emit(self):
        self.c.calc_signal.emit()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    ev = evalTeamWindow()
    ev.show()
    sys.exit(app.exec_())
