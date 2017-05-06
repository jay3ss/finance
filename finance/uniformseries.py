def series_compound_amount(a, i, n):
    return a*((1 + i)**n - 1)/i

def sinking_fund(f, i, n):
    return f*i/((1 + i)**n - 1)

def capital_recovery(p, i, n):
    return p*i*(1 + i)**n/((1 + i)**n - 1)

def select_present_worth(a, i, n):
    return a*((1 + i)**n - 1)/(i*(1 + i)**n)
