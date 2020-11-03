import random
signs=["R", "S", "P"]
draw = "You draw!"
loss = "You lost!"
win = "You won!"

results = [[draw, win, loss ],
                 [loss, draw, win],
                 [win, loss, draw]
                 ] #0-draw, 1-loose, 2-win



def userInput():
    sign = input("Enter r, s or p: ").upper()
    print(sign)
    try:
        if (signs.index(sign)+1  ):
            return sign
    except:
        print("Error! Enter r, s or p!")

    return userInput()

    

def main():
    sign1 = userInput()
    sign2 = signs[random.randint(0, len(signs)-1)]

    print("You: ",sign1)
    print("Computer: ",sign2)

    print(results[signs.index(sign1)][signs.index(sign2)])
    print("<-------------------->\n")
    main()


main()


