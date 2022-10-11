# user_color=input(f'Type "WHITE" or "BLACK": ')
# Turn=int(input(f'WHITE first (1) BLACK first (2): '))
import string
import sys


BoardSize = 3 
blackPawn = " \u265f  "
whitePawn = " \u2658  "
empty_square = "    "
bgcolor = "\u001b[48;5;245m"

### Minimax Alpha-beta pruning을 위한 노드
class Node:
    def __init__(self, state, heuristicValue):
        self.state = state
        self.heuristicValue = heuristicValue
    # 파이썬의 Special Method
    def __lt__(self, other):
        return self.heuristicValue < other.heuristicValue


### Hexapawn_game
def Hexapawn_game(State,User_color,computer_color,Turn):
    State = Str_to_Pawn(State)
    while True:
        if gameover(State) == 1:
            return 1
        DrawBoard(State)
        if Turn == 1 :  ### 흰색 턴
            if User_color==whitePawn:
                State=get_move_human(State,User_color)
            elif user_color == blackPawn:
                AI_move()
        elif Turn == 2 : ### 검은색 턴
            if User_color==blackPawn:
                State=get_move_human(State,User_color)
            elif user_color == whitePawn:
                AI_move()


###  Read the input text file to make a state
def read_file(filename):
    f=open(filename,'r')
    strState=f.readlines()
    # 파일의 공백 제거
    for i in range(BoardSize):
        strState[i]=strState[i].replace(" ","")
        strState[i]=strState[i].replace("\n","")
    return strState

## 파일의 str값을 그림으로 바꿔주는 작업.
def Str_to_Pawn(strState):
    State = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            if strState[i][j] == '1':
                State[i][j]=whitePawn
            elif strState[i][j] == '2':
                State[i][j]=blackPawn
            elif strState[i][j] == '0':
                State[i][j]=empty_square
    return State

### 판 그리기.
def DrawBoard(State):
    clear = "\u001b[0m\u001b[K\n" 
    print(clear)
    ## 체스판처럼 검은색 흰색 나누려 하였으나 편의상 바꾸었다.
    board = ["1 ", bgcolor, State[0][0], bgcolor, State[0][1], bgcolor, State[0][2], clear,
    "2 ", bgcolor, State[1][0], bgcolor, State[1][1], bgcolor, State[1][2], clear,
    "3 ", bgcolor, State[2][0], bgcolor, State[2][1], bgcolor, State[2][2], clear,
    "   1   2   3\n"]

    sys.stdout.write("".join(board))
    return State
def get_opposite_Color(color):
    if color == blackPawn :
        return whitePawn
    elif color == whitePawn:
        return blackPawn
    else :
        print("get_opposite_color Error")

### 선택한 Pawn에서 가능한 움직임들을 반환하는 함수
### invalid한 움직임은 무엇인가
### 1. 상태판을 벗어나는 움직임
### 2. 바로앞에 상대편이 있을 때, 전진하려는 움직임 정도
### valid한 움직임
### 1. 앞공간이 비어있고 전진할때
### 2. 적이 대각선위치에 있을 때
def is_valid_move(State,row,col):
    if State[row][col] == empty_square: # 다시 한번 빈 공간인지 확인
        return []
    my_pawn = State[row][col]           # 내가 선택한 말(나의 말)의 색
    opposite_pawn = get_opposite_Color(my_pawn)    # 적팀의 색
    direction = get_direction(my_pawn)

    if(row + direction < 0 or row + direction> 2):
        ### 전진을 할때(대각선이든 직선이든)
        ### 상태판을 벗어나면 그것은 Invalid하다
        return []
    valid_move = [] ### 상태판을 안 벗어난다는 가정
    if State[row+direction][col] == empty_square: ## valid중 1번
        valid_move.append('gf')
    if col>0 and State[row+direction][col-1] == opposite_pawn: ## 왼쪽 대각선으로 움직일 수 있는 경우는 col 1,2
        valid_move.append('kl')
    if col<2 and State[row+direction][col+1] == opposite_pawn: ## 오른쪽 대각선으로 움직일 수 있는 경우는 col 0,1
        valid_move.append('kr')

    return valid_move

### 어떤 색을 선택하느냐에따라 방향이 달라짐 (위, 아래)
### 따라서 검은 Pawn인 경우 위 방향, 하얀 Pawn인 경우 아랫 방향
def get_direction(color):
    if color == blackPawn :
        direction = -1
    elif color == whitePawn :
        direction = 1
    else : # 예외시 어떤 값이 들어왔는지 확인
        print("Invalid color",color)
    return direction

