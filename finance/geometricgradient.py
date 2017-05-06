def present_worth(a, g, i, n):
    if i == g:
        return a*(n*(1 + i)**-1)
    else:
        return a*((1 - ((1 + g)**n)*((1 + i)**-n))/(i - g))

def future_cash(a, g, j):
    return a*(1 + g)**(j - 1)
