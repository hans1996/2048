import random
import itertools
#number = random.choice( [1,2,4] )
#x, y = random.choice([(x,y) for x ,y in itertools.product([0,1,2,3],[0,1,2,3]) if self.board[x][y]== 0]) 
#print(x,y)

board = [[0,0,16,0],[0,20483,0,0],[0,0,0,0],[0,0,0,0]]
#print(board)
del board[:]
#print(board)
board1= [[0,0,16,0],[0,20483,0,0],[0,0,0,0],[0,0,0,0]]
board.extend(board1)

#print(*board)
#print(list(itertools.chain(*board)))

#print(*board)
def up():
    pass

def down():
    pass

def left():
    pass

def right():
    pass


#board = {'up':up , 'down':down , 'left':left , 'right':right}[right]



board1= [[0,0,16,0],[0,20483,0,0],[0,0,0,0],[0,0,0,0]]

[ n for n in itertools.chain(*board1)]

itertools.chain(*board1)

#print(board1)
#print(max(list(itertools.chain(*board1))))

#if max(list(itertools.chain(*board1))) >= 131072 :
#    print(0)
#print(1)

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
#        return [trim([seqs[0], seqs[1]*2, 0 , seqs[3]],direction=direction),seqs[1]*2]
#        seqs[0], seqs[1] = seqs[0]*2 , 0
#    if seqs[2] and seqs[3] and seqs[2] == seqs[3]:
#        seqs[2], seqs[3] = seqs[2]*2 , 0
#    return trim(seqs, direction=direction)


def sum_seqs(seqs, direction=0):
    points = 0
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

#def sum_seqs1(seqs, direction=0):
    
    if seqs[1] and seqs[2] and seqs[1] == seqs[2]:
        return trim([seqs[0], seqs[1]*2, 0 , seqs[3]],direction=direction)
    if seqs[0] and seqs[1] and seqs[0] == seqs[1]:
        seqs[0], seqs[1] = seqs[0]*2 , 0
    if seqs[2] and seqs[3] and seqs[2] == seqs[3]:
        seqs[2], seqs[3] = seqs[2]*2 , 0
    return trim(seqs, direction=direction)

#print(trim([0,2,2,0],))    
#print(sum_seqs(trim([1,2,2,0])))
#print(sum_seqs(trim([2,2,0,0])))
#print(sum_seqs(trim([1,2,4,4])))
#print(sum_seqs(trim([2,2,4,4])))

print(sum_seqs(trim([1,2,2,0]))[0])
print(sum_seqs(trim([2,2,0,0])))
print(sum_seqs(trim([1,2,4,4])))
print(sum_seqs(trim([2,2,4,4])))
print(sum_seqs(trim([4,2,6,8])))
print(sum_seqs(trim([4,2,6,8]))[0])

