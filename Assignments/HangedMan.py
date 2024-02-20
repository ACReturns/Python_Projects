import random

Option_List = ['Alligator', 'Snake', 'Rabbit', 'Dog', 'Raven', 'Gundam']
Name = input('Please enter the name of the person who created this game: ')
print('This game was made by the amazing ' + Name + '!')
print('Welcome to my Guessing Game!')
print('In this program, you will try to guess a word that I chose')
print('Good Luck!')

def start():
    Player_Name = input('What is the name of the player?')
    print('Greetings, ' + Player_Name + '! It\'s time to guess!')
    Secret_Word = random.choice(Option_List).lower()
    Guesses = ''
    Turns_Left = 11
    while Turns_Left > 0:
        Wrong_Answers = 0
        for Letter in Secret_Word:
            if Letter in Guesses:
                print(Letter)
            else:
                print('_')
                Wrong_Answers += 1

        if Wrong_Answers == 0:
            print('YOU WIN! You guessed my word: ' + Secret_Word + '!!!!')
            break

        Guess = input('Guess a letter here: ').lower()
        Guesses += Guess

        if Guess not in Secret_Word:
            Turns_Left -= 1
            print('OOps! This letter is not in the word. Please try again.')
            print('You have ' + str(Turns_Left) + ' more guesses left. You can do it!')
            if Turns_Left == 0:
                print('Game Over!')

    def Play_Again():
        Again = input('Would you like to play again? ').lower()
        if Again == 'No'.lower():
            quit()
        elif Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thankk you!')
            Play_Again()

    Play_Again()
    
start()
