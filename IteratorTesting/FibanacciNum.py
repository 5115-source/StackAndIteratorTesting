#Iterate through fibonacci numbers up to a user chosen max value. Utilizes the FibonacciIterator class to calculate and iterate through the different numbers
from FibonacciIterator import FibonacciIterator
def main():
    #What is the maximum value to calculate Fibonacci numbers up to?
    maxFibNumPotential = userInput()
    
    #Initialize and iterate through Fibonacci numbers using the FibonacciIterator class and print each number less than the max
    iterate = FibonacciIterator(maxFibNumPotential)
    for fibNum in iterate:
        print(fibNum)
    
#Ask user for input on the max number to calculate Fibonacci nubers up to
def userInput():
    #Valid input checker
    maxFibNumPotential = input("What is the max value you want me to calculate Fibonacci numbers up to? ")
    while not maxFibNumPotential.isdigit():
        maxFibNumPotential = input("I'm sorry that wasn't a valid integer number. What is the max value you want me to calculate Fibonacci numbers up to? ") 
        
    print("Here's a list of the Fibonacci numbers up to", maxFibNumPotential, ":")
    return int(maxFibNumPotential)
    
#If there is a main method, run it
if __name__ == "__main__":
    main()