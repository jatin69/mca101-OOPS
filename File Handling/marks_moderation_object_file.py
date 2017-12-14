import pickle

def addstudents(file1):
    fOut = open(file1,'wb')
    Slist= [
        [1001,'AJAY',30],
        [1002,'ABHISHEK',50],
        [1003,'YASHVI',70],
        [1004,'PRAGYA',85],
        [1005,'SAURABH',90],
        [1006,'RAHUL',98],
        [1007,'YOGESH',89],
        [1008,'SHUSMITA',90],
        [1009,'AVINASH',87]
        ]
    for s in Slist:
        pickle.dump( s , fOut )
    fOut.close()
    
def computeModeratedMarks(file1, file2, addPercent):
    '''
    Objective: To compute moderated marks of students
    Input Parameters: file1, file2: file names - string values
                      file1, file2 are files of list objects
    addPercent – numeric value
    Return Value: None
    Side effect: A new file – OUTPUT2 of moderated marks is produced
    '''

    try:

        fIn = open(file1, 'rb')
        fOut = open(file2,'wb')

    except IOError:
        print('Problem in opening the file'); sys.exit()

    while True:
        try:
            sList = pickle.load(fIn)
            maxMarks = 100
            sList[2] = sList[2] + ((addPercent * maxMarks)/100) 

        except IndexError:
            print('Undefined Index')
            sys.exit()

        except (ValueError, TypeError):
            print('Unsuccessful conversion to int'); sys.exit()

        except EOFError:
            break

        pickle.dump( sList , fOut )

    fIn.close()
    fOut.close()

    fIn = open(file2, 'rb')

    print('\n\nLoading object file\n\n\n')
 
    while True:
        try:
            print(pickle.load(fIn))
        except EOFError:
            break

def main():
    '''
    Objective: To compute moderated marks based on user input
    Input Parameter: None
    Return Value: None
    '''

    import sys
    sys.path.append('/home/administrator>')

    # To compute moderated marks of students
    #file1 = input('Enter name of file containing marks:')
    file1='INPUT2'
    #file2 = input('Enter output file for moderated marks:')
    file2='OUTPUT2'
    addPercent = int(input('Enter moderation percentage:'))
    addstudents(file1)
    computeModeratedMarks(file1, file2, addPercent)

if __name__=='__main__':

    main()
