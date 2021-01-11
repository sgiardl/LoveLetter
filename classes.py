# Love Letter

from random import shuffle

class Players:
    def __init__(self):
        self.list = []

        nPlayers = 2  # int(input('Veuillez entrer le nombre de joueurs (2-4) : '))

        for i in range(nPlayers):
            self.list.append(Player(i + 1, f'Joueur {i + 1}'))  # input(f'Nom joueur {i + 1} : ')))

    def resetProtected(self):
        for player in self.list:
            player.protected = False

    def choosePlayer(self, player, includeSelf):
        print('\nJoueurs :')

        otherplayersIDs = []

        for player2 in self.list:
            if player2 != player or includeSelf:
                print(f'{player2.id} : {player2.name}')
                otherplayersIDs.append(player2.id)

        while True:
            chosenPlayerID = int(input('-> Quel joueur voulez-vous désigner? '))

            if chosenPlayerID in otherplayersIDs:
                chosenPlayer = self.list[chosenPlayerID - 1]

                if chosenPlayer.protected:
                    if input('\nCe joueur est protégé par la carte Handmaid!\n' +
                          'Voulez-vous gaspiller la carte? (o/n)') == 'o':
                        # to prevent loop if all other players are protected
                        chosenPlayer = None
                        break
                else:
                    break

        return chosenPlayer

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        self.deck = []
        self.discardDeck = []
        self.protected = False

    def draw(self, card):
        # card.id = len(self.deck) + 1
        self.deck.append(card)

    def __str__(self):
        chars = []

        i = 1

        for card in self.deck:
            chars.append(f'{i} : {card.char}')
            i += 1

        return f'{chars}'

    def discard(self, index):
        self.discardDeck.append(self.deck.pop(index))

    def getDeckCardsChars(self):
        chars = []

        for card in self.deck:
            chars.append(card.char)

        return chars

class Card:
    def __init__(self, char, strength):
        self.char = char
        self.strength = strength

    def __str__(self):
        return f'{self.char}'

class Deck:
    def __init__(self):
        chars = ['Guard', 'Priest', 'Baron', 'Handmaid',
                 'Prince', 'King', 'Countess', 'Princess']
        
        strengths = [1, 2, 3, 4, 
                     5, 6, 7, 8]
        
        numbers = [5, 2, 2, 2,
                   2, 1, 1, 1]
        
        self.deck = []
        
        for i in range(len(chars)):
            for j in range(numbers[i]):
                self.deck.append(Card(chars[i], strengths[i]))
                
        shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
        
    def __len__(self):
        return len(self.deck)
    
    
    
    
    
    
    
    
    
    
    
    