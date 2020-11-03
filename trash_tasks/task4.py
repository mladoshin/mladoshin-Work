studentNum = int(input("Enter the number of students: "));
bookNum = int(input("Enter the number of books to be shared: "));
res = bookNum // studentNum;
bookRemainder = bookNum % studentNum;

print("Each student will get "+str(res) + " books.", end="\n");
print("There will be "+str(bookRemainder)+" left.");

## ACS - I don't think the code above works correctly. Try 23 books and 3 students. 

name = input("Enter your name: ");
nameLength = len(name)
print("Your name length is "+str(nameLength));
