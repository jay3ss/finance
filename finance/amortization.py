from finance import uniformseries as us

def current_payment(loan, interest, term):
    return us.capital_recovery(loan, interest/12, term)

def interest_payment(loan, interest):
    return interest/12 * loan

def current_principal(payment, interest):
    return payment - interest

def monthly_breakdown(payment, loan, interest, term):
    interest = interest_payment(loan, interest)
    principal = current_principal(payment, interest)
    return (interest, principal)

def get_schedule(loan, interest, term):
    payment = current_payment(loan, interest, term)
    monthly_principals = []
    monthly_interest = []
    beg_balance = []
    end_balance = []
    (tmp_payment, tmp_principal, tmp_interest) = (0, 0, 0)
    current_balance = loan

    for t in range(term):
        (intrst, principal) = monthly_breakdown(payment, current_balance, interest, term)
        monthly_principals.append(principal)
        monthly_interest.append(intrst)
        beg_balance.append(current_balance)
        current_balance -= principal
        end_balance.append(current_balance)

    return (payment, monthly_principals, monthly_interest, beg_balance, end_balance)
