num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num1=float(num1)
num2=float(num2)
sum=num1+num2
difference=abs(num1+num2)
product=num1*num2

if(num2!=0):
    quotient=num1/num2
else:
    printf("Undefined")
 
print("\nresults:")
print("sum=",sum)
print("Difference=",difference)
print("product=",product)
print("Quotient=",quotient)
