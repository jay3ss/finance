def compound_amount(p, i, n):
    return p*(1 + i)**n

def present_worth(f, i, n):
    return f*(1 + i)**(-n)
