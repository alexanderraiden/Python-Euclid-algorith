print('You can calculate the GCD of two numbers')

# This function just defines how the euclid algorithm works 
def euclid(x,y):
    if x<y: #checks to see which of the two numbers is larger and inverses them so that the first number is always the larger one
        (x,y)=(y,x)
    if (x%y) == 0: #compare both numbers to check when the result of the division produces a remainder of zero
        print('the Greatest Common Divider of', a, 'and', b, 'is', y) #if the remainder is zero, than the last number is the GDC
        if y == 1:
            print('And', a, 'and', b, 'are co-prime') #if the GCD is 1, it gives an additional message as that the two numbers are co-prime
        else:
            return    
    else:
        euclid(y, x%y) # if the division of the first number by the second numbers gives a remainder different than zero, then we didive
                        # the second number by the remainder of the previous operation and repeat the process

a = int (input('Enter first number:')) #prompt the user to input a number
b = int (input('Enter second number:')) #prompt the user to input a second number

euclid(a,b) #runs the function with the numbers entered by the user
