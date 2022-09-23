import random
from deck import suits, values


class Players:
    def __init__(self, name, hand_list,points=0,bet=0):
        self.name = name
        self.hand_list = hand_list
        self.points = points
        self.bet = bet

    def draw_cards(self):
        self.hand_list.append(random.choice(deck))
        for card in self.hand_list:
            if self.hand_list.count(card) > 1:
                print("CARD IS THE SAME!!")
                self.hand_list.pop()
                self.hand_list.append(random.choice(deck))

    def show_cards(self):
        for card in self.hand_list:
            print(f'{card.value} of {card.suit} and has {card.points} points')

    def show_card(self):
        for card in self.hand_list:
            if card == self.hand_list[-1]:
                print(f'{self.name} draws a card:')
                print(f'{card.value} of {card.suit} and has {card.points} points')

    def show_points(self):
        self.points = 0
        for card in self.hand_list:
            self.points += card.points
        print(f'{self.name} has: {self.points} points overall')




class Card:
    def __init__(self, suit, value, points=0):
        self.suit = suit
        self.value = value
        self.points = points

    def give_points(self):
        if self.value == 'J' or self.value == 'Q' or self.value == 'K':
            self.points = 10
        elif self.value == "Ace":
            self.points = 11
        else:
            self.points = self.value

class Game:
    def __init__(self,game_over):
        self.game_over = game_over


    def play(self):
        print('BlackJack game will begin soon')
        print(f"Player's name is: {player1.name} and his rival is {computer.name}")
        player1.draw_cards()
        player1.draw_cards()
        print(f'{player1.name} draws 2 cards:')
        player1.show_cards()
        player1.show_points()
        print(f'{computer.name} draws 2 cards, one is hidden')
        computer.draw_cards()
        computer.show_cards()
        computer.show_points()
        while not start_game.game_over:
            player_decision = int(input("Do you want 1.Hit or 2.Stand?"))
            if player_decision == 1:
                player1.draw_cards()
                player1.show_card()
                player1.show_points()
                if player1.points > 21:
                    print(f'{computer.name} WINS! You overdrew!')
                    start_game.game_over = True
                elif player1.points == 21:
                    print(f'{player1.name} has won the BLACKJACK!')
            elif player_decision == 2:
                while computer.points <= 17:
                    computer.draw_cards()
                    computer.show_card()
                    computer.show_points()
                    if computer.points >= 17:
                        print(f'The Crupier got 17 or more points worth of cards.')
                        print('Calculating points between player and Crupier!')
                        print(f'{player1.name} points: {player1.points}\t{computer.name} points: {computer.points}')
                        if player1.points > computer.points or computer.points > 21:
                            print(f'{player1.name} has won the game!')
                            start_game.game_over = True
                        else:
                            print(f'{computer.name} WINS!')
                            start_game.game_over = True
if __name__ == "__main__":
    player1 = Players('Dominik', [])
    computer = Players('Computer', [])
    deck = [Card(suit, value) for suit in suits for value in values]
    for cards in deck:
        cards.give_points()
    start_game = Game(False)
    start_game.play()