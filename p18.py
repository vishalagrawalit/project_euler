from datetime import *

for _ in range(2*int(input())):
    try:
        y1 = list(map(int, input().split()))
        y2 = list(map(int, input().split()))

        curr_day = date(y1[0],y1[1],1)
        month = y1[1]
        year = y1[0]
        counter = 0

        while(curr_day.year < y2[0] or curr_day.month < y2[1]):
            if(curr_day.weekday() == 6):
                counter += 1
            if(month+1 == 13):
                month = 1
                year += 1
            else:
                month += 1
            curr_day = date(year,month,1)

        print(str(counter))
    except EOFError:
        pass
