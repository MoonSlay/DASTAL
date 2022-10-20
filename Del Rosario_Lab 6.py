StackClass = []
Size = None


class stack:

    def init(stack):
        global Size
        if stack > 0:
            Size = int(stack)
        else:
            print('Invalid Input')
            exit()

    def traverse():
        if Size == None:
            print("Invalid Stack Size")
        else:
            for i in range(len(StackClass)): print(StackClass[i])

    def pop():
            return StackClass.pop(len(StackClass) - 1)

    def push(input):
        if len(StackClass) == Size:
            print("Stack Size limit reached: " + input)
        else:
            StackClass.append(input)


    def peek():
            print(StackClass[len(StackClass) - 1])
            return StackClass[len(StackClass) - 1]


stack.init(4)
stack.push("Juggernaut")
stack.push("Sniper")
stack.push("Shadow Fiend")
stack.push("Outworld Destroyer")
stack.push("Pudge")

print('Traverse:')
#prints stack
stack.traverse()

print('\nPop:')
#removes the element from the top of the stack which is "Outworld"("Pudge" went over the limit size so it wasn't counted)
stack.pop()
#prints stack
stack.traverse()
print('\nPeek:')
#prints the element from the top of the stack after pop which is "Shadow Fiend"
stack.peek()