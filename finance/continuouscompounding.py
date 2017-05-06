from math import exp

def single_future_payment(p, r, n):
    return p*(exp(r*n))

def single_present_payment(f, r, n):
    return f*(exp(-r*n))

def cash_from_future(f, r, n):
    return f*(exp(r) - 1)/(exp(r*n) - 1)

def cash_from_present(p, r, n):
    return f*(exp(r*n)*(exp(r) - 1))/(exp(r*n) - 1)

def future_sum(a, r, n):
    return a*(exp(r*n) - 1)/(exp(r) - 1)

def present_sum(a, r, n):
    return a*(exp(r*n) - 1)/(exp(r*n)*(exp(r) - 1))
