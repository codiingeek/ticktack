import itertools

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
     # horizontal
    for row in game:
       # print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True
     # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True
     # / diagonal    
    diag1 = []
    for col, row in enumerate(reversed(range(len(game)))):
        diag1.append(game[row][col])     
       
    if all_same(diag1):
        print(f"Player {diag1[0]} has won Diagonally (/)")
        return True
    # \ diagonal
    diag2 = []
    for id in range(len(game)):
        diag2.append(game[id][id])
    if all_same(diag2):
        print(f"Player {diag2[0]} has won Diagonally (\\)")
        return True
    return False

def game_board(game,player=0,row=0,column=0,display=False):
    try:    
        if game[row][column]!=0:
            print("already occupied ")
            return game, False
        if not display:
            game[row][column]=player;
        print("   0  1  2")
        for count , row in enumerate(game):
            print(count,row)
        return game, True
    except Exception as e:
        print(e)
        return game, False

#game, _=game_board(game,1,1,1,False)

play=True
players=[1,2]
while play:
    game_size=int(input("enter game size"))
    game=[]
    for i in range(game_size):
        row=[]
        for j in range(game_size):
            row.append(0)
        game.append(row)
    
    game_won=False
    game, _=game_board(game,display=True)
    player_choice=itertools.cycle(players)
    while not game_won:
        current_player=next(player_choice)
        print(f"Current Player: {current_player}")
        played=False
        while not played:
            column_choice=int(input("enter column: "))
            row_choice=int(input("enter row: "))
            game, played=game_board(game,current_player,row_choice,column_choice)
        if win(game):
            game_won=True
            again=input("would like to play again(y/n)")
            if again.lower()=="y":
                print("restarting")
            elif again.lower()=="n":
                print("Byeee")
                play=False
            else: 
                print("not a valid answer")
                play=False
            
