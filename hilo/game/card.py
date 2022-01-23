import random

class Card:
    """A generation of a card 1 to 13.
       The responsibility of Card is to keep track of the card selected 
   
        Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Card.
        Args:
            self (Die): An instance of Card.
        """
        self.value = 0

    def deal(self):
        """Selects a new random card.
        
        Args:
            self (Card): An instance of Hilo.
        """
        self.value = random.randint(1, 13)
