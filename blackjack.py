import random

player_name = "YoungHwan"
nextGame = True
count = 0

class Blackjack(object):
    cardDeck = [
        'A', 'A', 'A', 'A', 2, 2, 2, 2,
        3, 3, 3, 3, 4, 4, 4, 4,
        5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8,
        9, 9, 9, 9, 10, 10, 10, 10,
        'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q',
        'K', 'K', 'K', 'K'
    ]

    result = {'win': 0, 'lose': 0, 'draw': 0}

    def drawing(self):
        if self.cardDeck:
            x = random.choice(self.cardDeck)
            self.cardDeck.remove(x)
            return x
        else:
            print('There \'s no card left')

    def __init__(self, name):
        self._deck = {}
        self._deck[name] = []
        self._deck['dealer'] = []
        self._sum = {}
        self._sum['dealer'] = 0
        self._sum[name] = 0
        for i in range(2):
            self._deck[name].append(self.drawing())
            self._deck['dealer'].append(self.drawing())

        self.hidden_card = self._deck['dealer'][0]
        self._deck['dealer'][0] = 'H'

        self.ace_card = []

        print('Dealer\'s Deck: {}'.format(self._deck['dealer']))
        print('{}\'s Deck: {}'.format(name,self._deck[name]))

    def choose_ace(self, name):

        if name == 'dealer':
            return 11
        else:
            while True:
                x = input("choose your ace as 1 or 11:")
                if type(int(x)) == int and (int(x) == 1 or int(x) == 11):
                    return int(x)
                    break

    def counting(self, name):
        sum = 0
        for index, card in enumerate(self._deck[name]):
            if card == 'A':
                 sum += self.choose_ace(name)
            elif card == 'J' or card == 'Q' or card == 'K':
                sum += 10
            elif card == 'H':
                if self.hidden_card == 'A':
                    sum += self.choose_ace(name)
                elif self.hidden_card == 'J' or self.hidden_card == 'Q' or \
                    self.hidden_card == 'K':
                    sum += 10
                else:
                    sum += self.hidden_card
            else:
                sum += card
        # print("{}\'s count is {}".format(name, sum))
        self._sum[name] = sum
        return sum

    def comparing(self, name):
        player = self.counting(name)
        dealer = self.counting('dealer')
        print("hidden_card is",self.hidden_card)

        if (21 - dealer) > (21 - player):
            self.result['win'] += 1
            print("Dealer:{} You: {}\n#######You Win#######".format(self._sum['dealer'],self._sum[name]))
        elif (21 - dealer) < (21 - player):
            self.result['lose'] += 1
            print("Dealer:{} You: {}\n#######You Lose#######".format(self._sum['dealer'],self._sum[name]))
        elif (21- dealer) == (21-player):
            self.result['draw'] += 1
            print("Dealer:{} You: {}\n########Draw########".format(self._sum['dealer'],self._sum[name]))

        elif dealer > 21 and player <= 21:
            self.result['win'] += 1
            print("#######Dealer Burst! You Win#######")

    def betting(self,name):
        player = self.counting(name)
        dealer = self.counting('dealer')


        if player == 21:
            self.result['win'] += 1
            print("#######It's BlackJack! You Win!#######")
            return 0

        elif player > 21:
            self.result['lose'] += 1
            print("#######Burst! you lose#######")
            return 0


        while True:

            x = input("insert 'H'(hit) or 'S'(stand):")
            if x == 'H':
                if dealer < 16:
                    self._deck['dealer'].append(self.drawing())
                    self._deck[name].append(self.drawing())
                    print('Dealer\'s Deck: {}'.format(self._deck['dealer']))
                    print('{}\'s Deck: {}'.format(name, self._deck[name]))
                    self.betting(name)
                    break

                else:
                    self._deck[name].append(self.drawing())
                    print('Dealer\'s Deck: {}'.format(self._deck['dealer']))
                    print('{}\'s Deck: {}'.format(name, self._deck[name]))
                    self.betting(name)
                    break

            elif x == 'S':
                self.comparing(name)
                break


while nextGame:
    count += 1
    print("\nHere's {}th game! Good Luck!!\n".format(count))
    game = Blackjack(player_name)
    game. betting(player_name)
    x = input("Will you continue? (Y/N):")
    if x == 'N':
        nextGame = False
        print(game.result)