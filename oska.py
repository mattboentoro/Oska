import copy
class Piece:
    #Container for the piece on the board
    def __init__(self):
        self.icon=""
        self.i=-1
        self.j=-1
    def print(self):
        #for debugging purposes
        print(self.icon)
        print("i= ",str(self.i))
        print("j= ",str(self.j))
def is_in_board(array,i,j):
    #check if the coordinate is in the board
    if((i>=0)&(j>=0)):
        if(i<len(array)):
            if(j<len(array[i])):
                return True
    return False
def is_upper_half(array,i,piece):
    #check if the piece is in the middle to upper half
    if(piece=="w"):
        return (i>=mid(array))
    else:
        return (i<=mid(array))
def mid(array):
    #return the mid point of the board
    return ((len(array)-1)/2)
def state(array):
    symbol=[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(array[i][j]!="-"):
                piece=Piece()
                piece.icon=array[i][j]
                piece.i=i
                piece.j=j
                symbol.append(piece)
    return symbol
def movegen(arr,color):
    #generate all possible moves for the current state of the board
    moves=[]
    token=state(arr)
    for item in token:
        if(item.icon==color):
            if(color=="b"):
                #move black
                if(is_upper_half(arr,item.i,color)!=True):
                    #not in upper half
                    if(is_in_board(arr,item.i-1,item.j)):
                        #check right
                        if(arr[item.i-1][item.j]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i-1][item.j]="b"
                            moves.append(arrcopy)
                        elif(arr[item.i-1][item.j]=="w"):
                            #occupied by enemy
                            if(is_upper_half(arr,item.i-1,color)!=True):
                               #lower half
                               if(is_in_board(arr,item.i-2,item.j)):
                                   if(arr[item.i-2][item.j]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i-1][item.j]="-"
                                        arrcopy[item.i-2][item.j]="b"
                                        moves.append(arrcopy)
                            else:
                                #upper half
                               if(is_in_board(arr,item.i-2,item.j+1)):
                                   if(arr[item.i-2][item.j+1]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i-1][item.j]="-"
                                        arrcopy[item.i-2][item.j+1]="b"
                                        moves.append(arrcopy)
                               
                    if(is_in_board(arr,item.i-1,item.j-1)):
                        #check left
                        if(arr[item.i-1][item.j-1]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i-1][item.j-1]="b"
                            moves.append(arrcopy)
                        elif(arr[item.i-1][item.j-1]=="w"):
                            #occupied by enemy
                            if(is_upper_half(arr,item.i-1,color)!=True):
                               #lower half
                               if(is_in_board(arr,item.i-2,item.j-2)):
                                   if(arr[item.i-2][item.j-2]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i-1][item.j-1]="-"
                                        arrcopy[item.i-2][item.j-2]="b"
                                        moves.append(arrcopy)
                            else:
                                #upper half
                               if(is_in_board(arr,item.i-2,item.j-1)):
                                   if(arr[item.i-2][item.j-1]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i-1][item.j-1]="-"
                                        arrcopy[item.i-2][item.j-1]="b"
                                        moves.append(arrcopy)
                else:
                    #upper half
                    if(is_in_board(arr,item.i-1,item.j)):
                        #check left
                        if(arr[item.i-1][item.j]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i-1][item.j]="b"
                            moves.append(arrcopy)
                        elif(arr[item.i-1][item.j]=="w"):
                            #occupied by enemy
                            if(is_in_board(arr,item.i-2,item.j)):
                                if(arr[item.i-2][item.j]=="-"):
                                    #can "eat" the piece
                                    arrcopy=copy.deepcopy(arr)
                                    arrcopy[item.i][item.j]="-"
                                    arrcopy[item.i-1][item.j]="-"
                                    arrcopy[item.i-2][item.j]="b"
                                    moves.append(arrcopy)
                    if(is_in_board(arr,item.i-1,item.j+1)):
                        #check right
                        if(arr[item.i-1][item.j+1]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i-1][item.j+1]="b"
                            moves.append(arrcopy)
                        elif(arr[item.i-1][item.j+1]=="w"):
                            #occupied by enemy
                            if(is_in_board(arr,item.i-2,item.j+2)):
                                if(arr[item.i-2][item.j+2]=="-"):
                                    #can "eat" the piece
                                    arrcopy=copy.deepcopy(arr)
                                    arrcopy[item.i][item.j]="-"
                                    arrcopy[item.i-1][item.j+1]="-"
                                    arrcopy[item.i-2][item.j+2]="b"
                                    moves.append(arrcopy)
            elif(color=="w"):
                #move white
                if(is_upper_half(arr,item.i,color)!=True):
                    #not in upper half
                    if(is_in_board(arr,item.i+1,item.j)):
                        #check left
                        if(arr[item.i+1][item.j]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i+1][item.j]="w"
                            moves.append(arrcopy)
                        elif(arr[item.i+1][item.j]=="b"):
                            #occupied by enemy
                            if(is_upper_half(arr,item.i+1,color)!=True):
                               #lower half
                               if(is_in_board(arr,item.i+2,item.j)):
                                   if(arr[item.i+2][item.j]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i+1][item.j]="-"
                                        arrcopy[item.i+2][item.j]="w"
                                        moves.append(arrcopy)
                            else:
                                #upper half
                               if(is_in_board(arr,item.i+2,item.j+1)):
                                   if(arr[item.i+2][item.j+1]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i+1][item.j]="-"
                                        arrcopy[item.i+2][item.j+1]="w"
                                        moves.append(arrcopy)
                    if(is_in_board(arr,item.i+1,item.j-1)):
                        #check right
                        if(arr[item.i+1][item.j-1]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i+1][item.j-1]="w"
                            moves.append(arrcopy)
                        elif(arr[item.i+1][item.j-1]=="b"):
                            #occupied by enemy
                            if(is_upper_half(arr,item.i+1,color)!=True):
                               #lower half
                               if(is_in_board(arr,item.i+2,item.j-2)):
                                    if(arr[item.i+2][item.j-2]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i+1][item.j-1]="-"
                                        arrcopy[item.i+2][item.j-2]="w"
                                        moves.append(arrcopy)
                            else:
                                #upper half
                               if(is_in_board(arr,item.i+2,item.j-1)):
                                   if(arr[item.i+2][item.j-1]=="-"):
                                        #can "eat" the piece
                                        arrcopy=copy.deepcopy(arr)
                                        arrcopy[item.i][item.j]="-"
                                        arrcopy[item.i+1][item.j-1]="-"
                                        arrcopy[item.i+2][item.j-1]="w"
                                        moves.append(arrcopy)
                else:
                    #upper half
                    if(is_in_board(arr,item.i+1,item.j)):
                        #check left
                        if(arr[item.i+1][item.j]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i+1][item.j]="w"
                            moves.append(arrcopy)
                        elif(arr[item.i+1][item.j]=="b"):
                            #occupied by enemy
                            if(is_in_board(arr,item.i+2,item.j)):
                                if(arr[item.i+2][item.j]=="-"):
                                    #can "eat" the piece
                                    arrcopy=copy.deepcopy(arr)
                                    arrcopy[item.i][item.j]="-"
                                    arrcopy[item.i+1][item.j]="-"
                                    arrcopy[item.i+2][item.j]="w"
                                    moves.append(arrcopy)
                    if(is_in_board(arr,item.i+1,item.j+1)):
                        #check right
                        if(arr[item.i+1][item.j+1]=="-"):
                            #empty
                            arrcopy=copy.deepcopy(arr)
                            arrcopy[item.i][item.j]="-"
                            arrcopy[item.i+1][item.j+1]="w"
                            moves.append(arrcopy)
                        elif(arr[item.i+1][item.j+1]=="b"):
                            #occupied by enemy
                            if(is_in_board(arr,item.i+2,item.j+2)):
                                if(arr[item.i+2][item.j+2]=="-"):
                                    #can "eat" the piece
                                    arrcopy=copy.deepcopy(arr)
                                    arrcopy[item.i][item.j]="-"
                                    arrcopy[item.i+1][item.j+1]="-"
                                    arrcopy[item.i+2][item.j+2]="w"
                                    moves.append(arrcopy)
    return moves
def minimax(node,depth,maximizing,symbol):
    #the actual minimax control is here
    if((depth==0)|win(node)):
        return depth+boardevaluator(node,symbol) #we want the one with the "least" iteration
    if(maximizing):
        #maximizing player
        value=-10000
        if(symbol=="w"):
            child=movegen(node,"w")
        else:
            child=movegen(node,"b")
        if(child==[]):
            child.append(node)
        for item in child:
            value=max(value,minimax(item,depth-1,False,symbol))
        return value
    else:
        #minimizing player
        value=10000
        if(symbol=="w"):
            child=movegen(node,"b")
        else:
            child=movegen(node,"w")
        if(child==[]):
            child.append(node)
        for item in child:
            value=min(value,minimax(item,depth-1,True,symbol))
        return value
    
def getwhiteonopponent(arr,token):
    #get number of white on opponent's starting row
    count=0
    for item in token:
        if((item.icon=="w")&(item.i==(len(arr)-1))):
           count+=1
    return count
def getblackonopponent(arr,token):
    #get number of black on opponent's starting row
    count=0
    for item in token:
        if((item.icon=="b")&(item.i==0)):
           count+=1
    return count
def winblack(arr,token):
    #check if black wins
    countwhite=0
    countblack=0
    for item in token:
        if (item.icon=="w"):
            countwhite+=1
        else:
            countblack+=1
    if(countwhite==0):
        #white doesn't have anything in the board, black wins
        return True
    else:
        whiteonopponent=getwhiteonopponent(arr,token)
        blackonopponent=getblackonopponent(arr,token)
        if((countblack==blackonopponent)and(countblack>0)):
            #black has all the token on opponent's board
            if(countwhite!=whiteonopponent):
                #not all white on opponent's board, black wins
                return True
            else:
                #white also has all on the opponent's side. Count which one is larger
                return (blackonopponent>whiteonopponent)            
    return False
def max(x,y):
    #max function for the minimax
    if(x>y):
        return x
    return y
def min(x,y):
    #min function for the minimax
    if(x>y):
        return y
    return x
def winwhite(arr,token):
    #check if white wins
    countblack=0
    countwhite=0
    for item in token:
        if (item.icon=="b"):
            countblack+=1
        else:
            countwhite+=1
    if(countblack==0):
        return True
    else:
        whiteonopponent=getwhiteonopponent(arr,token)
        blackonopponent=getblackonopponent(arr,token)
        if((countwhite==whiteonopponent)and(countwhite>0)):
            #white has all the token on opponent's board
            if(countblack!=blackonopponent):
                #not all black on opponent's board, white wins
                return True
            else:
                #black also has all on the opponent's side. Count which one is larger
                return (blackonopponent<whiteonopponent)            
    return False
def win(arr):
    #check if the board is a winning board
    token=state(arr)
    return (winblack(arr,token) or winwhite(arr,token))
def averagecalculator(arr,token,symbol):
    #calculate the average distance from the i-value of the token to the endzone of particular symbol
    count=0
    total=0
    for item in token:
        if (item.icon==symbol):
            count+=1
            if(symbol=="w"):
                difference=(len(arr)-1)-(item.i)
                total+=len(arr)-difference
            elif(symbol=="b"):
                difference=item.i #mod(0-item.i)=item.i
                total+=len(arr)-difference
    return total/count
def boardevaluator(arr,symbol):
    #this is the static board evaluator
    #here I used the difference in the average of distance from the i-value of the tokens to the endzone in order to compute the value
    #if the board is a win board, value = length of the board
    #if the board is a lose board, value = -length of the board
    #if the board is a draw board, value = 0
    token=state(arr)
    if((symbol=="w")and(winwhite(arr,token))):
        #win board
        return len(arr)
    elif((symbol=="b")and(winwhite(arr,token))):
        #lose board
        return -len(arr)        
    elif((symbol=="b")and(winblack(arr,token))):
        #win board
        return len(arr)
    elif((symbol=="w")and(winblack(arr,token))): 
        #lose board
        return -len(arr)
    else:
        #nobody wins or lose, apply the formula
        averagewhite=averagecalculator(arr,token,"w")
        averageblack=averagecalculator(arr,token,"b")
        if(symbol=="w"):
            return averagewhite-averageblack
        elif(symbol=="b"):
            return averageblack-averagewhite
def oskaplayer(board,symbol,depth):
    #return the best move for the certain board, not printed
    #example of the use is below
    arr=splitboard(board)
    moves=movegen(arr,symbol)
    index=-1
    value=-1000.0
    for i in range(len(moves)):
        minimaxvalue=minimax(moves[i],depth,False,symbol)
        if(minimaxvalue>=value):
            value=minimaxvalue
            index=i
    if(index==-1):
        return returnboard(arr)
    else:
        return returnboard(moves[index])
def splitboard(board):
    arr=[] #list of 2d array from the representation
    for i in board:
        arr.append([char for char in i]) #split into 2d array to make it more accessible
    return arr
def returnboard(item):
    #return board as per input
    board=[]
    for i in range(len(item)):
        string=""
        for j in range(len(item[i])):
            string+=item[i][j]
        board.append(string)
    return board
def printboard(item):
    #print board to specific format readable
    space=0
    middle=mid(item)
    print("-"*(len(item[0])*4+1))
    for i in range(len(item)):
        print(" "*space,end='')
        char=0
        for j in range(len(item[i])):
            if(item[i][j]=="-"):
                print("|  ",end=' ')
            else:
                print("| "+item[i][j],end=' ')
            char+=4
        print("|")
        char+=1
        if(i==len(item)-1):
            print(" "*space,end='')
            print("-"*(len(item[i])*4+1))
        elif(i>=middle):
            space-=2
            print(" "*space,end='')
            print("-"*(len(item[i+1])*4+1))
        else:
            print(" "*space,end='')
            print("-"*char)
            space+=2
            

#how to run the code:

#command: assign variable i to the oskaplayer
i=oskaplayer(['----','w--','b-','---','-bbb'],'b',2)
#i=oskaplayer(['----','---','--','---','---w'],'w',2)

#command: can be nested to something like below
#i=oskaplayer(oskaplayer(['wwwww','----','---','--','---','----','bbbbb'],'w',2),'b',2)

#command: print i
printboard(i)
