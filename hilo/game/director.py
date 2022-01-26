# from hashlib import new
from game.card import Card


class Director:
   """The director of the game. 

   The game play is controlled by the Director.

   Attributes:        
      is_playing (boolean): Whether or not the game is being played.
      total_score (int): The score for the entire game.

   Methods:
      start_game(): starts the main game loop
      get_input(): prompts player for guess
      do_updates(): updates player's score
      show_points(): displays player's points and asks if player wants to continue to play
   """

   def __init__(self):
      """Constructor
      
      Args:
         self (Director)
      """

      self.card = Card()
      self.next_card = Card()
      self.guess = ''
      self.is_playing = True
      self.points = 300
      

   def start_game(self):
      """
      Starts the game by running the main game loop.
      
      Args:
         self (Director)
      """

      while self.is_playing:
         self.get_inputs()
         self.do_updates()
         self.show_points()

   def get_inputs(self):
      """
      Display first card.
      Ask for guess if the next card will be higher or lower.

      Args:
         self (Director): An instance of Director.
      """
      self.card.deal()
      print(f"\nThe card is: {self.card.value}")
      self.guess = input("Higher or lower? [h/l] ")
      self.next_card.deal()
      print(f"The next card was: {self.next_card.value}") 
            
   def do_updates(self):
      """Updates the player's score.

      Args:
         self (Director): An instance of Director.
      """

      if not self.is_playing:
         return 

      # If the next card is the same as the current card the guess is counted
      # as incorrect.
      if self.guess == 'h':
         if self.next_card.value > self.card.value:
            self.points += 100
         else:
            self.points -= 75
      else:
         if self.next_card.value < self.card.value:
            self.points += 100
         else:
            self.points -= 75

   def show_points(self):
      """Displays the score. Also asks the player if they want to roll again. 

      Args:
         self (Director)
      """
      
      self.is_playing = (self.points > 0)

      if not self.is_playing:
         return
      
      print(f"Your score is: {self.points}")
      
      self.is_playing = input("Play again? [y/n] ") == 'y'

      if not self.is_playing:
         return
   
