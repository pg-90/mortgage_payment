# utils/mortgage_calculator.py
import numpy as np


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
    balance = []

    for _ in months:
        interest = remaining_balance * monthly_interest_rate
        principal_component = monthly_payment - interest
        remaining_balance -= principal_component
        balance.append(remaining_balance)

    return months, balance


def accumulate_mortgages(mortgages):
    total_years = max(m["years"] for m in mortgages)
    total_months = total_years * 12
    total_balance = np.zeros(total_months)
    months = np.arange(1, total_months + 1)

    for mortgage in mortgages:
        _, balance = generate_amortization_schedule(
            mortgage["principal"], mortgage["rate"], mortgage["years"]
        )
        total_balance[: len(balance)] += (
            balance  # Add balance to the corresponding months
        )

    return months, total_balance
