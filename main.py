# Love Letter

from classes import Deck, Player

if __name__ == '__main__':
#    while True:
    print('\n')
    print('*' * 40)
    print('Jeu Love Letter')
    print('*' * 40)
    
    nPlayers = 2 # int(input('Veuillez entrer le nombre de joueurs (2-4) : '))
    
    # List of players
    players = []
    
    for i in range(nPlayers):
        players.append(Player(f'Joueur {i + 1}')) # input(f'Nom joueur {i + 1} : ')))
            
    deck = Deck()
    
    # Initial draw for each player
    for player in players:
        player.draw(deck.deal())
    
    # One card is discarded in the beginning
    discard = deck.deal()
    
    # Initialize to first turn
    turn = 1
            
    while len(deck) > 0:
        print(f'\n----- Tour {turn} -----')
        
        for player in players:
            player.draw(deck.deal())
            
            print(f'\nMain de {player.name} : {player}')
            choice = int(input('-> Quelle carte voulez-vous jouer? '))
        
            card = player.deck[choice - 1]
        
            if card.char == 'Guard':
                
                
            # elif card.char == 'Priest':
                
                                    
            # elif card.char == 'Baron':
                 
                           
            # elif card.char == 'Handmaid':
                
                            
            # elif card.char == 'Prince':
                
                                    
            # elif card.char == 'King':
                
                                    
            # elif card.char == 'Countess':
                
                                    
            # elif card.char == 'Princess':
            
            player.discard(choice - 1)
                 
        
        
        
        
        
        
        
            if len(deck) == 0:
                break
            
        turn += 1
            
    print('==== Fin de la partie! Le gagnant est : ')

    

        # if input('Voulez-vous jouer une autre partie? (o/n) : ') != 'o':
        #     break

