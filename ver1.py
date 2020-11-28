import random as r
win, lose = 0, 0
print("If you wanna change limit or see score - write \"0\"")
while True:
    top =int(input("Multiplication limit: "))
    if top == 0:
        break
    x = 1
    while x != 0:
        rand1, rand2 = r.randint(1, top), r.randint(1, top)
        print(rand1, "*", rand2)
        x = int(input("Answer: "))
        if x == 0:
            break
        elif x == rand1*rand2:
            win += 1
            print("You are right, answer is ", rand1*rand2)
        else:
            print("You are wrong, answer is ", rand1*rand2)
            lose += 1
print("Youe score:")
print("Right - ", win, ", ", "Wrong - ", lose)
if win + lose != 0:
    print("Percentage of correct answers - ", round((win/(win + lose)), 2) * 100)
input()
