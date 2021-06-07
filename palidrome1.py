a = input()
def palidrome(a):      
    n = len(a)
    flag = 0
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2          
    start1 = 0
    start2 = n-1      
    while(start1 < mid ):          
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 -1 
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
palidrome(a)          
