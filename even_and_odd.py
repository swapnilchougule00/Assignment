                     # even and odd
num=int(input('Enter any numbers :'))
odd = 0 
even = 0
for i in range(0,num):
    if i %2  :
        even += 1
    else:
        odd+=1

print('Total even numbers are',even)    
print('Total odd numbers are',odd)    

