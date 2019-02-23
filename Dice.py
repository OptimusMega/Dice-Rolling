class Dice:
    """Group of Die"""
    def __init__(self, NumberofDice, Sided):
        self.Dice = []
        for i in range(1,NumberofDice+1):
            self.Dice.append(Die(Sided))
            
    def Roll(self):
        """Roll Group of Dice and Return Tuple of Numbers"""
        RollNumbers =list()
        for i in self.Dice:
            RollNumbers.append(i.Roll())
        return tuple(RollNumbers)
        
        
class Die:
    """A Single Die"""
    def __init__(self, NumberofSides):
        self.Die = []
        for i in range(1,NumberofSides+1):
            self.Die.append(Side(i))
            
    def Roll(self):
        """Roll a single Die and Return the side it lands on"""
        from random import randint
        return self.Die[randint(0,len(self.Die)-1)]
            

class Side(int):
    """Represents the Side of a Die"""
    def __init__(self,sideNumber):
        """Initializer that stores the Side number of the die"""
        int.__init__(sideNumber)
        self.Side = sideNumber
