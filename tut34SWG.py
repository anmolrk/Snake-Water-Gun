import random

def comp_ch():
    lst = ["Snake","Water","Gun"]
    choice = random.choice(lst)
    c_char = choice[0]
    return c_char

def inpt(play):    
    try:
        p = play[0].upper()
        return p
    except Exception as e:
        p = " "
        # print(e)
        # print("Try again")
        return p

def user_ch():
    while(True):
        play = input("Enter S for SNAKE, W  for WATER and G for GUN: ")        
        p_char = inpt(play)
        print(p_char)
        if p_char == 'S' or p_char == 'W' or p_char == 'G':
            return p_char
            break
        else:
            print("INVALID INPUT!!! Please try again") 
            

def enterYN():
    while(True):
        chr = input("Enter Y to Run Again or N to stop")
        ch = inpt(chr)
        if ch == "Y" or ch == "N" or ch == "y" or ch == "n":
            return ch
            break
        else:
            print("INVALID INPUT!!! Please try again") 

def intinpt():
    n = input("Enter the Score Limit: ")
    try:
        num = int(n)
        # print("try is called")
        return num
    except Exception as e:
        # print(e)
        print("Invalid Input!!! TRY AGAIN")
        num = 0
        # print("except is called")
        return num 


def checkZERO():
    while(True):
        i = intinpt()
        if i > 0:
            # print("if is called")
            return i
            break
        else:
            # print("else is called")
            pass


while(True):
    print("\n\n*************   SNAKE WATER GUN    ******************")
    print("This just like stone paper scissor. Both the players\nshould keep the gestures simultaneously. The snake\ndrinks the water, the gun shoots the snake, and gun\nhas no effect on water.")
    print("*****************************************************")

    name = input("Enter the Your name Player: ")
    n = checkZERO()
    compPoint = 0
    playerPoint = 0
    while(True):
        if compPoint < n and playerPoint < n:
            c = comp_ch()
            p = user_ch()
            
            if c == 'S':
                if p == 'S':
                    print("Computer : Snake and", name,": Snake")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                elif p == 'W':
                    compPoint = compPoint + 1
                    print("Computer : Snake and", name,": Water")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                else:
                    playerPoint = playerPoint + 1
                    print("Computer : Snake and", name,": Gun")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
            elif c == 'W':
                if p == 'S':
                    playerPoint = playerPoint + 1
                    print("Computer : Water and", name,": Snake")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                elif p == 'W':
                    print("Computer : Water and", name,": Water")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                else:
                    compPoint = compPoint + 1            
                    print("Computer : Water and", name,": Gun")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
            else:
                if p == 'S':
                    compPoint = compPoint + 1
                    print("Computer : Gun and", name,": Snake")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                elif p == 'W':
                    playerPoint = playerPoint + 1
                    print("Computer : Gun and", name,": Water")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
                else:           
                    print("Computer : Gun and", name,": Gun")
                    print("Computer :", compPoint, "and", name, ":",playerPoint)
        else:
            if compPoint > playerPoint:
                print("----------------------------------------------")
                print("Computer Wins")
                print("Computer :", compPoint, "and", name, ":",playerPoint)
                print("----------------------------------------------")
            else:
                print("----------------------------------------------")
                print("You Wins")
                print("Computer :", compPoint, "and", name, ":",playerPoint)
                print("----------------------------------------------")
            break
    print("Wanna Play Again Y/N")
    ch = enterYN()
    if ch == "Y" or ch == "y":
        continue
    else:
        break