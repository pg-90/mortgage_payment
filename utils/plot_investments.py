import matplotlib.pyplot as plt
import numpy as np

def plot_savings_and_investment(savings, investment_return, months):
    years = months / 12

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(years, savings, label="Accumulated Savings", color="blue")
    ax.plot(years, investment_return, label="Investment Return", color="green")

    ax.set_xlabel("Years")
    ax.set_ylabel("Amount (HUF)")
    ax.set_title("Savings vs Investment Return Over Time")
    ax.legend()
    ax.grid()

    # Improve x-axis readability
    ax.set_xticks(np.arange(0, max(years) + 1, 1))
    ax.set_xticklabels([str(int(i)) for i in np.arange(0, max(years) + 1, 1)])

    # Improve y-axis readability
    ax.ticklabel_format(style="plain", axis="y")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", "."))
    )

    return fig
