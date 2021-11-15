#------------------------------------------#
# Title: Assignment05.py
# Desc: Assignment 05 for Foundations of Programming: Python
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# SBurner, 2021-Nov-11, changed lists to dictionaries
#------------------------------------------#


# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary for table row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
readRow = []
readDic = {}
strID = ''
strTitle = ''
strArtist = ''
strRow = ''

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName,'r')
        for row in objFile:
            readRow = row.strip().split(',')
            readDic['ID'] = readRow[0]
            readDic['Artist'] = readRow[1]
            readDic['Title'] = readRow[2]
            lstTbl.append(readDic)
            readDic = {}
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        dicRow['ID'] = input('Enter an ID: ')
        dicRow['Title'] = input('Enter the CD\'s Title: ')
        dicRow['Artist'] = input('Enter the Artist\'s Name: ')
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            strRow = str(row['ID']) + ', ' + str(row['Title']) + ', ' + str(row['Artist'])
            print(strRow)
    elif strChoice == 'd':
        # Allow the user to delete a row
        print('Current Inventory:\n')
        for row in lstTbl:
            strRow = str(row['ID']) + ', ' + str(row['Title']) + ', ' + str(row['Artist'])
            print(strRow)
        
        delID = str(input('Enter ID of row you would like to delete: '))

        for i in range(len(lstTbl)):
            if lstTbl[i]['ID'] == delID:
                del lstTbl[i]
                break
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        wrtType = input('Tyoe a to add data, type w to overwrite data: ').lower()
        if wrtType == 'a':
            objFile = open(strFileName,'a')
            for row in lstTbl:
                strRow = str(row['ID']) + ',' + str(row['Title']) + ',' + str(row['Artist']) + '\n'
                objFile.write(strRow)
            objFile.close()
        elif wrtType == 'w':
            objFile = open(strFileName,'w')
            for row in lstTbl:
                strRow = str(row['ID']) + ',' + str(row['Title']) + ',' + str(row['Artist']) + '\n'
                objFile.write(strRow)
            objFile.close()
        else:
            print('invalid option')

    else:
        print('Please choose either l, a, i, d, s or x!')

