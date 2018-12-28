# Instructions to the fantasy cricket league application
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout 
import sys

class InstructionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = QTextEdit(self)
        self.text.setText(
        '''
            Welcome to the Fantasy Cricket League Game!\n
            Create your Team, Play a Match and who knows.. maybe you can
            win!

            There are some rules to follow here. Please go through them for a
            better experience
            1. Team's creation starts with you clicking on
                            'Manage Teams' > 'NEW Team'
            2. Then Navigate to the 'OPEN Team' option in the menu and click
            on that
            3. Select your team in the drop down list
            4. Once done with that, you can select your players from given
            categories by clicking on the radio button required and double
            clicking on the player name
            5. If you selected a player accidentally, you can remove the player
            from the team by double clicking on the player name in the second
            widget
            6. Click on 'SAVE Team' in the 'Manage Teams' to save your team
            7. Remember, you can select only
                - 4 Batsmen
                - 4 Bowlers
                - 2 All Rounders
                - 1 Wicket Keeper
            per team
            8. To play a match you can go to the 'EVALUATE Team' Option in the
            menu and select the team and the match number.

            Thanks for reading the very long instruction manual.
            Hope you have fun! 
        '''
        )

        self.text.setReadOnly(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text)

        self.setLayout(vbox)
        self.setGeometry(400,170,440,440)
        self.setWindowTitle('Instructions')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = InstructionWindow()
    sys.exit(app.exec_())
