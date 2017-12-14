import pickle

def convertToObjectFile(file1, file2):

    '''

    Objective: To convert text file to object file

    Input Parameters: file1, file2: file names - string values

    Return Value: None

    Side effect: A new object file – file2 is created 

    '''

    try:

        fIn = open(file1, 'r')

        fOut = open(file2,'wb')

    except IOError:

        print('Problem in opening the file'); sys.exit()

    line = fIn.readline()

    while(line != ''):

        sList = line.split(',')

        try:

            sList[0] = int(sList[0])

            sList[2] = int(sList[2])

        except IndexError:
            
            print('Undefined Index')
            
            sys.exit()

        except (ValueError, TypeError):

            print('Unsuccessful conversion to int'); sys.exit()

        pickle.dump( sList , fOut )

        line = fIn.readline()

    fIn.close()

    fOut.close()

    print('\n\n\nInput file successfully converted to object file.')

def main():

    '''

    Objective: To convert text file to object file

    Input Parameter: None

    Return Value: None

    '''

    import sys

    sys.path.append('/home/administrator>')

    # To compute moderated marks of students

    file1 = input('Enter name of the text file:')

    file2 = input('Enter output object file name:')

    convertToObjectFile(file1, file2)

if __name__=='__main__':

    main()
