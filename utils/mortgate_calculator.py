# utils/mortgage_utils.py
import numpy as np
import matplotlib.pyplot as plt


def calculate_mortgage_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = years * 12

    if monthly_interest_rate == 0:
        monthly_payment = principal / total_payments
    else:
        monthly_payment = (
            principal
            * monthly_interest_rate
            * (1 + monthly_interest_rate) ** total_payments
        ) / ((1 + monthly_interest_rate) ** total_payments - 1)
    return monthly_payment


def generate_amortization_schedule(principal, annual_interest_rate, years):
    monthly_payment = calculate_mortgage_payment(principal, annual_interest_rate, years)
    remaining_balance = principal
    monthly_interest_rate = annual_interest_rate / 100 / 12

    months = np.arange(1, years * 12 + 1)
    principal_paid = []
    interest_paid = []
    balance = []

    for _ in months:
        interest = remaining_balance * monthly_interest_rate
        principal_component = monthly_payment - interest
        remaining_balance -= principal_component

        interest_paid.append(interest)
        principal_paid.append(principal_component)
        balance.append(remaining_balance)

    return months, principal_paid, interest_paid, balance
