#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Alex Angelico, 20200807, Added code for
# adding CD dictionaries to 2D storage list.
# Alex Angelico, 20200811, Modified code for
# reading and writing data from/to the .txt
# file; added code for displaying
# current 2D list entries and deleting data
# from the .txt file; new variables include
# dispTbl[] and delTbl[].
#------------------------------------------#

#declare variables
strChoice = ''
lstTbl = []
dispTbl = []
delTbl = []
dicRow = {}
strFileName = 'CDInventory.txt'
objFile = None

#generate user input with reiterating menu
print('The Magic CD Inventory\n')
while True:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()
    print()
    
    #exit program
    if strChoice == 'x':
        break
    
    #view inventory contents
    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        print("ID | Artist | Title | # Songs")
        for row in objFile:
            tempRow = row.strip().split(',')
            dicRow = {'ID': int(tempRow[0]), 'Artist': tempRow[1], 'Title': tempRow[2], '# Songs': tempRow[3]}
            dispTbl.append(dicRow)
            dicRow = f"{dicRow['ID']} | {dicRow['Artist']} | {dicRow['Title']} | {dicRow['# Songs']}"
            print(dicRow)
        objFile.close()
        print()
        
        #optional search parameter for CDs by artist
        subsearch = input('Would you like to search for CDs from a specific artist? y/n ').lower()
        if subsearch == 'y':
            artist_search = input('Enter artist name: ')
            print('\nID | Artist | CD Title | # Songs')
            rowcount = int()
            cdcount = int()
            while rowcount < len(dispTbl):
                for row in dispTbl:
                    row.get(artist_search)
                    if artist_search == row['Artist']:
                        rowcount += 1
                        cdcount += 1
                        row = f"{row['ID']} | {row['Artist']} | {row['Title']} | {row['# Songs']}"
                        print(row)
                    else:
                        rowcount += 1
                        continue
            if cdcount == 0: print('There are no CDs by that artist.')
            dispTbl.clear()
        elif subsearch == 'n':
            dispTbl.clear()
            print()
        print()
        
    #add new CD data collection
    elif strChoice == 'a':
        strID = input('Enter an ID: ')
        strArtist = input('Enter the Artist\'s Name: ')
        strTitle = input('Enter the CD\'s Title: ')
        strSongNum = input('Enter the Number of Songs: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Artist': strArtist, 'Title': strTitle, '# Songs': strSongNum}
        lstTbl.append(dicRow)
        
    #view new CD data collections ready for inventory file
    elif strChoice == 'i':
        print('ID | Artist | CD Title | # Songs')
        for row in lstTbl:
            row = f"{row['ID']} | {row['Artist']} | {row['Title']} | {row['# Songs']}"
            print(row)
        print()
        
    #delete CD from inventory
    elif strChoice == 'd':
        #I/O for CD selection
        objFile = open(strFileName, 'r')
        print("ID | Artist | Title | # Songs")
        for row in objFile:
            tempRow = row.strip().split(',')
            dicRow = {'ID': int(tempRow[0]), 'Artist': tempRow[1], 'Title': tempRow[2], '# Songs': tempRow[3]}
            delTbl.append(dicRow)
            dicRow = f"{dicRow['ID']} | {dicRow['Artist']} | {dicRow['Title']} | {dicRow['# Songs']}"
            print(dicRow)
        objFile.close()
        print()
        id_search = int(input('Enter the ID you want to delete: '))
        for row in delTbl:
            row.get(id_search)
            if id_search == row['ID']:
                delTbl.remove(row)
            else:
                continue
            
        #simulated deletion via file rewrite
        lstTbl = delTbl
        print()
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            row = (row['ID'],row['Artist'],row['Title'],row['# Songs'])
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    #save new CD(s) to inventory
    elif strChoice == 's':
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            row = (row['ID'],row['Artist'],row['Title'],row['# Songs'])
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

