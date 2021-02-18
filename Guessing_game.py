import random
num = random.randint(1,10)
var = input ("1 ~ 10 whats your guess? :")
var = int(var)
if var == num:
    print ("Correct you win... NOTHING!!!")
else:
    print ("Nope that's wrong")
    
    print ("the answer is",num)