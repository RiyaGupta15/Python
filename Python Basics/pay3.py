def computepay(h,r):
    return h * r
def compute(h,r):
    return ((h * r) + (0.5 * r * (h-40)))

hrs = input("Enter Hours:")
rate = input("enter rate:")
h = float(hrs)
r = float(rate)
if h <= 40:
	p = computepay(h,r)
else:
    p = compute(h,r)
print("Pay",p)
