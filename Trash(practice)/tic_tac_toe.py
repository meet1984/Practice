board={1:"-",2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}
def print_board():
    print(board[1],board[2],board[3])
    print(board[4],board[5],board[6])
    print(board[7],board[8],board[9])

def winner():
    if board[1]==board[2]==board[3] and board[1]!="-":
        return 1
    if board[4]==board[5]==board[6] and board[4]!="-":
        return 1
    if board[7]==board[8]==board[9] and board[7]!="-":
        return 1
    if board[1]==board[4]==board[7] and board[1]!="-":
        return 1
    if board[2]==board[5]==board[8] and board[2]!="-":
        return 1
    if board[3]==board[6]==board[9] and board[3]!="-":
        return 1
    if board[1]==board[5]==board[9] and board[1]!="-":
        return 1
    if board[3]==board[5]==board[7] and board[3]!="-":
        return 1
    return 0
print_board()
cn=0
flag=0
player1=input("Enter player 1 name:")
player2=input("Enter player 2 name:")
while cn<9 :
    if flag%2==0 :
        pos=int(input(player1+" Turn :"))
        if board[pos]!="-":
            continue
        board[pos]="X"
        flag=1
    else :
        pos=int(input(player2+" True :"))
        if board[pos]!="-":
            continue
        board[pos]="O"
        flag=0
    x=winner()
    if x==1 :
        if flag==1 :
          print(player1+" winner ")
        else :
          print(player2+" winner ")
        break
    print_board()
    cn+=1    
    
    