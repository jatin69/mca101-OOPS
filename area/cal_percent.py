def calPercent(obtainedMarks,maxMarks):
    '''
    objective : To calculate the percentage of the given marks 
    arguments:
        obtainedMarks : the marks obtained by the student
		maxMarks      : the maximum marks possible
    approach : Using arithmetic operations
    return value : 
		percentage : The calculated percentage is returned
		'''
    percentage=(obtainedMarks/maxMarks)*100
    return percentage
    
def main():
    '''
    objective: To calculate the percentage of the given marks
    User inputs :
            obtainedMarks : The marks obatined by the student
            maxMarks : The maximum marks possible
    calPercentage : The calculated percentage which is returned
    approach: Using function calPercent()
    '''
    obtainedMarks = int(input("Enter Marks:  "))
    maxMarks = int(input("Enter max Marks:  "))
    calPercentage = calPercent(obtainedMarks,maxMarks)
    print("Percentage: ", calPercentage)
    print("End of Main")
    
if __name__ == "__main__":
    main()
    print("End of Program")