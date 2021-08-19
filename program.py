### Arrays
### what is array
### Array is immutable (you cant change the size)
### Arrays contain elements of a single type
### how do we declare an array in python



### how do i get the size of my array ?

#
# counter = 0
# for everyElement in myArray:
#     counter = counter + 1


### how do i access a specific index within my array ?
### myArray[n - 1]

# myArray = [1,2,3,4]
# lengthOfMyArray = len(myArray)
# for i in range(lengthOfMyArray - 1):
#     evaluation = myArray[i] * 3
#     print(evaluation)

# for number in range(7):
#     print(number)


### I want an array of tempratures (integers) in celsius
### I want you to convert them to freedom units
### after you convert the numbers, find the mean, the min, and the max
### use a function for converting from celsius to Freedom units
#### hint set a variable that holds the to compare to
# def toFreedomUnits(celsiusTemp):
## define this function
# return freemdomTemp


##### Dictionaries
### most useful python data structure

myDictionary = {}
myDictionary["word1"] = 33
myDictionary["word2"] = "definition2"
myDictionary["word3"] = [1,2,3,4]

myDictionary["word4"] = {}
myDictionary["word4"]["word4a"] = "cool dictionary"
myDictionary["word4"]["word4b"] = "cool dictionary"


### I want you to make me a dictionary of a multiplication table
### the key will be an integer, you will have 12 keys (1 to 12),
## the value will be a list of numbers(1 through 12) times the key
#### example entry
#### mulitplicationTable[3] = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

### YOU MUST USE A LOOP
### Remember that dictionary values can be of any type
### for number in range(however many iterations you need)
n=1

def getMultiples(n):
    multiplications = list()
    for number in range(12):
        multiplications.append(number * n)
    return multiplications
    multiplicationTable = {n:multiplications}
    return multiplicationTable

#multiplier = getMultiples


for n in range(12):
    getMultiples(n)
    multiplicationTable[multiplicationTable].append(multiplications)
    n = n+1 

    
print(getMultiples(12))


        







### make another loop where you call getMultiples with a variable 
### store the output in a dictionary
