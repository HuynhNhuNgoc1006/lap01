# S(n) = 1/2 + 2/3 +...+n/n+1

s=0
n = int(input("nhap n:"))
while n <=0:
    n = int(input("nhap n:"))

for i in range(1, n+1):
    s += i / (i+1)
print(round(s, 2))  
