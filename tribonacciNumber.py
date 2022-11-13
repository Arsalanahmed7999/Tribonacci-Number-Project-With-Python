# Tribonacci Number project with Python
# 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149...

# t0 = 0
# t1 = 1
# t2 = 1
# t3 = 2
# t4 = 4
# t5 = 7
# t6 = 13

def tribonacci(n):
    if n==0:
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2)+ tribonacci(n-3)


number = int(input('Enter your Number: \n'))
print(tribonacci(number))


