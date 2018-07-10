import random

player_name = "YoungHwan"
dealer=[]
player=[]
result =  True

class Blackjack(object):


    def drawing(self):
        cardlist = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        x = random.choice(cardlist)
        return x

    def __init__(self, name):
        self._deck = {}
        self._deck[name] = []
        self._deck['dealer'] = []

        self._deck[name].append(self.drawing())
        self._deck['dealer'].append(self.drawing())
        self._deck[name].append(self.drawing())
        self._deck['dealer'].append(self.drawing())

        self.hidden_card = self._deck['dealer'][0]
        self._deck['dealer'][0] = 'H'

        self.ace_card = []

        print('Dealer\'s Deck: {}'.format(self._deck['dealer']))
        print('{}\'s Deck: {}'.format(name,self._deck[name]))

    def counting(self, name):
        sum = 0
        for index, card in enumerate(self._deck[name]):
            if card == 'A':

                while True:
                    x = int(input('choose A as 1 or 11:'))
                    if x ==  11 or x == 1:
                        self.ace_card.append(x)
                        self._deck[name][index] = x
                        sum += self.ace_card[-1]
                        break

            elif card == 'J' or card == 'Q' or card == 'K':
                sum += 10
            elif card == 'H':
                #dealer의 경우 A를 11로 카운트한다고 가정
                if self.hidden_card == 'A':
                    x = 11
                    sum += x
                elif self.hidden_card == 'J' or self.hidden_card == 'Q' or \
                    self.hidden_card == 'K':
                    sum += 10
                else:
                    sum += self.hidden_card
            else:
                sum = sum + card
        # print("{}\'s count is {}".format(name, sum))
        return sum

    def comparing(self, name):
        player = self.counting(name)
        dealer = self.counting('dealer')
        print("hidden_card is",self.hidden_card)
        if (21 - dealer) > (21 - player):
            print("#######You Win#######")
        elif (21 - dealer) < (21 - player):
            print("#######You Lose#######")
        else:
            print("########Draw########")

    def betting(self,name):
        player = self.counting(name)
        dealer = self.counting('dealer')
        if player == 21:
            print("#######It's BlackJack! You Win!#######")


        elif player > 21:
            print("#######Burst! you lose#######")


        elif player < 21:
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


while result:
    game = Blackjack(player_name)
    game. betting(player_name)
    x = input("Will you continue? (Y/N):")
    if x == 'N':
        result = False
