# starting with a clean file

#THIS IS HOW YOU WRITE A SINGLE LINE COMMENT

'''
THIS IS THE MULTI LINE COMMENT COOOOL
'''

#********************************************************************************************************************************************************************************************

#Let's start with print statements

'''
There is no functional difference in using double and single quotations,
but there might be situations where I want to print "", who knows?
'''

print("Dummy")
print('He yelled, "Dummy!"')
print('the sum is', 22*45,  ". that's not a sum, that's a product but whatever maths is funny")

'''
OUTPUT

Dummy
He yelled, "Dummy!"
the sum is 990 . that's not a sum, that's a product but whatever maths is funny

'''

#********************************************************************************************************************************************************************************************

#Let's jump to types, which we don't have to worry about

a=1
b=2
c=a+b

print("this is fun, I don't have to care about types haha, anyway the sum is:", c)

'''
OUTPUT

this is fun, I don't have to care about types haha, anyway the sum is: 3

'''
#********************************************************************************************************************************************************************************************
#Let's take an imput from the user
#x = input("Enter a number")
'''
x = x*x
print(x)
So I can't do this, because I took a string from the user even though it's not specified. 
I have to cast it into an int first, let's try that
'''
#x=int(x)
#print(x)

#********************************************************************************************************************************************************************************************
#Let's try a conditional
if b > a:
    print("b is greater than a")
    #Here I was indented here by the ide itself yay
    print("b is still greater than a")
else:
    print("b is less than a")

#********************************************************************************************************************************************************************************************
#For loop & other loops

for i in range(10):
    print(i)

#This is cool, but what if I want to iterate over a list
num = [1, 2, 3, 4, 5]
for i in num:
    print(i)
strs = ['apple', 'ball', a, 0]
for i in strs:
    print(i)
for i in range(len(strs)):
    print(strs[i])

'''
OUTPUT

apple
ball
1
0

'''
#********************************************************************************************************************************************************************************************
#Lists are cool, we will learn more about it


