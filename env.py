# coding=utf8

import sys
import os
import random
import itertools


def trim(seqs, direction=0):
    """
    ex: "[0,2,2,0]     #right to left 
        step 1. [2 2]   #remove 0
        step 2. [2,2] + [0,0,0,0] = [2,2,0,0,0,0]  
        step 3. [2,2,0,0,0,0][:4] = [2,2,0,0]

    """
    return([0,0,0,0] + [n for n in seqs if n])[-4:] if direction else ([n for n in seqs if n] + [0,0,0,0] )[:4]


#def sum_seqs(seqs, direction=0):
    
#    if seqs[1] and seqs[2] and seqs[1] == seqs[2]:
#        return trim([seqs[0], seqs[1]*2, 0 , seqs[3]],direction=direction)
#    if seqs[0] and seqs[1] and seqs[0] == seqs[1]:
#        seqs[0], seqs[1] = seqs[0]*2 , 0
#    if seqs[2] and seqs[3] and seqs[2] == seqs[3]:
#        seqs[2], seqs[3] = seqs[2]*2 , 0
#    return trim(seqs, direction=direction)


def sum_seqs(seqs, direction=0):
    if seqs[0] and seqs[1] and seqs[2] and seqs[3] and seqs[0] == seqs[1] and seqs[2] == seqs[3] : 
        seqs[0], seqs[1] , seqs[2] ,seqs [3] = seqs[0]*2 , seqs[3]*2, 0, 0
        return [trim(seqs, direction=direction) , seqs[0] + seqs[1]]

    if seqs[1] and seqs[2] and seqs[1] == seqs[2]:
        return [trim([seqs[0], seqs[1]*2, 0 , seqs[3]],direction=direction), seqs[1]*2]
    if seqs[0] and seqs[1] and seqs[0] == seqs[1]:
        seqs[0], seqs[1] = seqs[0]*2 , 0
        return [trim(seqs, direction=direction) , seqs[0] ]
    if seqs[2] and seqs[3] and seqs[2] == seqs[3]:
        seqs[2], seqs[3] = seqs[2]*2 , 0
        return [trim(seqs, direction=direction) , seqs[2]]

    return [ trim(seqs, direction=direction ) , 0 ]



def up(board):
    emptylist=[]
    for col in [0,1,2,3]:
        colpoints = (sum_seqs(trim([row[col] for row in board]))[1])
        emptylist.append(colpoints)
        for _idx, n  in enumerate(sum_seqs(trim([row[col] for row in board]))[0]):
            board[_idx][col] = n
    point = sum(emptylist)
    #print('this move points is ',point)
    return board , point
    
def down(board):
    emptylist=[]
    for col in [0,1,2,3]:

        colpoints = (sum_seqs(trim([row[col] for row in board]))[1])
        emptylist.append(colpoints)
        for _idx, n  in enumerate(sum_seqs(trim([row[col] for row in board],direction=1),direction=1)[0]):
            board[_idx][col] = n
    point = sum(emptylist)
    #print('this move points is ',point)
    return board ,point

def left(board):
    emptylist=[]
    for row in board:
        rowpoints=sum_seqs(trim(row))[1]
        emptylist.append(rowpoints)
    #print('this move points is ',sum(emptylist))
    point = sum(emptylist)
    return [ sum_seqs(trim(row))[0] for row in board ] , point

def right(board):
    emptylist=[]
    for row in board:
        rowpoints=sum_seqs(trim(row))[1]
        emptylist.append(rowpoints)
    #print('this move points is ',sum(emptylist))
    point = sum(emptylist)
    return [ sum_seqs(trim(row , direction=1),direction=1)[0] for row in board] , point



class Game:
    def __init__(self, board=[], controls=["w","s","a","d"]):
        self.board = board
        self.controls = controls
        
    
    def random_init(self):
        # three init random number 1 , 2 , 4
        number = random.choice( [2] )
        # finding the empty board grid fill in random number 
        x, y = random.choice([(x,y) for x ,y in itertools.product([0,1,2,3],[0,1,2,3]) if self.board[x][y]== 0])
        self.board[x][y] = number
    
    
    def print_screen(self):
    
        # find out which value is the largest   
        largest = self.board[0][0] 
        for row in self.board:
            for element in row:
                if element > largest:
                    largest = element

        numSpaces = len(str(largest))    
        for row in self.board:        
            currRow = "|"
            for element in row:
                if element == 0 :
                    currRow += " " * numSpaces + "|"
                else:
                    currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
            print(currRow)
        print()


    def logic(self, control):
        

         # generate a new board based on our controls
        # copy a new board

        board = {'w':up , 's':down , 'a':left , 'd':right}[control]([[c for c in r] for r in self.board])[0]
        

        # if we move -> we generate a new random number

        if board != self.board:

   
            del self.board[:]
            self.board.extend(board)
            
            # unpack list && and connect list together 
            if max(list(itertools.chain(*board))) >= 2048 :
                return 1 , "you win "

            self.random_init()
            #print(self.board)
        else:
            # cant move
            if not [ 1 for g in [f(board)[0] for f in [up, down, left, right]] if g != self.board]:
                return -1, "you lost"          
        return 0, ''   #1 ,  win # -1 lost  # 0 continue


    def main_loop(self):
        del self.board[:] # cleaning the board 
        self.board = [ [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0] ]
        self.random_init()
        self.random_init()
        reward=[]
        while True:
            self.print_screen()
            control = input('input w(up) & s(down) & a(left) & d(right): ')

            #control = random.choice(['w','s','a','d'])
            if control in self.controls:
                themovereward={'w':up , 's':down , 'a':left , 'd':right}[control]([[c for c in r] for r in self.board])[1]
                reward.append(themovereward)
                status, info = self.logic(control)

                print(themovereward)          
                print('my total reward is  :' ,sum(reward))

                print(self.board)

                if status:
                    print(info)
                    if input('start another game?').lower() == "y":
                        break
                    else:
                        sys.exit(0)
        self.main_loop()

if __name__ == "__main__":
    Game().main_loop()
