import matplotlib.pyplot as plt
from utils.mortgate_calculator import accumulate_mortgages


def plot_total_mortgage(mortgages):
    months, total_balance = accumulate_mortgages(mortgages)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(months, total_balance, label="Total Remaining Balance", color="blue")

    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (HUF)")
    ax.set_title("Total Mortgage Payment Breakdown")
    ax.legend()
    ax.grid()

    # Improve y-axis readability
    ax.ticklabel_format(style="plain", axis="y")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", "."))
    )

    return fig
