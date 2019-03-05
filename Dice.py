import random # Using the random library to generate random numbers

# Variables value is randomlygenerated between 1 and 6 !


def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

def main():
    player1 = 0
    Player1wins = 0  # for second If statement
    Player2 = 0
    Player2wins = 0   # for second If statement
    rounds = 1
    
    while rounds != 4:
        print("Round  " +str ( rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print (" Player 1 roll : " + str(player1))
        print (" Player 2 roll : " + str(player2))

        if player1 == player2:
            print ("Draw !")
        elif player1 > player2:
            Player1wins = Player1wins + 1
            print ("Player 1 wins 1")
        else:
            Player2wins = Player2wins + 1
            print ("Player 2 wins 1")

        rounds = rounds + 1

    if Player1wins == Player2wins:
        print ("Draw !")
    elif Player1wins  > Player1wins:
        print ("Player 1 wins 1")
    else:
        print ("Player 2 wins 1")
     
        

main()
