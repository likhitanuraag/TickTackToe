import sys
global bool

class GameState:
    def __init__(self, n, t):
        self.n = n
        self.t = t       
    
    def gameLoop(self):
        global Bool
        [print(self.t[x], end='\n') for x in range(self.n)]
        for game_loop in range(self.n*self.n):
            Bool = True
            while (Bool):
                print(game_loop)
                if ((game_loop+1) % 2) != 0:  
                    Player().UpdateBoard("X")  
                else:    
                    Player().UpdateBoard("O")

class Player(GameState):
    def __init__(self, **kv):
        GameState.__init__(self, n, t)
        
    def Winner(self, player):
        BoolWin = True
        self.display_board(t)
        print(f"the winner is {player}")
        if input("If you want to play the game again, press enter. If not, type exit to exit: ") == "":
            sys.exit()
        while (BoolWin):
            BoolWin = True
        
    def UpdateBoard(self, player):
        global Bool
        try:
            pos_val = int(input(f"Enter position for player {player}: "))
        except ValueError:
            print("please enter a valid number")    
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
        self.display_board(t)
        
    def display_board(self, board):
        [print(board[x], end='\n') for x in range(self.n)]  

class Board(GameState):
    def __init__(self, **kv):
        GameState.__init__(self, n, t)
        
    def similarList(self, list):
        return all(x == list[0] for x in list)
    
    def check_board(self, arr, player):
        for l in range(self.n):
            kk = []
            if (self.similarList(arr[l]) == True) and ("*" not in arr[l]):
                return True                 #Horizontal check
            for m in range(self.n):
                kk.append(arr[m][l])
            if (self.similarList(kk) == True) and ("*" not in kk):
                return True                #vertical check
            else:
                continue
        dd1, dd2 = [], []
        for d in range(self.n):
            dd1.append(arr[self.n-(d+1)][d])
            dd2.append(arr[d][d])
        if (self.similarList(dd1) == True) or (self.similarList(dd2) == True):
            if ("*" not in dd1) or ("*" not in dd2):
                return True                #Diagonal check
            else:
                pass

if __name__ == "__main__":
    n = int(input("enter the dim: "))
    t = [["*" for x in range(n)] for y in range(n)]
    root = GameState(n, t)
    root.gameLoop()
