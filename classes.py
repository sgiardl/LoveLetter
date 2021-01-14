# Love Letter
# By : Simon Giard-Leroux, P.Eng.
# 2021

from random import shuffle

class Players:
    def __init__(self):
        self.list = []

        nPlayers = 4  # int(input('Veuillez entrer le nombre de joueurs (2-4) : '))

        for i in range(nPlayers):
            self.list.append(Player(f'Joueur {i + 1}'))  # input(f'Nom joueur {i + 1} : ')))

    def choosePlayer(self, player, includeSelf):
        print('\nJoueurs :')

        otherplayersIDs = []

        i = 1

        for player2 in self.list:
            if player2 != player or includeSelf:
                print(f'{i} : {player2.name}')
                otherplayersIDs.append(i)
            i += 1

        while True:
            chosenPlayerID = int(input('\n-> Quel joueur voulez-vous désigner? '))

            if chosenPlayerID in otherplayersIDs:
                chosenPlayer = self.list[chosenPlayerID - 1]

                if chosenPlayer.protected:
                    if input('\nCe joueur est protégé par la carte Handmaid!\n' +
                          '\nVoulez-vous gaspiller la carte? (o/n)') == 'o':
                        # to prevent loop if all other players are protected
                        chosenPlayer = None
                        break
                else:
                    break

        return chosenPlayer

    def removePlayer(self, player):
        print(f'\n{player.name} est éliminé de la partie!')
        self.list.remove(player)

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.discardDeck = []
        self.protected = False

    def draw(self, card, explicit):
        self.deck.append(card)

        if explicit:
            print(f'\nVous avez pigé une carte {card.char}!')

        return card.char

    def __str__(self):
        chars = []

        i = 1

        for card in self.deck:
            chars.append(f'{i} : {card.char}')
            i += 1

        return f'{chars}'

    def discard(self, index):
        discaredCard = self.deck.pop(index)
        self.discardDeck.append(discaredCard)

        return discaredCard

    def getDeckCardsChars(self):
        chars = []

        for card in self.deck:
            chars.append(card.char)

        return chars

    def give(self, index, otherPlayer):
        card = self.deck.pop(index)
        otherPlayer.deck.append(card)
        print(f'\n{self.name} a donné une carte {card.char} à {otherPlayer.name}!')

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