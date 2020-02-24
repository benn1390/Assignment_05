#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Russell Bennett, 2020-Feb-23, Added code per assignment
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    
    elif strChoice == 'l':
        # Load existing data from file
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('Data has been imported\n')
    
    elif strChoice == 'a':  
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        try: 
            intID = int(strID)
        except ValueError:
            print('\nError: ID must be an integer\n')
            continue
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        print()
        
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('\nID | Title | Artist')
        for dicRow in lstTbl:
            strRow = ''
            for key, value in dicRow.items():
                strRow += str(value)+' | '
            strRow = strRow[:-3]
            print(strRow)
        print()
        
    elif strChoice == 'd':
        # Delete specified entry
        strID=input('Please specify the ID of the entry you wish to delete: ')
        try: 
            intID = int(strID)
        except ValueError:
            print('\nError: ID must be an integer\n')
            continue
        check=0
        for dicRow in lstTbl: 
            if dicRow.get('id') == intID:
                check+=1
                lstTbl.remove(dicRow)
                print('\nID: ',intID,' has been deleted')
        if check == 0:
            print('\nID: ',intID,' was not found')
        print()
            
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for dicRow in lstTbl:
            strRow = ''
            for key, value in dicRow.items():
                strRow += str(value) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Data has been stored in: ', strFileName, '\n')
        
    else:
        print('Please choose either l, a, i, d, s or x!\n')

