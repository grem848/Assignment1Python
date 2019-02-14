import kbh
import csv
file = './befkbhalderstatkode.csv'

# testing kbh.py
with open('befkbhalderstatkode.csv') as file:
    # making array of strings with data from the file
    linesarray = file.readlines()

    # converting stringarray to intarray
    for idx in range(len(linesarray)):
        linesarray[idx] = linesarray[idx].strip()
    
    assert kbh.STATISTICS[2015][1][0][5106] == int(linesarray[3][-1])
    print("Test complete.")