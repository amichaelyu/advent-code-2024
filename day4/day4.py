from http.cookiejar import user_domain_match
from symbol import and_expr

f = open("day4_data", "r")
input = f.read()
sum = 0
sum += input.count("XMAS")
sum += input.count("SAMX")
input = input.split("\n")
for z in range(len(input) - 3):
    for i in range(len(input[z])):
        if input[z][i] == "X" and input[z + 1][i] == "M" and input[z + 2][i] == "A" and input[z + 3][i] == "S":
            sum += 1
        if input[z][i] == "S" and input[z + 1][i] == "A" and input[z + 2][i] == "M" and input[z + 3][i] == "X":
            sum += 1

for z in range(len(input) - 3):
    for i in range(len(input[z]) - 3):
        if input[z][i] == "X" and input[z + 1][i + 1] == "M" and input[z + 2][i + 2] == "A" and input[z + 3][i + 3] == "S":
            sum += 1
        if input[z][i] == "S" and input[z + 1][i + 1] == "A" and input[z + 2][i + 2] == "M" and input[z + 3][i + 3] == "X":
            sum += 1

for z in range(3, len(input)):
    for i in range(len(input[z]) - 3):
        if input[z][i] == "X" and input[z - 1][i + 1] == "M" and input[z - 2][i + 2] == "A" and input[z - 3][i + 3] == "S":
            sum += 1
        if input[z][i] == "S" and input[z - 1][i + 1] == "A" and input[z - 2][i + 2] == "M" and input[z - 3][i + 3] == "X":
            sum += 1

print(sum)

sum2 = 0
for z in range(1, len(input) - 1):
    for i in range(1, len(input[z]) - 1):
        tl_br = False
        tr_bl = False
        if input[z][i] == "A":
            if (input[z + 1][i + 1] == "M" and input[z - 1][i - 1] == "S") or (input[z + 1][i + 1] == "S" and input[z - 1][i - 1] == "M"):
                tl_br = True
            if (input[z + 1][i - 1] == "S" and input[z - 1][i + 1] == "M") or (input[z + 1][i - 1] == "M" and input[z - 1][i + 1] == "S"):
                tr_bl = True
        sum2 += tl_br and tr_bl

print(sum2)