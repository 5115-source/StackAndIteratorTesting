#This version of the DisplayPrimeNum program uses the built in stack functionality of python so it doesn't rely on the GenericStack class
def main():
    #How many prime numbers need to be calculated
    amountPrimeNumbers = userInput()
    
    #Create a stack of the calculated prime numbers
    primeStack = primeCalculator(amountPrimeNumbers)
    
    #Print a formatted version of the stack of prime numbers
    primePrinter(primeStack)
    
#Ask user how many prime numbers they would like to calculate. Includes invalid input checker, and singular prime number grammar check
def userInput():
    #Valid input checker
    amountPrimeNumbers = input("How many prime numbers do you want me to calculate? ")
    while not amountPrimeNumbers.isdigit():
        amountPrimeNumbers = input("I'm sorry that wasn't a valid integer number. How many prime numbers do you want me to calculate? ") 
    
    #Singular prime number checker
    if int(amountPrimeNumbers) == 1:
        print("The first prime number is: ")
    else: 
        print("The first", amountPrimeNumbers, "prime numbers are: ", end = "")
    
    return int(amountPrimeNumbers)

#Go through every possible divisor of each number to find the amount of prime numbers the user has asked for
def primeCalculator(amountPrimeNumbers):
    #Set initial values for variables to be iterated on later
    primeStack = []
    currentPrimeCheck = 2
    divisibleBy = currentPrimeCheck - 1
    
    #Find the user chosen amount of prime numbers
    while amountPrimeNumbers != 0:
        #While the current number being checked is not divisible by any number less than it
        while currentPrimeCheck % divisibleBy != 0:
            divisibleBy -= 1
        
        #If current number being checked made it through every number except itself divided by 1
        if divisibleBy == 1:
            primeStack.append(currentPrimeCheck)
            amountPrimeNumbers -= 1
        
        #Update the current number being checked and the divisor being used to start chcking that number
        currentPrimeCheck += 1
        divisibleBy = currentPrimeCheck - 1
    
    return primeStack
    
#Add comments explaining this method
def primePrinter(primeStack):
    #The least amount of spacing needed will be equivalent to the amount of digits of the longest number + 1
    leastSpacing = len(str(primeStack[-1])) + 1
    printCounter = 0
    
    #While the stack is not empty
    while primeStack:
        #Take the current prime number off the stack and check its length
        currentPrime = primeStack.pop()
        currentPrimeLength = len(str(currentPrime))
        
        #If the amount of printed prime numebrs is a divisible of 10 then make a new row
        if printCounter % 10 == 0:
                print("\n")
        
        #While the spacing is not the same as the spacing on the largest length number add spaces
        while currentPrimeLength != leastSpacing:
            print(end = " ")
            currentPrimeLength += 1
            
        #Print the currentPrime number without adding a new line and update teh printed numbers counted
        print(f"{currentPrime}", end = "")
        printCounter += 1
    #For readaility
    print()
    print()
    
#If there is a main method, run it
if __name__ == "__main__":
    main()