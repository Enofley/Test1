import random

win = False

interation = 0
player_name = input(str('Write your Name: '))
print (f'Hello {player_name} its variables games!')

def game():
    record_max = 0
    record = 100
    Play_game = True  
    while (Play_game):
        pc_variable = random.randint(10,90)
        print(f'Your have {record} points!')
        print('PC make to guesses variables!')
        user = input('Write your answer: ')
        print(record)
        if int(user) == pc_variable :
            record += 10
            record_max += 10
            print(f'Great, you have {record} points')
        elif int(user) != pc_variable :
            record -= 10
            print(f'You wrong, you have {record} points')
        
        if record == 0 or record < 0:
            Play_game = False
            print('Game over')
            print(f'Good game, your max record this game : {record_max} points')
            start = input(('Write stop or Enter - start!: '))
            if start == 'stop' or start == "Stop":
                Play_game = False
            else:
                Play_game = True
                record = 100
        

game()



    
    
    


