import random
from deck import suits, values


class Players:
    def __init__(self, name, hand_list, points=0, bet=0 ,deposit=0):
        self.name = name
        self.hand_list = hand_list
        self.points = points
        self.bet = bet
        self.deposit = deposit


    def draw_cards(self):
        self.hand_list.append(random.choice(deck))
        for card in self.hand_list:
            if self.hand_list.count(card) > 1:
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
    def __init__(self, game_over):
        self.game_over = game_over

    def intro(self):
        print('BlackJack game will begin soon')
        print(f"Player's name is: {player1.name} and his rival is {computer.name}")
        player1.deposit = int(input("How much money do you want to start with?"))
        start_game.play()

    def game_continue(self):
        if player1.deposit > 0:
            choice = int(input("Do you want to continue? 1.Yes/2.No"))
            if choice == 1:
                self.deck_hand_refresh()
                self.game_over = False
                start_game.play()
            else:
                print("Thanks for playing")
        else:
            print("Your deposit is 0. Can't continue")
    def deck_hand_refresh(self):
        player1.hand_list = []
        computer.hand_list = []

    def play(self):
        while not start_game.game_over:
            player1.bet = int(input("How much money do you want to bet?"))
            if player1.bet > player1.deposit:
                print(f"You can't bet this much, Your deposit is {player1.deposit}")
            else:
                print(f"{player1.name} starts with ${player1.deposit}")
                print(f"{player1.name} bets ${player1.bet} on this game")
                player1.draw_cards()
                player1.draw_cards()
                print(f'{player1.name} draws 2 cards:')
                player1.show_cards()
                player1.show_points()
                print(f'{computer.name} draws 2 cards, one is hidden')
                computer.draw_cards()
                computer.show_cards()
                computer.show_points()

                player_decision = int(input("Do you want 1.Hit, 2.Stand, 3.Double, 4.Split"))
                if player_decision == 1:
                    player1.draw_cards()
                    player1.show_card()
                    player1.show_points()
                    win_condition()
                elif player_decision == 2:
                    while computer.points <= 17:
                        computer.draw_cards()
                        computer.show_card()
                        computer.show_points()
                        win_condition()

                elif player_decision == 3 and len(player1.hand_list) == 2:
                    player1.bet *= 2
                    player1.draw_cards()
                    player1.show_card()
                    player1.show_points()
                    win_condition()
                    while computer.points <= 17:
                        computer.draw_cards()
                        computer.show_card()
                        computer.show_points()
                        win_condition()

                elif player_decision == 3 and len(player1.hand_list) > 2:
                    print("You can't double. Already have more than 2 cards!")


def win_condition():
    if player1.points > 21:
        print(f'{computer.name} WINS! You overdrew!')
        player1.deposit -= player1.bet
        print(f'You lose {player1.bet} and your deposit is {player1.deposit}')
        start_game.game_over = True
        start_game.game_continue()
    elif player1.points == 21:
        print(f'{player1.name} has won the BLACKJACK!')
        player1.bet *= 2
        player1.deposit += player1.bet
        print(f'You have won {player1.bet} and your deposit is {player1.deposit}')
        start_game.game_over = True
        start_game.game_continue()
    elif computer.points >= 17:
        print(f'The Crupier got 17 or more points worth of cards.')
        print('Calculating points between player and Crupier!')
        print(f'{player1.name} points: {player1.points}\t{computer.name} points: {computer.points}')
        if player1.points > computer.points or computer.points > 21:
            print(f'{player1.name} has won the game!')
            player1.bet *= 2
            player1.deposit += player1.bet
            print(f'You have won {player1.bet} and your deposit is {player1.deposit}')
            start_game.game_over = True
            start_game.game_continue()
        else:
            print(f'{computer.name} WINS!')
            player1.deposit -= player1.bet
            print(f'You lose {player1.bet} and your deposit is {player1.deposit}')
            start_game.game_over = True
            start_game.game_continue()

if __name__ == "__main__":
    player1 = Players('Player', [])
    computer = Players('Computer', [])
    deck = [Card(suit, value) for suit in suits for value in values]
    for cards in deck:
        cards.give_points()
    start_game = Game(False)
    start_game.intro()
