import numpy as np
import sys

global Bool
Bool = True

class Game:
    def __init__(self, n, t):
        self.n = n
        self.t = t
    
    def similarList(self, list):
        return all(x == list[0] for x in list)
    
    def goalCheck(self, arr, player):
        for l in range(self.n):
            kk = []
            if (self.t[l] == player).all() and ("*" not in kk):
                #Horizontal check
                return True
            for m in range(self.n):
                kk.append(arr[m, l])
            if (self.similarList(kk) == True) and ("*" not in kk):
                #vertical check
                return True
            else:
                continue
        dd1 = []
        dd2 = []
        for d in range(self.n):
            dd1.append(arr[self.n-(d+1), d])
            dd2.append(arr[d, d])
        if (self.similarList(dd1) == True) or (self.similarList(dd2) == True):
            if ("*" not in dd1) or ("*" not in dd2):
                #Diagonal check
                return True
            else:
                pass

    def Winner(self, player):
        BoolWin = True
        print(self.t)
        print(f"the winner is {player}")
        if input("If you want to play the game again, press enter. If not, type exit to exit: ") == "":
            sys.exit()
        while (BoolWin):
            BoolWin = True
        
    def Inserter(self, player):
        global Bool
        try:
            pos_val = int(input(f"Enter position for player {player}: "))
        except ValueError:
            print("please enter a valid number")    
        i = 1
        for j in range(self.n):
            for k in range(self.n):
                if (i == pos_val):
                    if (self.t[j, k] == "*"):
                        self.t[j, k] = player
                        Bool = False
                        if (self.goalCheck(self.t, player)):
                            self.Winner(player)
                    else:
                        print("Position of the value is occupied, please enter right value")
                i += 1                   
        print(self.t)
    
    def gameLoop(self):
        global Bool
        print(self.t)
        for game_loop in range(self.n*self.n):
            Bool = True
            while (Bool):
                print(game_loop)
                if ((game_loop+1) % 2) != 0:  
                    self.Inserter("X")  
                else:    
                    self.Inserter("O")
    
    
if __name__ == "__main__":
    n = int(input("enter the dim: "))
    t = np.full((n,n), "*")
    root = Game(n, t)
    root.gameLoop()
    