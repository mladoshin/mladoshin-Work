import random
signs=["R", "S", "P"]

def checkWin(s1, s2):
    res = True
    if (s1=="R") and (s2=="P") or (s1=="S") and (s2=="R") or (s1=="P") and (s2=="S"):
        res=False

    return res


def userInput():
    sign = input("Enter r, s or p: ").upper()
    try:
        if (signs.index(sign)):
            return sign
    except:
        print("Error! Enter r, s or p!")
        return userInput()

    

def main():
    sign1 = userInput()
    sign2 = signs[random.randint(0, len(signs)-1)]

    res = checkWin(sign1, sign2)
    print("You: ",sign1)
    print("Computer: ",sign2)
    if (res==True):
        print("You won!")
    else: print("You lost!")
    print("<-------------------->\n")
    main()


main()


