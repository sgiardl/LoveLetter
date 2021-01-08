# Love Letter

import random as rd

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def draw(self, card):
        self.deck.append(card)
        
    def __str__(self):
        chars = []
        
        i = 1
        
        for card in self.deck:
            chars.append(f'{i} : {card.char}')     
            
            i += 1
        
        return f'{chars}'
    
    def discard(self, index):
        self.deck.pop(index)



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
                
        rd.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
        
    def __len__(self):
        return len(self.deck)
    
    
    
    
    
    
    
    
    
    
    
    