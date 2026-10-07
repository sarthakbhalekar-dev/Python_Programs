from random import choice

while True:
    m=input("Do You Want To Play Rock, Paper & Scissors? [y/n]: ")
    if m=='y':
        player=input("Enter Your Choice - Rock , Paper Or Scissors? [Choose From r,p or s]: ")
        c=['r','p','s']
        c_choice=choice(c)
        print(c_choice,'Versus',player ,'!')
        if player == c_choice:
            print('Draw!')
        elif (player=='r' and c_choice=='p'):
            print('Computer Wins! Try Again!')
        elif (player=='r' and c_choice=='s'):
            print('Player Wins! Great Job!')
        elif (player=='s' and c_choice=='p'):
            print('Player Wins! Great Job!')
        elif (player=='s' and c_choice=='r'):
            print('Computer Wins! Try Again!')
        elif (player=='p' and c_choice=='s'):
            print('Computer Wins! Try Again!')
        else:
            print("Player Wins! Great Job!")
              
         
    elif m=='n':
        print("Good Bye!See You Next Time!")
        break
    else:
        print("Please Enter Correct Option.")
    
