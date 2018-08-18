from random import randint #Imported for random number generation

class myQueue:
	#Constructor initializing to empty lists to act as our stacks
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	#Method to print the contents of the stacks for demonstration of functionality
	def printStack(self):
		if len(self.stack1) is 0: #If there is nothing in the stack
			print("Stack1 is empty!", end='\n\n') #Tell everyone that stack is empty
		else:
			print("The contents of stack1 are:", end=' ') #Otherwise, print the contents of the stack with formatting
			for i in self.stack1:
				print(i, end=' ')
			print("\n")

		if len(self.stack2) is 0:
			print("Stack2 is empty!", end='\n\n')
		else:
			print("The contents of stack2 are:", end=' ')
			for i in self.stack2:
				print(i, end=' ')
			print("\n")


	#Method which appends or "pushes" a passed data value onto stack1
	def push(self, data):
		self.stack1.append(data)

	#Method which returns the first element in the Queue
	def peek(self):
		self.prepareStacks() #Method that helps the 2 stacks emulate a single Queue
		if len(self.stack2) is 0: #If the "Queue" has nothing in it, simply return
			print("The Queue is empty.")
			return
		else:
			return self.stack2[-1] #Returning the "first" element of the "Queue"

	#Method that removes the first element in the Queue (FIFO)
	def pop(self):
		self.prepareStacks() #Prepare the stacks so that they act like a Queue
		return self.stack2.pop() #Release the first value in the "Queue"

	#Method that helps the 2 stacks emulate a Queue by using the stacks to order data as a Queue would
	def prepareStacks(self):
		if not self.stack2:
			while len(self.stack1) > 0: #While there are values in stack1
				self.stack2.append(self.stack1.pop()) #Pop the value off stack1 and append it to stack2

	#Method to print the contents of the Queue
	def printQueue(self):
		self.prepareStacks() #Prepare the "Queue"
		if len(self.stack2) is 0:
			print("The Queue is empty!", end='\n\n')
			return
		print("The contents of the Queue are:", end=' ')
		for i in self.stack2: #For every value in the queue, print it with formatting
			print(i, end=' ')
		print("\n")


def main():
	Q = myQueue() #Create an instance of the myQueue class


	#Generate 10 random numbers between 0 and 100 and Q.push them
	for i in range(0, 10):
		Q.push(randint(0, 100))

	print("The contents of the stacks currently:", end='\n\n')

	#Call printing functions to show their utility and show current contents of the stacks
	Q.printStack()

	print("Preparing the stacks to act as a queue.", end='\n\n')
	Q.prepareStacks()

	print("The contents of the stacks currently:", end='\n\n')
	Q.printStack()
	Q.printQueue()

	x = Q.peek() #Catch the value returned from the peek of the queue
	print("The first element in the queue is:", x, end='\n\n') #Print peek to show peek method functionality

	#Input validation and user input when demonstrating the pop methods functionality
	inp = int(input("Please enter the number of pops you want to occur: "))
	while inp > 10:
		print("There are only 10 elements in the queue, please choose a number 10 or lower.", end='\n\n')
		inp = int(input("Please enter the number of pops you want to occur: "))

	#Pop as many items as the user requested from the stack
	for i in range(0, inp):
		Q.pop()

	#Print to show current contents
	Q.printQueue()

if __name__ == '__main__':
	main()
