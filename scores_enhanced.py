scores = []
names = []
x = input ('How many students are there? : ')
x = int(x)

if x > 20:
    print ('The system cannot take more than twenty grades and names at a time.')
for c in range(x):
    c = c + 1  
    c = str(c)
    c = input("enter name here: ")
    names.insert(0, c)
    a = -1
for s in range(x):
    s = s + 1
    a = a + 1
    s = str(s)
    b = input("enter student's grades here in the order that they were given:# ")
    b = int(b)
    scores.append(b)
         
   
total = 0
total = int(total)
for l in range (x):
    total = total + scores[l]
average = total / x

lowest = 110
highest = 0
for m in range (x):
    if highest < scores[m]:
        highest = scores[m]
        
    if lowest > scores[m]:
        lowest = scores[m]
z = -1
z = int (z)
for z in range(x):
    z = z + 1

    if z == 0:
        print (scores[0],)
        print (names[0],)
        print('----------------------------------')
    
    if z == 1:
        print (scores[1],)
        print(names[1],)
        print('----------------------------------')


    if z == 2:
        print (scores[1],)
        print (names[1],)
        print('----------------------------------')
    
    if z == 3:
        print (scores[2],)
        print (names[2],)
        print('----------------------------------')
    
    if z == 4:
        print (scores[3],)
        print (names[3],)
        print('----------------------------------')
    
    if z == 5:
        print (scores[4],)
        print (names[4],)
        print('----------------------------------')
    
    if z == 6:
        print (scores[5],)
        print (names[5],)
        print('----------------------------------')
    
    if z == 7:
        print (scores[6],)
        print (names[6],)
        print('----------------------------------')
    
    if z == 8:
        print (scores[7],)
        print (names[7],)
        print('----------------------------------')
    
    if z == 9:
        print (scores[8],)
        print (names[8],)
        print('----------------------------------') 
    if z == 10:
        print (scores[9],)
        print (names[9],)
        print('----------------------------------')

    if z == 11:
        print (scores[10],)
        print (names[10],)
        print('----------------------------------')
    
    if z == 12:
        print (scores[11],)
        print (names[11],)
        print('----------------------------------')
    
    if z == 13:
        print (scores[12],)
        print (names[12],)
        print('----------------------------------')
    if z == 14:
        print (scores[13],)
        print (names[13],)
        print('----------------------------------')
    
    if z == 15:
        print (scores[14],)
        print (names[14],)
        print('----------------------------------')
    if z == 16:
        print (scores[15],)
        print (names[15],)
        print('----------------------------------')
    
    if z == 17:
        print (scores[16],)
        print (names[16],)
        print('----------------------------------')
    
    if z == 18:
        print (scores[17],)
        print (names[17],)
        print('----------------------------------')
    
    if z == 19:
        print (scores[18],)
        print (names[18],)
        print('----------------------------------')
    if z == 20:
        print (scores[19],)
        print (names[19],)
        print('----------------------------------')    
    
    
    
    
print ('average', average)
print('the lowest score is: ',lowest)
print('the highest score is: ', highest)

        
    
        