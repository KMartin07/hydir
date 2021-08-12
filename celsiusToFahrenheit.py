celsius = [32, 41, 23, 19, 34, 25, 29, 28, 17]
    
fahrenheit = []

def fahrenheitMaker(celsius):   
    for celsiusNumber in celsius:
        fahrenheitNumber = celsiusNumber * 1.8 + 32
        fahrenheit.append(fahrenheitNumber)

fahrenheitMaker(celsius)

print("Fahrenheit Temp Array:")
print(fahrenheit)

max_value = max(fahrenheit)
min_value = min(fahrenheit)
avg_value = 0 if len(fahrenheit) == 0 else sum(fahrenheit)/len(fahrenheit)

print("Max temp is:")
print(max_value)

print("Min temp is:")
print(min_value)

print("The average of all temps is:")
print(avg_value)

#celsius * 1.8 + 32 = fahrenheit
## I want an array of tempratures (integers) in celsius
### I want you to convert them to freedom units
### after you convert the numbers, find the mean, the min, and the max
### use a function for converting from celsius to Freedom units
#### hint set a variable that holds the to compare to 
# def toFreedomUnits(celsiusTemp):
## define this function 
# return freemdomTemp

