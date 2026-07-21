import random

n = random.randint(1,100)

a = -1
guess = 1

while(a!=n):
    a = int(input("Guss the number:"))

    if(a>n):
        print("lower number please")
        guess += 1
    elif (a<n):
        print("Higher number please")
        guess +=1
    
print(f"You gussed the the right number {n} in {guess} attempts.") 