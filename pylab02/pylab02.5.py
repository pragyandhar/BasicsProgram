a = str(input())
b = str(input())
c = str(input())
d = str(input())

if (c == "Rock" and d == "Scissor"):
    print(a,"Win")

elif (c == "Paper" and d == "Rock"):
    print(a,"Win")

elif (c == "Scissor" and d == "Paper"):
    print(a,"Win")

elif (c == "Scissor" and d == "Rock"):
    print(b,"Win")

elif (c == "Rock" and d == "Paper"):
    print(b,"Win")

elif (c == "Paper" and d == "Scissor"):
    print(b,"Win")

elif (c == "rock" and d == "scissor"):
    print(a,"Win")

elif (c == "paper" and d == "rock"):
    print(a,"Win")

elif (c == "scissor" and d == "paper"):
    print(a,"Win")

elif (c == "scissor" and d == "rock"):
    print(b,"Win")

elif (c == "rock" and d == "paper"):
    print(b,"Win")

elif (c == "paper" and d == "scissor"):
    print(b,"Win")