ans = input("Please input score in numerical form ")
ans = int (ans)
if ans > 110:
    print ('please stop messing around')
elif ans >= 95:
    print ('A+, Congratulations you get a Certificate of Exemplary Behaviour')
elif ans >= 90:
    print ('A, Congratulations you get a Certificate of Proficiency')
elif ans >= 85:
    print ('B+, Good job keep working and you will get to A someday')
elif ans >= 80:
    print ('B, Nice job keep at it!')
elif ans >= 75:
    print ('C+, keep at it')
elif ans >= 70:
    print ('C, Do better next time')
elif ans >= 65:
    print ('D+, congratulations you get a week of cleaning cesspits')
elif ans >= 60:
    print ('D, congratulations you get a week of detention')
else :
    print ('F, congratulations you are suspended for three weeks')