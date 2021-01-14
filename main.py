# Love Letter
# By : Simon Giard-Leroux, P.Eng.
# 2021

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
        print('-' * 40)
        print(f'{player.name} :')
        player.draw(deck.deal(), explicit=True)
    
    # One card is discarded in the beginning
    discard = deck.deal()

    while len(deck) > 0 and len(players.list) > 1:
        for player in list(players.list): # list() to copy list so you can delete active player in loop
            print('-' * 40)
            print(f'{player.name} :')

            if player.protected:
                player.protected = False
                print("\nVous n'êtes plus protégé(e) par la carte Handmaid!")

            firstCard = player.deck[0]
            secondCard = player.draw(deck.deal(), explicit=True)

            if firstCard == 'Countess' and (secondCard == 'King' or secondCard == 'Prince'):
                print('\nVous avez à la fois une carte Countess et une carte King ou Prince!')
                print('\nVous avez jeté votre carte Countess!')
                player.discard(0)

            elif secondCard == 'Countess' and (firstCard == 'King' or firstCard == 'Prince'):
                print('\nVous avez à la fois une carte Countess et une carte King ou Prince!')
                print('\nVous avez jeté votre carte Countess!')
                player.discard(1)

            else:
                print(f'\nVotre main : {player}')

                while True:
                    choice = int(input('\n-> Quelle carte voulez-vous jouer? '))

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
                            chosenCharID = int(input('\n-> Quelle carte voulez-vous nommer? '))

                            if chosenCharID in charIDs:
                                chosenChar = chars[chosenCharID - 1]
                                break

                        if chosenChar in chosenPlayer.getDeckCardsChars():
                            print(f'\nVous avez réussi à deviner la carte de {chosenPlayer.name}.')
                            players.removePlayer(chosenPlayer)
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
                                  f'({chosenPlayerCard.strength}) de {chosenPlayer.name}!\n')
                            players.removePlayer(chosenPlayer)

                        elif chosenPlayerCard.strength > playerCard.strength:
                            print(f'\nLa carte {chosenPlayerCard.char} ({chosenPlayerCard.strength}) ' +
                                  f'de {chosenPlayer.name} bat la carte {playerCard.char} ' +
                                  f'({playerCard.strength}) de {player.name}!\n')
                            players.removePlayer(player)

                        else:
                            print(f'\nLa carte {playerCard.char} ({playerCard.strength}) ' +
                                  f'de {player.name} est identique à la carte {chosenPlayerCard.char} ' +
                                  f'({chosenPlayerCard.strength}) de {chosenPlayer.name}!\n\n' +
                                  f"Personne n'est éliminé de la partie!")

                elif card.char == 'Handmaid':
                    print('\nVous êtes protégé(e) pour le reste du tour!')
                    player.protected = True

                elif card.char == 'Prince':
                    chosenPlayer = players.choosePlayer(player, includeSelf=True)

                    if chosenPlayer == player:
                        if choice == 1:
                            discardedCard = chosenPlayer.discard(1)
                        elif choice == 2:
                            discardedCard = chosenPlayer.discard(0)
                    else:
                        discardedCard = chosenPlayer.discard(0)

                    print(f'\n{chosenPlayer.name} a jeté une carte {discardedCard.char}!')

                    drawnCard = chosenPlayer.draw(deck.deal(), explicit=False)

                    print(f'\n{chosenPlayer.name} a pigé une carte {drawnCard}!')

                elif card.char == 'King':
                    chosenPlayer = players.choosePlayer(player, includeSelf=False)

                    if chosenPlayer != None:
                        if choice == 1:
                            index = 1
                        elif choice == 2:
                            index = 0

                    player.give(index, chosenPlayer)
                    chosenPlayer.give(0, player)

                # elif card.char == 'Countess':
                    # nothing happens, Countess effect is only at draw

                elif card.char == 'Princess':
                    players.removePlayer(player)

                player.discard(choice - 1)

            if len(deck) == 0 or len(players.list) == 1:
                break

    print(f'\n==== Fin de la partie! Le gagnant est : {player.name}!====')

        # if input('Voulez-vous jouer une autre partie? (o/n) : ') != 'o':
        #     break