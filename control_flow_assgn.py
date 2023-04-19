#class assignment
#Write a function that uses while, if and continue statements
#  to print all the even numbers between 0 and 50. 
def continue_statement():
    x=0
    while x<=50:
        x+=1
        if x%2 !=0:
            continue
        print(x)
 #Write a function that takes an integer argument and prints "Prime"
 # # if the number is prime, and "Not prime" if the number is not prime. 
def prime(num):
        if num<1:
            print(" num not a prime number")
        else:
             for n in range(2,num):
                  if (num%n) ==0:
                       print("num not a prime")
                       break
                  else:
                       print("num is a prime")

    #Write a function that takes a list of integers as input and prints 
     #the sum of all the even numbers in the list.
def nums(numbers): 
    total=[]
    answer=0
    for z in numbers:
        if z%2 ==0: 
            answer=answer+z
            total.append(z)
            
    print(sum(total))

#Write a function that takes any two integers as input, and prints the
#  sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def numbers(num1,num2):
    result=0
    for i in range(num1,num2+1):
         if i%3==0:
              result=result+i
    print(result)          
              


