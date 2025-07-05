# write a program to find compound interese simple interest and compound amount and find the differences between them.

p = float(input("Enter the principal"))
t = int(input("Enter the time"))
r = int(input("Enter the rate"))

def simpleInterest(p,t,r):
    return (p*t*r)/100

def CompundInterest(p,t,r):
    return p*((1+r/100)**t)-1

def CompundAmount(p,t,r):
    return p*((1+r/100)**t)

a = simpleInterest(p,t,r)
b = CompundInterest(p,t,r)
c = CompundAmount(p,t,r)

print(f"principal: {a}")
print(f"Compunt Interest: {b}")
print(f"Compunt Amount: {c}")

print(f'The differences between them is {abs(a-b-c)}')