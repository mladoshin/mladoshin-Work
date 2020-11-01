rows = 10
cols = 6
parking = []

def initParking():
    print("Array init")
    for i in range(0, 10):
        row = []
        for j in range(0, 6):
            row.append("empty")

        parking.append(row)

def displayParking():
    for i in range(0, 10):
        for j in range(0, 6):
            print(parking[i][j])

def placeInput():
    row = int(input("Enter the row: "))
    col = int(input("Enter the col: "))
    if (row < 11) and (col < 7):
        return row, col
    else:
        return placeInput()

def park():
    reg = input("Enter car reg number: ")
    row, col = placeInput()
    if (parking[row-1][col-1] == "empty"):
        parking[row-1][col-1] = reg
        print("Success")
        
def firstChar(string):
    return string[0]

def lastChar(string):
    return string[len(string)-1]

def middlePart(string):
    return string[1:-1]

def leftSide(string):
    #print(string[:-1])
    return string[:-1]

def rightSide(string):
    #print(string[1:])
    return string[1:]

def pol(string):
    
    if (len(string)==0):
        return True
    
    if (isPolindrom(string)==True):
        print(string)
        
    if (len(string)>2):
        pol(leftSide(string))

    if (len(string)>2):
        pol(rightSide(string))
        
    if (len(string)>3):
        pol(middlePart(string))
    
        
def isPolindrom(string):

    if (len(string)<2):
        return True

    if(firstChar(string) != lastChar(string)):
        return False

    
    
        
    return isPolindrom(middlePart(string))

    
    
#s = "nitin"
#pol(s)

def main():
    park()
    displayParking()
    main()

initParking()
main()
displayParking()
