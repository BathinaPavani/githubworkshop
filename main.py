
print("hi")
print("chani")


print("Hi, My name is shivaram")
print("how are you guys")
print("this is karteek")


#in karteek point of view explaining the how to check the number is prome or not
#lets define one variable as a integer
a = -20
#if that variable is Zero or less than Zero it is not a prime number.
#and we all know if it is a prime number the mathematical condition is- it has to devide only with the 1 and itself
if a<=0:
    print("it is not a prime")
#so we checked the above condition if it passed it will generate it is not a prime num
#if it is not passed it will continue new operation nothing but 'else' operation.
else:    
    for i in range(2,a):
        if a%i == 0:
            print("not a prime")
            break
#in the above condition we are checking if it is a 
#positive number then except 1 and itself chack 
#all the numbers inbetween perfectly deviding or not.
#so the range b/w the 1 and itself writen using the range operation.
#if the condition passes then it will print 'not a prime'.
#if above condition not passed then it will go to next condition nothing but else
#then it will pring what the else statement says.
    else:
        print("it is prime")
