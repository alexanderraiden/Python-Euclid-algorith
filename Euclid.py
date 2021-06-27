print('You can calculate the GCD of two numbers')

def euclid(x,y):
    if x<y:
        (x,y)=(y,x)
    if (x%y) == 0:
        print('the Greatest Common Divider of', a, 'and', b, 'is', y)
        if y == 1:
            print('And', a, 'and', b, 'are co-prime')
        else:
            return    
    else:
        euclid(y, x%y)

a = int (input('Enter first number:'))
b = int (input('Enter second number:'))

euclid(a,b)
