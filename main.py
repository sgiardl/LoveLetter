# Love Letter

from classes import Deck, Players

if __name__ == '__main__':
#    while True:
    print('\n')
    print('*' * 40)
    print('Jeu Love Letter')
    print('*' * 40)
    
    players = Players()
    deck = Deck()
    
    # Initial draw for each player
    for player in players.list:
        player.draw(deck.deal())
    
    # One card is discarded in the beginning
    discard = deck.deal()
    
    # Initialize to first turn
    turn = 1
            
    while len(deck) > 0 and len(players.list) > 1:
        print(f'\n----- Tour {turn} -----')

        players.resetProtected()

        for player in players.list:
            player.draw(deck.deal())
            
            print(f'\nMain de {player.name} : {player}')

            while True:
                choice = int(input('-> Quelle carte voulez-vous jouer? '))

                if choice == 1 or choice == 2:# player.getDeckCardsIDs():
                    break

            card = player.deck[choice - 1]

            if card.char == 'Guard':
                chosenPlayer = players.choosePlayer(player, includeSelf=False)

                if chosenPlayer != None:
                    #  Guard cannot be named as the type of card.
                    chars = ['Priest', 'Baron', 'Handmaid',
                             'Prince', 'King', 'Countess', 'Princess']

                    i = 1

                    charIDs = []

                    print('\nChoix de cartes :')

                    for char in chars:
                        print(f'{i} : {char}')
                        charIDs.append(i)
                        i += 1

                    while True:
                        chosenCharID = int(input('-> Quelle carte voulez-vous nommer? '))

                        if chosenCharID in charIDs:
                            chosenChar = chars[chosenCharID - 1]
                            break

                    if chosenChar in chosenPlayer.getDeckCardsChars():
                        print(f'\nVous avez réussi à deviner la carte de {chosenPlayer.name}.')
                        players.list.remove(chosenPlayer)
                    else:
                        print(f'\nVous avez échoué à deviner la carte de {chosenPlayer.name}.')

            elif card.char == 'Priest':
                chosenPlayer = players.choosePlayer(player, includeSelf=False)

                if chosenPlayer != None:
                    print(f'\nCarte de {chosenPlayer.name} : {chosenPlayer}')

            elif card.char == 'Baron':
                chosenPlayer = players.choosePlayer(player, includeSelf=False)

                if chosenPlayer != None:
                    chosenPlayerCard = chosenPlayer.deck[0]

                    if choice == 1:
                        playerCard = player.deck[1]
                    elif choice == 2:
                        playerCard = player.deck[0]

                    if playerCard.strength > chosenPlayerCard.strength:
                        print(f'\nLa carte {playerCard.char} ({playerCard.strength}) ' +
                              f'de {player.name} bat la carte {chosenPlayerCard.char} ' +
                              f'({chosenPlayerCard.strength}) de {chosenPlayer.name}!\n\n' +
                              f'{chosenPlayer.name} est éliminé de la partie!')
                        players.list.remove(chosenPlayer)
                    elif chosenPlayerCard.strength > playerCard.strength:
                        print(f'\nLa carte {chosenPlayerCard.char} ({chosenPlayerCard.strength}) ' +
                              f'de {chosenPlayer.name} bat la carte {playerCard.char} ' +
                              f'({playerCard.strength}) de {player.name}!\n\n' +
                              f'{player.name} est éliminé de la partie!')
                        players.list.remove(player)
                    else:
                        print(f'\nLa carte {playerCard.char} ({playerCard.strength}) ' +
                              f'de {player.name} est identique à la carte {chosenPlayerCard.char} ' +
                              f'({chosenPlayerCard.strength}) de {chosenPlayer.name}!\n\n' +
                              f"Personne n'est éliminé de la partie!")

            elif card.char == 'Handmaid':
                print('\nVous êtes protégé(e) pour le reste du tour!')
                player.protected = True
                            
            # elif card.char == 'Prince':
                
                                    
            # elif card.char == 'King':
                
                                    
            # elif card.char == 'Countess':
                
                                    
            # elif card.char == 'Princess':
            
            player.discard(choice - 1)
                 
        
        
        
        
        
        
        
            if len(deck) == 0 or len(players.list) == 1:
                break
            
        turn += 1
            
    print(f'\n==== Fin de la partie! Le gagnant est : {player.name}!====')

    

        # if input('Voulez-vous jouer une autre partie? (o/n) : ') != 'o':
        #     break

