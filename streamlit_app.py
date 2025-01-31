# streamlit_app.py
import streamlit as st
from utils.plotter import plot_total_mortgage
from utils.plot_investments import plot_savings_and_investment
from utils.calculate_savings import calculate_savings_with_investment

st.title("Multi-Mortgage Tracker")

mortgages = []

st.subheader("Add Mortgage Loans")
num_loans = st.slider(
    "How many mortgage loans?", min_value=1, max_value=10, step=1, value=1
)

for i in range(num_loans):
    st.markdown(f"### Loan {i + 1}")
    principal_label = f"Loan {i + 1} Amount (HUF):"
    principal = st.slider(
        principal_label,
        min_value=1_000_000,
        max_value=100_000_000,
        step=500_000,
        key=f"principal_{i}",
    )
    st.text_input("Amount (HUF):", f"{principal:,}".replace(",", "."), disabled=True)
    interest_rate = st.slider(
        f"Loan {i + 1} Annual Interest Rate (%):",
        min_value=0.1,
        max_value=10.0,
        step=0.1,
        key=f"rate_{i}",
    )
    years = st.slider(
        f"Loan {i + 1} Term (Years):",
        min_value=1,
        max_value=35,
        step=1,
        key=f"years_{i}",
    )
    mortgages.append({"principal": principal, "rate": interest_rate, "years": years})

if st.button("Calculate Loan and Plot"):
    fig = plot_total_mortgage(mortgages)
    st.pyplot(fig)


## investments and savings
st.title("Savings and Investment Tracker")

# User Inputs for Savings and Investment Calculation
base_savings = st.slider(
    "Monthly Savings Amount (HUF):",
    min_value=50_000,
    max_value=2_000_000,
    step=10_000,
    value=500_000,
)
yearly_increase_rate = st.slider(
    "Yearly Increase in Savings (%):",
    min_value=0.0,
    max_value=50.0,
    step=0.1,
    value=10.0,
)
investment_base = st.slider(
    "Initial Stock Investment (HUF):",
    min_value=1_000_000,
    max_value=100_000_000,
    step=1_000_000,
    value=2_000_000,
)
investment_return_rate = st.slider(
    "Annual Investment Return Rate (%):",
    min_value=0.0,
    max_value=50.0,
    step=0.1,
    value=10.0,
)
years = st.slider(
    "Investment Period (Years):", min_value=1, max_value=30, step=1, value=5
)
current_savings = st.number_input(
    "Current Account Savings (HUF):", min_value=0, max_value=100_000_000, value=10_000_000
)

if st.button("Calculate Savings and Plot"):
    savings, investment_return, months = calculate_savings_with_investment(
        base_savings,
        yearly_increase_rate / 100,
        investment_base,
        investment_return_rate,
        years,
        current_savings,
    )
    fig = plot_savings_and_investment(savings, investment_return, months)
    st.pyplot(fig)
