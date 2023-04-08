def computepay(hours, rate):
    normal = normal = (40*rate)
    if hours > 40 :
        ot = (hours-40)*(1.5*rate)
        pay = normal + ot
    else:
        pay = normal
    return pay

sh = input("Enter Hours : ")
sr = input("Enter Rate : ")
fh = float(sh)
fr = float(sr)

print("Pay : {}".format(computepay(fh, fr)))