f = open("day3_data", "r")
input = f.read()
sum = 0
enabled = True
mulLoc = input.find("mul(")
doLoc = input.find("do()")
dontLoc = input.find("don't()")
while mulLoc != -1:
    doLoc = input.find("do()")
    dontLoc = input.find("don't()")
    while ((dontLoc < mulLoc) and (dontLoc != -1)) or (doLoc < mulLoc and doLoc != -1):
        if dontLoc < mulLoc and dontLoc != -1:
            enabled = False
            input = input[(dontLoc+1):]
            doLoc = input.find("do()")
            dontLoc = input.find("don't()")
            mulLoc = input.find("mul(")
        if doLoc < mulLoc and doLoc != -1:
            enabled = True
            input = input[(doLoc+1):]
            doLoc = input.find("do()")
            dontLoc = input.find("don't()")
            mulLoc = input.find("mul(")
    start = input.find("mul(") + 4
    end = 1
    while input[start + end] != ")":
        end += 1
    end = start + end
    sub = input[start:end]
    split = sub.split(",")
    try:
        if enabled:
            sum += int(split[0]) * int(split[1])
    except:
        pass
    input = input[start:]
    mulLoc = input.find("mul(")
print(sum)