def get_move_human(State,User_color):
    print("valid input is coordinate of board like (1,1)~(3,3)")
    print("input example : 11")
    ## 전진 방향
    direction = get_direction(User_color)
    while True:
        input_limit={'11':(0,0),'21':(0,1),'31':(0,2), # a
        '12':(1,0),'22':(1,1),'32':(1,2),
        '13':(2,0),'23':(2,1),'33':(2,2)}
        coordinate=input(f'what you want to move?: ')
        print('your choice : ', coordinate)
        if coordinate not in input_limit:
            print("Please input valid value!!")
            continue # return to start point of loop
        (row,col) = input_limit[coordinate]
        pawn = State[row][col]
        if pawn == empty_square :
            print("There is no pawn to move")
            continue
        if pawn != user_color:
            print("It is not your pieces")  
            continue
        valid_moves=is_valid_move(State,row,col)    ## 선택한 폰에서 가능한 움직임들을 반환해준다.
        print(valid_moves)
        if len(valid_moves) == 0:  # 선택한 Pawn에서 움직일 수 있는 경우가 없다.
            print("This pawn doesn't have valid move")
        move = list(valid_moves)[0]
        if len(valid_moves) > 1 :
            move = input(f'What move do you want to make ({",".join(list(valid_moves))})? ')
            if move not in valid_moves: 
                print("not allowed")
                continue
        if move == 'gf':    # 전진  go front
            State[row+direction][col] = State[row][col]
        if move == 'kl':   # 왼쪽에 있는 pawn 죽이기  kill left
            State[row+direction][col-1] = State[row][col]
        if move == 'kr':   # 오른쪽에 있는 pawn 죽이기 kill right
            State[row+direction][col+1] = State[row][col]
        State[row][col] = empty_square # Pawn을 옮겼으니 빈칸으로 채워준다.
        return State

def AI_move():
    return
def minimax():
    return

## 게임 종료 
## 1. 말이 상대편의 보드에 닿았는가
## 2. 말들이 다 죽었는가 
## 3. 행동 불가능
def gameover(State):
    ## case 1
    if State[2][0] == whitePawn or State[2][1] == whitePawn or State[2][2] == whitePawn :
        DrawBoard(State)
        print("WHITE PAWN REACH OPPOSITE SIDE!")
        print("WHITE WIN!!!!!!!!!!!!!!!!")
        return 1
    if State[0][0] == blackPawn or State[0][1] == blackPawn or State[0][2] == blackPawn :
        DrawBoard(State)
        print("BLACK PAWN REACH OPPOSITE SIDE!")
        print("BLACK WIN!!!!!!!!!!!!!!!!")
        return 1
    count_White_pawn=0
    count_Black_pawn=0
    ## case 2 : 말들이 다 죽음
    for i in range(3):
        for j in range(3):
            if State[i][j] == blackPawn:
                count_Black_pawn+=1
            if State[i][j] == whitePawn:
                count_White_pawn+=1
    if count_Black_pawn == 0 and count_White_pawn != 0 :
        DrawBoard(State)
        print("BLACK PAWN ALL DEAD!")
        print("WHITE WIN!!!!!!!!!!!!!!!!")
        return 1
    elif count_White_pawn == 0 and count_Black_pawn != 0 :
        DrawBoard(State)
        print("WHITE PAWN ALL DEAD!")
        print("BLACk WIN!!!!!!!!!!!!!!!!")
        return 1
    ## 행동 불가
    ## 모든 Pawn에 대하여 valid한 움직임 값을 얻어야한다.
    white_valid_move=[]
    black_valid_move=[]

    ## 판에 있는 모든 Pawn에 대하여 움직임을 얻는다.
    for i in range(3):
        for j in range(3):
            moves = is_valid_move(State, i, j)
            if State[i][j] == whitePawn:
                if len(moves) > 0: ### 움직임이 있는 경우.
                    white_valid_move.append(moves)
            if State[i][j] == blackPawn:
                if len(moves) > 0: ### 움직임이 있는 경우
                    black_valid_move.append(moves)
    if len(white_valid_move) == 0 and len(black_valid_move) !=0 : ## White가 움직일 경우의 수가 없다.
        DrawBoard(State)
        print("WHITE PAWN HAVE NO CHOICE!")
        print("BLACk WIN!!!!!!!!!!!!!!!!")
        return 1
    elif len(black_valid_move) == 0 and len(white_valid_move) !=0 : ## Black의 움직일 경우가 없다.
        DrawBoard(State)
        print("BLACk PAWN HAVE NO CHOICE!")
        print("WHITE WIN!!!!!!!!!!!!!!!!")
        return 1

    return 0




###### MAIN
State = []
file_input_name=input(f'Input file name (default board = 0) : ')
user_color=input(f'Type "WHITE" or "BLACK": ')
Turn=int(input(f'WHITE first (1) BLACK first (2): '))
if user_color == "WHITE" :
    user_color=whitePawn
    computer_color = blackPawn
elif user_color == "BLACK" :
    user_color=blackPawn
    computer_color = whitePawn
if file_input_name == '0' :
    while True: 
        State = ['111','000','222']
        if(Hexapawn_game(State,user_color,computer_color,Turn) == 1) :
            quest=int(input(f'Would you play MORE(1) or End(2) : '))
            if (quest == 1 ): ### 게임 재시작, input.txt 의 입력값이나 초기 상태부터 다시 시작.
                continue
            elif (quest == 2) :
                print("GAME OVER")
                break
else : 
    while True:
        State = read_file(file_input_name)
        if(Hexapawn_game(State,user_color,computer_color,Turn) == 1) :
            quest=int(input(f'Would you play MORE(1) or End(2) : '))
            if (quest == 1 ): ### 게임 재시작, input.txt 의 입력값이나 초기 상태부터 다시 시작.
                continue
            elif (quest == 2) :
                print("GAME OVER")
                break


