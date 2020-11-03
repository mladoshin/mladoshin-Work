def verificate():
    a = input("Are you sure? ")

    if (a=="yes"):
        return True
    else:
        return False

def validate(value, t):
    ROWS_RANGE = [1, 25]
    BASE_RANGE = [1, 20]
    res = False
    if (t=="rows"):
        try:
            value=int(value)
            if(value > ROWS_RANGE[0]) and (value < ROWS_RANGE[1]):
                res=True
        except:
            res=False

    elif (t=="base"):
        try:
            value=int(value)
            if(value > BASE_RANGE[0]) and (value < BASE_RANGE[1]):
                res = True
        except:
            res=False
           
    print(res)
    return res


def createTable(base, rows):
    base = int(base)
    rows = int(rows)
    for i in range(1, int(rows+1)):
        print(str(base)+"*"+str(i)+" = "+str(base*i))


    
#main programm

print("Hello")
base = input("Please enter the base: ")
v = verificate()



while (validate(base, "base")==False) or (v==False):
    
    if(v==True):
        print("Enter the base between 1 and 20!")
    
    base = input("Please enter the base: ")
    v = verificate()


rows = input("Please enter the number of rows: ")
v = verificate()

while (validate(rows, "rows")==False) or (v==False):
    if(v1==True):
        print("Enter the rows between 1 and 25!")
    rows = int(input("Please enter the number of rows: "))
    v = verificate()


createTable(base, rows)

    
