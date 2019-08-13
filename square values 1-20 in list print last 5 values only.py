def square(n):
    li= list()
    for i in range(1,n):
        li.append(i**2)
    print(li)
    print(li[-1:-6:-1])
square(21)
