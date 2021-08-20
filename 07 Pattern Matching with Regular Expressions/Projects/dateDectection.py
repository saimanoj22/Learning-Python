# Date Dectection Program

import re, pyperclip
text = str(pyperclip.paste())
matches = []
dateRegex = re.compile(r'([0-3]\d)/([0-1]\d)/([1-2]\d{3})')

# Finding dates from text
for groups in dateRegex.findall(text):
    date=''
    #print(groups[0],groups[1],groups[2], sep=',')
    date += '/'.join([groups[0],groups[1],groups[2]])
    # Additional code (Validating dates)
    #========================================ADDITIONAL CODE STARTS========================================
    day = int(groups[0])
    month = int(groups[1])
    year = int(groups[2])
    leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)
    if(day in range(1,32) and month in range(1,13) and year in range(1000,3000)):
        if(month in [4,6,9,11]):
            dayCheck = day in range(1,31)
        elif month == 2:
            if leapYear:
                dayCheck = day in range(1,30)
            if not leapYear:
                dayCheck = day in range(1,29)
        else:
            dayCheck = day in range(1,32)
        if dayCheck:
            print(date)
            matches.append(date)
    #=========================================ADDITIONAL CODE ENDS=========================================
    
    #print(date)
    #matches.append(date)
print(matches)

# Some sample cases to check
'''
01/01/2001 32/01/2003 29/02/2001 28/02/2001 31/09/2003 05/50/2003 
'''