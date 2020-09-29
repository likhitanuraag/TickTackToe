from os import system
import sys
global bool
global boolWin

class GameState:
    def __init__(self, dim, board):
        self.n = dim
        self.t = board       
    
    def gameLoop(self):
        global Bool
        [print(self.t[x], end='\n') for x in range(self.n)]
        for game_loop in range(self.n*self.n):
            Bool = True
            while (Bool):
                if ((game_loop+1) % 2) != 0:  
                    Player().UpdateBoard("X")  
                else:    
                    Player().UpdateBoard("O")

class Player(GameState):
    def __init__(self, **kargs):
        GameState.__init__(self, dim, board)
        
    def Winner(self, player):
        global boolWin
        boolWin = False
        system('cls') 
        self.display_board(board)
        print(f"\n The winner is {player}")
        if input("Press enter to exit: ") == "":
            sys.exit()
        
    def UpdateBoard(self, player):
        global Bool
        while True:
            try:
                pos_val = int(input(f"Enter position for player {player}: "))
            except:
                pass
            else:
                break
            print("Wrong value entered, try again")
        i = 1
        for j in range(self.n):
            for k in range(self.n):
                if (i == pos_val):
                    if (self.t[j][k] == "*"):
                        self.t[j][k] = player
                        Bool = False
                        if (Board().check_board(self.t, player)):
                            self.Winner(player)
                    else:
                        print("Position of the value is occupied, please enter right value")
                i += 1  
        system('cls')        
        self.display_board(board)
        
    def display_board(self, board):
        [print(board[x], end='\n') for x in range(self.n)]  

class Board(GameState):
    def __init__(self, **kargs):
        GameState.__init__(self, dim, board)
        
    def similarList(self, list):
        return all(x == list[0] for x in list)
    
    def check_board(self, arr, player):
        for l in range(self.n):
            col = []
            if (self.similarList(arr[l]) == True) and ("*" not in arr[l]):
                return True                 #Horizontal row check
            for m in range(self.n):
                col.append(arr[m][l])
            if (self.similarList(col) == True) and ("*" not in col):
                return True                #vertical column check
            else:
                continue
        diag1, diag2 = [], []
        for d in range(self.n):
            diag1.append(arr[self.n-(d+1)][d])
            diag2.append(arr[d][d])
        if (self.similarList(diag1) == True) or (self.similarList(diag2) == True):
            if ("*" not in diag1) or ("*" not in diag2):
                return True                #Diagonal check
            else:
                pass

if __name__ == "__main__":
    if input("Press enter to begin the game or type exit to exit the game :") != "":
        sys.exit()
    global boolWin
    bool_ent = True
    while bool_ent:    
        while True:
            try:
                dim = int(input("enter the dimension: ")) 
            except:
                pass
            else:
                break
            print("Wrong value entered, try again")
        try:
            if ((dim) % 3) != 0:
                print("Please enter an appropriate dimension value, like 3 for 3x3 or 6 for 6x6. Only multiples of three are accepted.")
            else:
                system('cls')
                break
        except:
            pass
        else:
            bool_ent = True
    board = [["*" for x in range(dim)] for y in range(dim)]
    boolWin = True
    root = GameState(dim, board)
    root.gameLoop()
    print("Its a Draw, No one wins")
    if boolWin == True:
        if input("Press enter to exit: ") == "":
            sys.exit()