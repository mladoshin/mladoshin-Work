nameList = []
STUDENTS = 10
EXIT_ACTION = "exit"
NAME_LENGTH = 3

def initList():
    for i in range(STUDENTS):
        nameList.append("")

def displayList():
    print()
    for i in range(STUDENTS):
        #if (nameList[i] != ""):
        print(str(i+1)+": "+nameList[i])
    print()
        
def displayMenu():
    print()
    print("1 - Add Name")
    print("2 - Display list")
    print("3 - Quit")
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if (choice <= 3) and (choice >=1):
            return choice
    except:
        print("Please enter the number!")
    
    print("\nEnter the integer between 1 and 3\n")
    return displayMenu()


def addNameIndx(name):
    index = input("Enter the position in the list for "+str(name)+" (1-"+str(STUDENTS)+"):")
    try:
        index = int(index)
        if (index <= STUDENTS) and (index >=1):
            return index
    except:
        if(index == EXIT_ACTION):
            return False
        print("Please enter the number!")

    return addNameIndx(name)

    
def addName():
    print()
    name = input("Enter the name: ")
    if (name != "") and (len(name)>=NAME_LENGTH): 
        if (name==EXIT_ACTION):
            return False
        
        index = addNameIndx(name)
        if (index==False):
            return False
        
        nameList.insert(index-1, name)
    else:
        print("The name should contain at least "+str(NAME_LENGTH)+" letters!")
        addName()


        
def main():
    print("<----------------------------------------------------------------->")
    choice = displayMenu()
    if (choice==1):#Add name
        addName()
    elif (choice==2):#DisplayList
        displayList()
    elif (choice==3):
        return True
    
    main()
    
#main
initList()
main()
print("Program Terminated")
    
