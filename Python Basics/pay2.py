hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = h * r
if(h<=40):
    print(pay)
else:
    print(pay + (0.5 * r) * (h-40))
