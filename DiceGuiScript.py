import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsScene,QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


from Dice import Dice
from DiceRolling import *

class DicePicture:
    """Hold pictures of the sides of a die"""
    Dice = {1:"DieSidePictures/FaceDie1.png",
            2:"DieSidePictures/FaceDie2.png",
            3:"DieSidePictures/FaceDie3.png",
            4:"DieSidePictures/FaceDie4.png",
            5:"DieSidePictures/FaceDie5.png",
            6:"DieSidePictures/FaceDie6.png"}
    
class RollingGame(QMainWindow):
    """GUI of Dice Rolling"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        self.scene2 = QGraphicsScene(self)
        
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load(DicePicture.Dice[1])
        
        self.pixmap2 = QtGui.QPixmap()
        self.pixmap2.load(DicePicture.Dice[1])
        
        item = QGraphicsPixmapItem(self.pixmap)
        item2 = QGraphicsPixmapItem(self.pixmap2)
        
        self.scene.addItem(item)
        self.scene2.addItem(item2)

        dir(self.scene)
        
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView_2.setScene(self.scene2)
        
        self.ui.RollDice.clicked.connect(self.roller)
        self.Dice = Dice(2,6)
        self.show()

    def roller(self):
        """Roll Dice"""
        Roll = self.Dice.Roll()
        
        self.pixmap.load(DicePicture.Dice[Roll[0]])
        self.pixmap2.load(DicePicture.Dice[Roll[1]])
        
        item = QGraphicsPixmapItem(self.pixmap)
        item2 = QGraphicsPixmapItem(self.pixmap2)
        
        self.scene.addItem(item)
        self.scene2.addItem(item2)
        
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView_2.setScene(self.scene2)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = RollingGame()
    w.show()
    sys.exit(app.exec_())
