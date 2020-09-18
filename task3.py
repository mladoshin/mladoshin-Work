import math
filledMileage = float(input("Enter the car millieage the last time the car was filled: "));
currentMileage= float(input("Current Milliage: "));
tankVolume = float(input("Please enter the tank volume: "));

result = (currentMileage-filledMileage)/(tankVolume*0.22);
result = round(result, 2)
print(result);


## ACS - Logically correct
## ACS - Your code needs comments.
