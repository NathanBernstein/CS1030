def sumup(num):
    i = 1
    z=0
    while i <= num:
        z+=i
        i+=1
    return z

num = input("Enter number you want to sum up to!")
print(sumup(int(num)))
