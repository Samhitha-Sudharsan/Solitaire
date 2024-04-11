import random

# Define the card suit and rank
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Define the card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Define the deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise IndexError('Cannot draw a card from an empty deck')

# Define the pile class
class Pile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        return self.cards.pop()

    def display_cards(self):
        for card in self.cards:
            print(card)

# Define the tableau class
class Tableau:
    def __init__(self):
        self.piles = [Pile() for _ in range(7)]

    def add_card(self, pile_index, card):
        self.piles[pile_index].add_card(card)

    def remove_card(self, pile_index):
        return self.piles[pile_index].remove_card()

    def display_cards(self):
        for i, pile in enumerate(self.piles):
            print(f"Pile {i+1}:")
            pile.display_cards()

# Define the foundation class
class Foundation:
    def __init__(self):
        self.piles = [Pile() for _ in range(4)]

    def add_card(self, pile_index, card):
        self.piles[pile_index].add_card(card)

    def remove_card(self, pile_index):
        return self.piles[pile_index].remove_card()

    def display_cards(self):
        for i, pile in enumerate(self.piles):
            print(f"Pile {i+1}:")
            pile.display_cards()

# Define the game class
class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.tableau = Tableau()
        self.foundation = Foundation()

    def deal(self):
        self.deck.shuffle()
        for i in range(7):
            for j in range(i, 7):
                self.tableau.add_card(j, self.deck.draw_card())

    def move_card(self, src_pile_index, src_pile_type, dest_pile_index, dest_pile_type):
        if src_pile_type == 'tableau':
            card = self.tableau.remove_card(src_pile_index)
        elif src_pile_type == 'foundation':
            card = self.foundation.remove_card(src_pile_index)
        else:
            raise ValueError('Invalid source pile type')

        if dest_pile_type == 'tableau':
            self.tableau.add_card(dest_pile_index, card)
        elif dest_pile_type == 'foundation':
            self.foundation.add_card(dest_pile_index, card)
        else:
            raise ValueError('Invalid destination pile type')

    def is_game_over(self):
        for pile in self.foundation.piles:
            if len(pile.cards)!= 13:
                return False
        return True

    def get_user_input(self):
        while True:
            user_input = input('Enter a command (type "help" for a list of commands): ')
            if user_input == 'help':
                print('Available commands:')
                print('deal: deal the cards')
                print('move <src_pile_index> <src_pile_type> <dest_pile_index> <dest_pile_type>: move a card from one pile to another')
                print('quit: quit the game')
            elif user_input == 'deal':
                self.deal()
                self.tableau.display_cards()
                self.foundation.display_cards()
            elif user_input.startswith('move '):
                parts = user_input.split()
                if len(parts)!= 5:
                    print('Invalid command format. Use "move <src_pile_index> <src_pile_type> <dest_pile_index> <dest_pile_type>"')
                    continue
                src_pile_index = int(parts[1])
                src_pile_type = parts[2]
                dest_pile_index = int(parts[3])
                dest_pile_type = parts[4]
                try:
                    self.move_card(src_pile_index, src_pile_type, dest_pile_index, dest_pile_type)
                    self.tableau.display_cards()
                    self.foundation.display_cards()
                except ValueErroras :
                    print(e)
            elif user_input == 'quit':
                break
            else:
                print('Invalid command. Use "help" for a list of commands.')

# Start the game
game = Solitaire()
game.get_user_input()