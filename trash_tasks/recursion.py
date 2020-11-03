import time
num = 10

def fib(n):
    if (n <=1):
        return n
    else:
        return fib(n-1) + fib(n-2)

startTime1 = time.process_time()
print(fib(num))
endTime1 = time.process_time()
print("Time1: " + str(endTime1))

def fibonacci(n):
    fibNumbers = [0,1]

    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])

    
    return fibNumbers[n]


startTime2 = time.process_time()
print(fibonacci(num))
endTime2 = time.process_time()
print("Time2: " + str(endTime1))

