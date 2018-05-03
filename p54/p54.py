#https://projecteuler.net/problem=54 Poker hands
# High Card: Highest value card. 1
# One Pair: Two cards of the same value. 2
# Two Pairs: Two different pairs. 3
# Three of a Kind: Three cards of the same value. 4
# Straight: All cards are consecutive values. 5
# Flush: All cards of the same suit. 6
# Full House: Three of a kind and a pair. 7
# Four of a Kind: Four cards of the same value. 8
# Straight Flush: All cards are consecutive values of same suit. 9


class hand:

    def __init__(self, rawIn):
        self.cards = []
        self.handValue = [0,0]
        cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
                 'Q': 12, 'K': 13, 'A': 14}
        for i in range(0,len(rawIn)-1, 3):
            self.cards.append([cards[str(rawIn[i])],rawIn[i+1]])
        self.cards.sort(key=lambda card: card[0])

    def getHighCard(self):
        return self.cards[4][0]

    def getNextHighestCard(self, n):
        return self.cards[4-n][0]

    def getPairs(self):
        vals = []
        pairs = []
        for card in self.cards:
            vals.append(card[0])
        for card in vals:
            if vals.count(card) == 2:
                if card not in pairs:
                    pairs.append(card)

        return pairs

    def getThreeOfAKind(self):
        vals = []
        three = []
        for card in self.cards:
            vals.append(card[0])
        for card in vals:
            if vals.count(card) == 3:
                if card not in three:
                    three.append(vals)
        return three

    def getStraight(self):
        vals = []
        flag = True
        for card in self.cards:
            vals.append(card[0])
        for i in range(len(vals)-1):
            if vals[i] == vals[i+1] - 1:
                pass
            else:
                flag = False
        if flag:
            return vals[4]
        else:
            return 0

    def getFlush(self):
        suits = []
        for card in self.cards:
            suits.append(card[1])

        if suits.count(suits[0]) == 5:
            return self.cards[4][0]
        else:
            return 0

    def getFullHouse(self):
        if len(self.getPairs()) == 1 and len(self.getThreeOfAKind()) == 1:
            return self.getThreeOfAKind()[0] * 1000 + self.getPairs()[0]
        else:
            return 0

    def getFourOfAKind(self):
        vals = []
        four = []
        for card in self.cards:
            vals.append(card[0])
        for card in vals:
            if vals.count(card) == 4:
                if card not in four:
                    four.append(vals)
        return four

    def getStraighFlush(self):
        if self.getFlush() != 0 and self.getStraight() != 0:
            return self.cards[4][0]
        else:
            return 0

    def evaluate(self):
        if self.getStraighFlush() != 0:
            self.handValue = [9, self.getStraighFlush()]
        elif self.getFourOfAKind():
            self.handValue = [8, self.getFourOfAKind()[0]]
        elif self.getFullHouse() != 0:
            self.handValue = [7, self.getFullHouse()]
        elif self.getFlush() != 0:
            self.handValue = [6, self.getFlush()]
        elif self.getStraight() != 0:
            self.handValue = [5, self.getStraight()]
        elif self.getThreeOfAKind() != []:
            self.handValue = [4, self.getThreeOfAKind()[0]]
        elif self.getPairs() != []:
            if len(self.getPairs()) == 2:
                self.handValue = [3, max(self.getPairs())*1000 + min(self.getPairs())]
            else:
                self.handValue = [2, self.getPairs()[0]]
        else:
            self.handValue = [1, self.getHighCard()]


    def __str__(self):
        return "cards: " + str(self.cards) + "\n" + "hand value: " + str(self.handValue)

winsBy1 = 0

with open("p054_poker.txt", "r") as inputFile:
    for line in inputFile:
        player1 = hand(line[0:14])
        player2 = hand(line[15:])
        player1.evaluate()
        player2.evaluate()

        if player1.handValue[0] > player2.handValue[0]:
            winsBy1 += 1
        elif player1.handValue[0] == player2.handValue[0] and player1.handValue[1] > player2.handValue[1]:
            winsBy1 += 1
        elif player1.handValue[0] == player2.handValue[0] and player1.handValue[1] == player2.handValue[1]:
            for i in range(5):
                if player1.getNextHighestCard(i) > player2.getNextHighestCard(i):
                    winsBy1 += 1
                elif player1.getNextHighestCard(i) < player2.getNextHighestCard(i):
                    break
                else:
                    continue

print(winsBy1)