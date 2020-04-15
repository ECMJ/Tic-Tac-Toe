
p = input("Enter cells: > ")
print("---------")
print("|", p[0], p[1], p[2], "|")
print("|", p[3], p[4], p[5], "|")
print("|", p[6], p[7], p[8], "|")
print("---------")

row1 = (p[0] + p[1] + p[2])
row2 = (p[3] + p[4] + p[5])
row3 = (p[6] + p[7] + p[8])
column1 = (p[0] + p[3] + p[6])
column2 = (p[1] + p[4] + p[7])
column3 = (p[2] + p[5] + p[8])
cross1 = (p[0] + p[4] + p[8])
cross2 = (p[6] + p[4] + p[2])

result = row1, row2, row3, column1, column2, column3, cross1, cross2
x = "X"
y = "O"
z = "_"
x_win = "XXX"
y_win = "OOO"

if (x_win and y_win) in result:
    print("Impossible")
elif (len(x) - len(y)) in result >= 2:
    print("Impossible")
elif (len(y) - len(x)) in result >= 2:
    print("Impossible")
elif x_win in result:
    print("X Wins")
elif y_win in result:
    print("O Wins")
elif x_win and y_win not in result and z in p:
    print("Game not finished")
elif x_win and y_win not in result and z not in p:
    print("Draw")
