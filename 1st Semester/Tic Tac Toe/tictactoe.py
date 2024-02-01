#FUNCTION
def display(x):
    format_display = '''
      {1}   |   {2}   |  {3}
    ------|-------|-------
      {4}   |   {5}   |  {6}  
    ------|-------|-------
      {7}   |   {8}   |  {9}  
    '''.format(*move)
    print(format_display)

#MAIN CODE
move = [" ", " ", " ", " ", " ", " ", " ", " ", " "]*9
turn = "X"
while True:
    input1 = int(input(f"{turn} Turn index location from (1-9): "))
    if move[input1] != " ":
        print("Location already used\nTry another location")
        continue
    else:
        move[input1] = turn
    display(move)
    if move[0] == move[4] == move[8] != " " or move[0] == move[1] == move[2] != " " or move[0] == move[3] == move[6] != " ":
        print(f"{move[0]} WINS")
        break
    if move[2] == move[4] == move[6] != " " or move[2] == move[5] == move[8] != " ":
        print(f"{move[2]} WINS")
        break
    if move[1] == move[4] == move[7] != " ":
        print(f"{move[1]} WINS")
        break
    if move[3] == move[4] == move[5] != " ":
        print(f"{move[3]} WINS")
        break
    if move[6] == move[7] == move[8] != " ":
        print(f"{move[6]} WINS")
        break
    if " " not in move:
        print("TIE")
        break
    turn = "0" if turn == "X" else "X"