import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]
	def __str__(self):
		return self.rank + ' of ' + self.suit


class Deck:

	def __init__(self):
		self.allcards = []
		for suit in suits:
			for rank in ranks:
				self.allcards.append(Card(suit,rank))
	
	def shuffle(self):
		random.shuffle(self.allcards)

	def deal_one(self):
		return self.allcards.pop()

	def deal_two(self):
		return self.allcards.pop()
		return self.allcards.pop()

class Player:

	def __init__(self, name, bank):
		self.bank = bank
		self.name = name
		self.hand = []
		self.value = 0
		self.ace = 0


	def bet(self):
		print("money to bet")
		print(self.bank)
		amount = 'fool'
		while amount not in range(0, self.bank+1):
			try:
				amount = int(input("Place your bet: "))
				if amount not in range(0, self.bank+1):
					print('You cannot bet that much')
					
			except:
				print("Place a valid bet")
		return amount

	def draw_one(self):
		if deck.allcards[0].rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		self.adjust_ace()
		self.display_hand()

	def draw_two(self):
		if deck.allcards[0].rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		if deck.allcards[0].rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		self.adjust_ace()
		self.display_hand()
	
	def display_hand(self):
		print("in your hand")
		for i in self.hand:
			print(i)
		print(self.value)

	def discard(self):
		self.hand = []
		self.value = 0

	def adjust_ace(self):
		while self.value>21 and self.ace:
			self.value-=10
			self.ace-=1

	def __str__(self):
		return f'Player: {self.name}   Bank: {self.bank}'


class Computer:

	def __init__(self, name):
		self.name = name
		self.hand = []
		self.value = 0
		self.ace = 0

	def draw_one(self):
		if deck.allcards.pop(0).rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		self.adjust_ace()

	def draw_two(self):
		if deck.allcards[0].rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		if deck.allcards[0].rank == 'Ace':
			self.ace+=1
		self.hand.append(deck.allcards.pop(0))
		self.value+=self.hand[-1].value
		
		self.adjust_ace()

	def draw(self):
		while self.value < 18:
			self.draw_one()
	
	def show_half(self):
		print("In the computer's hand")
		print(self.hand[0])

	def display_hand(self):
		print('The computer hand')
		for i in self.hand:
			print(i)
		print(self.value)
	
	def discard(self):
		self.hand = []
		self.value = 0

	def adjust_ace(self):
		while self.value>21 and self.ace:
			self.value-=10
			self.ace-=1

	def __str__(self):
		return f'The computer is holding {self.hand[0]}'

def hit_stay():
	gamble = 'wrong'
	while gamble not in ['H','h','s','S']:
		gamble = input('Would you like to hit or stay?  [H, S]')
	if gamble not in ['H','h','s','S']:
		print('Enter H or S.')
	return gamble


deck = Deck()
deck.shuffle()


play = Player(input("Enter your name: "), 500)
com = Computer('com')

game_on = True

while game_on == True:
	com.discard()
	play.discard()
	if len(deck.allcards)<=10:
		print("not enough cards to play!")
		game_on = False
	if play.bank <= 0:
		print("You are out of money!!")
		game_on = False

	print(play)
	bet = play.bet()
	play.bank-=bet
	com.draw_two()
	com.show_half()
	play.draw_two()
	
	gambel = 'nope'
	while gambel == 'nope':
		playing = hit_stay()
		if playing == 's' or playing == 'S':
			gambel = "Continue"
		else:
			play.draw_one()
			if play.value>21:
				print("You lose")
				gambel = "Continue"
	print(f'Your total is {play.value}.')
	if play.value>21:
		continue
	com.draw()
	com.display_hand()
	if play.value>21:
		print("You lose")
	elif com.value > 21:
		print("You win!!")
		play.bank+=bet*2
	elif com.value> play.value:
		print('You lose')
	elif play.value>com.value:
		print("You win!!")
		play.bank+=bet*2
	elif com.value == 21 and play.value == 21:
		print('You lose')


