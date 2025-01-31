import matplotlib.pyplot as plt

def plot_mortgage(principal, annual_interest_rate, years):
    months, principal_paid, interest_paid, balance = generate_amortization_schedule(principal, annual_interest_rate, years)
    
    plt.figure(figsize=(10, 5))
    plt.plot(months, balance, label='Remaining Balance', color='blue')
    plt.fill_between(months, 0, principal_paid, color='green', alpha=0.5, label='Principal Paid')
    plt.fill_between(months, principal_paid, np.array(principal_paid) + np.array(interest_paid), color='red', alpha=0.5, label='Interest Paid')
    
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.title('Mortgage Payment Breakdown')
    plt.legend()
    plt.grid()
    plt.show()