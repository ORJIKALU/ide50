from cs50 import get_int
while True:
    print("Height")
    userInput = get_int()
    if (userInput > 0) and (userInput < 23):
        break
hash = 1
space = userInput - 1
for i in range(userInput):
    for j in range(space):
        print(" ",end="")
    for k in range(hash):
        print("#", end="")
    print()
    space = space - 1
    hash = hash + 1
