def SimpleInterest(p, t, r=10):
    si = (p*r*t)/100
    return si

def total(p, si):
    return p + si

p = int(input("Enter principle : "))
r = int(input("Enter rates : "))
t = int(input("Enter time : "))

si = SimpleInterest(p, t, r)

print(si)
T = total(p, si)
print(T)