#Make sure to use GenericStack class for this version of the program

#Create a loop that only generates prime numbers

#Store each prime number in a stack

#Print prime numbers from stack in a clean and formatted way, also make sure they are printed in descending order

def main():
    #How many prime numbers need to be calculated
    amountPrimeNumbers = userInput()
    
    #Create a stack of the calculated prime numbers
    primeStack = primeCalculator(amountPrimeNumbers)
    
    #Print the stack of prime numbers
    primePrinter(primeStack)
    
#Ask user how many prime numbers they would like to calculate. Includes invalid input checker.
def userInput():
    amountPrimeNumbers = input("How many prime numbers do you want me to calculate? ")
    while not amountPrimeNumbers.isdigit():
        amountPrimeNumbers = input("I'm sorry that wasn't a valid integer number. How many prime numbers do you want me to calculate? ") 
    print("The first", amountPrimeNumbers, "prime numbers are: \n")
    return int(amountPrimeNumbers)
    
def primeCalculator(amountPrimeNumbers):
    
    """lowEndPrime = 1
    
    #For (amountPrimeNumbers) iterate from the last prime number to the next prime number
    for i in range(1, amountPrimeNumbers + 1): #Starts at 1, ends before amoountPrimeNumbers + 1
        #print(i)
        
        #print(lowEndPrime)
        
        if lowEndPrime % lowEndPrime - 1 == 0:
            print(lowEndPrime, "not prime?")"""
            
    #Clunky code that works but needs to be completly optimized
    lowEndPrime = 2
    divisibleBy = lowEndPrime - 1
    
    while amountPrimeNumbers != 1:
    
        #Base case
        """if lowEndPrime <= 1:
            print(i, "Not a prime number")"""
        #print(divisibleBy)
        
        while lowEndPrime % divisibleBy != 0:
            #print(lowEndPrime, "%", divisibleBy, "==", lowEndPrime % divisibleBy, "Is a prime instance")
            
            divisibleBy -= 1
        
        if divisibleBy > 1:
            print(lowEndPrime, "is not a prime")
        else:
            print(lowEndPrime, "is a prime")
        lowEndPrime += 1
        amountPrimeNumbers -= 1
        divisibleBy = lowEndPrime - 1
    
    #iterate down through each number and see if it is divisible with any number lower than it that is greater than 1
    
    #add number to stack if it doesn't have a divisor (Excluding amountPrimeNumbers and 1)
    
    #Subtract 1 from amountPrimeNumbers and repeat
    
    #return primeStack
    
def primePrinter(primeStack):
    #While primeStack isn't empty
    
    #print each value of prime stack with spaces inbetween and make sure to create new rows as needed
    print()
    
#If there is a main method, run it
if __name__ == "__main__":
    main()