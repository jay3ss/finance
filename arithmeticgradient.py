def uniform_series(g, i, n):
    return g*(1/i - n/((1 + i)**n - 1))

def present_worth(g, i, n):
    return g*(1/i**2 - (i*n - 1)/((i**2)*((1 + i)**n)))
