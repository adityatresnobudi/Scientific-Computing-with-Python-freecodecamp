sh = input("Enter Hours : ")
sr = input("Enter Rate : ")
fh = float(sh)
fr = float(sr)
normal = normal = (40*fr)
if fh > 40 :
    ot = (fh-40)*(1.5*fr)
    pay = normal + ot
else:
    pay = normal
print("Pay : {}".format(pay))