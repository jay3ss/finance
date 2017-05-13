#1/usr/bin/env python3
from pprint import pprint
from finance import amortization as am

p = 476000
i = 0.04
n = 360

schedule = am.get_schedule(p, i, n)

(payment, monthly_principals, monthly_interest, beg_balance, end_balance) = schedule

for i in range(n):
    output = "Payment: {:.2f} Princ: {:.2f} Int: {:.2f} Beg Bal: {:.2f} End Bal: {:.2f}".format(payment, monthly_principals[i], monthly_interest[i], beg_balance[i], end_balance[i])
    print (output)
