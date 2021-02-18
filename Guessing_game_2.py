import random
num = random.randint(1,10)
var = input ("1 ~ 10 whats your guess? :")
while var != num:
    var = input ("try again, 1 ~ 10 whats your guess? :")
    var = int(var)
    if var == num:
        print ("Correct you win... NOTHING!!!")
        break
    elif var > num:
        print ("Just a bit too big, try again")
        
    elif var < num :
        print ("Just a bit too small, try again")
    else:
        print ("Nope")


