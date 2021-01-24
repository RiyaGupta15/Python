text = "X-DSPAM-Confidence:    0.8475";
t = text.find('0')
n = text[t:]
num = float(n)
print(num)
