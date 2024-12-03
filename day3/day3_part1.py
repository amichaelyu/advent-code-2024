f = open("day3_data", "r")
input = f.read()
sum = 0
enabled = True
while input.find("mul(") != -1:
    start = input.find("mul(") + 4
    end = 1
    while input[start + end] != ")":
        end += 1
    end = start + end
    sub = input[start:end]
    split = sub.split(",")
    try:
        sum += int(split[0]) * int(split[1])
    except:
        pass
    input = input[start:]
print(sum)