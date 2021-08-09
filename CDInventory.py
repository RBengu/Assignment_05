#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RBengu,     2021-Aug-06, Updated 'TODO's
#------------------------------------------#

# -- DATA -- #
# Declare variabls

strChoice = '' # User input
dicTbl = []  # list of dicts to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PRESENTATION (INPUT) -- #
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    # -- PROCESSING -- #
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow ={'id':int(lstRow[0]), 'artist':lstRow[1], 'title':lstRow[2]}
            dicTbl.append(dicRow)
        objFile.close()        

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id':intID, 'title':strTitle, 'artist':strArtist}
        dicTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in dicTbl:
            strRow = ''
            for key, val in row.items():
                strRow += str(val) + ', '
            strRow = strRow[:-2]
            print(strRow)
            
    elif strChoice == 'd':
        print('\nID, CD Title, Artist')
        for row in dicTbl:
            strRow = ''
            for key, val in row.items():
                strRow += str(val) + ', '
            strRow = strRow[:-2]
            print(strRow)
            
        delID = int(input('\nPlease select the ID of the CD to be deleted: \n'))
            
        for row in dicTbl:
            for key, val in row.items():
                if val == delID:
                    dicTbl.remove(row)
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName,'w')
        
        for row in dicTbl:
            strRow = ''
            for key, val in row.items():
                strRow += str(val) + ', '
            strRow = strRow[:-2] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

