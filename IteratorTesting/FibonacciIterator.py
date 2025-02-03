#Used ChatGPT for help learning about how to implement an iterator class in python
#It helped a lot in the general layout of this class before I tailor fit it to what I needed
class FibonacciIterator:
    #Set begining values when initialized
    def __init__(self, maxValue):
        self.previous = 1
        self.current = 1
        self.maxValue = maxValue

    #The __iter__ method makes this object an iterable (ChatGPT helped me realize this method was needed)
    def __iter__(self):
        return self

    # The __next__ method generates the next and previous Fibonacci numbers for evaluation
    def __next__(self):
        #If we have reached the maxValue then we will stop calculating Fibonacci numbers
        if self.current > self.maxValue:
            raise StopIteration  #Stop iterating as we don't want more Fibonacci Numbers
        else:
            #Current is updated to be a sum of the previous values
            self.current = self.current + self.previous
            #Previous is updated to be previous to the new current value
            self.previous = self.current - self.previous
            #Return the previous value so that current is not printed if it is larger than the high value
            return self.previous