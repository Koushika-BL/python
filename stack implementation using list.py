def push(item):
    stack.append(item)
def pop():
    if len(stack)==0:
        print(" stack is empty")
    else:
        a=stack.pop()
        print("popped item is :",a)
def display():
    print("items in stack are ",stack,"and the stack length is",len(stack))


    
stack=[]
choice=0
while(choice!=3):
          print("enter your choice 1.push 2.pop 3.exit")
          x=input()
          if x.isdigit():
              choice=int(x)
              if choice==1:
                  item1=int(input("enter a value to push into stack"))
                  push(item1)
                  display()
              elif choice==2:
                  pop()
                  display()
              elif choice==3:
                  break
              else:
                  print("Invalid choice")
          else:
             print("gvn choice is not a number")
          
    
