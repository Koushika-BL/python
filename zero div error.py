def div():
    a=5
    b=0
    try:
        c=a/b
    except ZeroDivisionError:
        print("c results in zero")
    else:
        print(c)
div()
    
