import math;
COVERAGE = 11;

length = float(input("Enter the length of the room: "));
width = float(input("Enter the width of the room: "));
height = float(input("Enter the height of the room: "));
unpArea = float(input("Enter the area of the unpaintable in sq m: "));


Area = length*width*2 + length*height*2 + width*height*2 - unpArea;
volume = math.ceil(Area/COVERAGE);
print(length);
print(width);
print(height);
print(unpArea);
print("area: "+str(Area));
print("paint volume: "+str(volume) + " litres");

## ACS - Logically fine.
## ACS - Needs comments so we know what approach you are taking.
