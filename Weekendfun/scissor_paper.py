playerOne = str(input("Player1 enter 'rock' , 'paper' , 'scissors':  "))
playerTwo = str(input("Player2 enter 'rock' , 'paper' , 'scissors':  "))


if (playerOne == 'rock' and playerTwo == 'sciccors') or (playerOne == 'scissors' and playerTwo == 'paper') or (playerOne == 'paper' and playerTwo == 'rock'):
    print("Player1 wins")
    

elif (playerTwo == 'rock' and playerOne == 'sciccors') or (playerTwo == 'scissors' and playerOne == 'paper') or (playerTwo == 'paper' and playerOne == 'rock'):
    print("Player2 wins")
    
elif (playerOne == playerTwo):
    print("Tie")
