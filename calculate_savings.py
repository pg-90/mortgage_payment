import numpy as np


def calculate_savings_with_investment(
    base_savings,
    yearly_increase_rate,
    investment_base,
    investment_return_rate,
    years,
    current_savings,
):
    # Initialize arrays for savings and investment return
    months = years * 12
    savings = np.zeros(months)
    investment_return = np.zeros(months)

    # Initial savings and investment base
    current_savings = current_savings  # Start with user input for savings
    current_investment = investment_base

    for month in range(1, months + 1):
        # Calculate savings (increases yearly)
        if (
            month % 12 == 1 and month != 1
        ):  # Increase savings every year (i.e. after 12 months)
            base_savings *= 1 + yearly_increase_rate

        # Add monthly savings to the current savings
        current_savings += base_savings
        savings[month - 1] = current_savings

        # Calculate investment return (added yearly, no monthly compounding)
        if month % 12 == 0:  # At the end of each year
            current_investment += current_investment * (investment_return_rate / 100)
        investment_return[month - 1] = current_investment

    return (
        savings,
        investment_return,
        np.arange(1, months + 1),
    )  # Returns savings, investment return, months array
