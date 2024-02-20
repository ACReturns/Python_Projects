def start():
    print('This is my rock, paper, scissors game!')
    Player_One = 'Don'
    Player_Two = 'Vivi'

    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == 'rock' and Player_Two_Choice == 'paper':
            return('Paper covers rock! ' + Player_Two + ' win!')
        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'scissors':
            return('Scissors cuts paper! ' + Player_Two + ' wins!')
        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'rock':
            return('Rock smashes scissors! ' + Player_Two + ' wins!')
        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'rock':
            return('Paper covers rock! ' + Player_One + ' win!')
        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'paper':
            return('Scissors cuts paper! ' + Player_One + ' wins!')
        elif Player_One_Choice == 'rock' and Player_Two_Choice == 'scissors':
            return('Rock smashes scissors! ' + Player_One + ' wins!')
        elif Player_One_Choice == Player_Two_Choice:
            return('Don & Vivi tied!')
        else:
            return('Please type Rock, Paper or Scissors!')

    Player_One_Choose = input('Does ' + Player_One +
                              ' choose Rock, Paper or scissors? ').lower()
    Player_Two_Choose = input('Does ' + Player_Two +
                              ' choose Rock, Paper or scissors? ').lower()

    print(choices(Player_One_Choose, Player_Two_Choose))
    
    def Play_Again():
        Again = input('Would you like to play the game again? ').lower()
        if Again == 'Yes'.lower():
            start()
        if Again == 'No'.lower():
            quit()
        else:
            print('Please enter Yes or No')
            Play_Again()
    Play_Again()
start()

start()
